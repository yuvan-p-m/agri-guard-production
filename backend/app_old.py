import os,logging,uvicorn
from fastapi import FastAPI,HTTPException,Request,Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional,Dict,Any
from dotenv import load_dotenv
load_dotenv()
from sms_service import send_sms
from weather_service import get_weather
from firebase_service import create_or_update_farmer,get_farmer_by_uid,get_farmer_sensor_data
from scheduler import start_scheduler
logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)
app=FastAPI(title="FarmAlert SMS Backend")
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])
class FarmerRegisterModel(BaseModel):
    uid:str
    name:str
    mobile:str
    crop:Optional[str]="Citrus"
    location:Optional[str]="Nagpur"
    sensor_data:Optional[Dict[str,Any]]=None
class TestSmsModel(BaseModel):
    uid:str
class SensorUpdateModel(BaseModel):
    uid:str
    soil_moisture:Optional[float]=35.0
    ph:Optional[float]=6.5
    nitrogen:Optional[float]=45.0
    temperature:Optional[float]=27.5
@app.on_event("startup")
def startup_event():
    try:
        start_scheduler()
    except Exception as sched_e:
        logger.error(f"scheduler_init_warning:{str(sched_e)}")
@app.get("/health")
def health_check():
    return {"status":"healthy","service":"farmalert_fastapi_sms_system"}
@app.post("/register-farmer")
@app.post("/api/register-farmer")
def register_farmer_route(payload:FarmerRegisterModel):
    try:
        uid=payload.uid.strip()
        name=payload.name.strip()
        mobile=payload.mobile.strip()
        crop=payload.crop.strip() if payload.crop else "Citrus"
        location=payload.location.strip() if payload.location else "Nagpur"
        if not uid or not name or not mobile:
            raise HTTPException(status_code=400,detail="missing_required_fields")
        sensor_dict=payload.sensor_data or {"soil_moisture":38.0,"ph":6.5,"nitrogen":45.0,"temperature":28.0}
        farmer_record={"uid":uid,"name":name,"mobile":mobile,"crop":crop,"location":location,"sensor_data":sensor_dict}
        saved=create_or_update_farmer(farmer_record)
        welcome_message=f"Welcome to FarmAlert, {name}! Your farm is now connected. You will receive daily weather, soil and farming tip alerts. Stay informed, farm smarter."
        sms_result=send_sms(mobile,welcome_message)
        return {"success":True,"sms_sent":sms_result,"farmer":saved}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"register_farmer_exception:{str(e)}")
        raise HTTPException(status_code=500,detail=str(e))
@app.post("/send-test-sms")
@app.post("/api/send-test-sms")
def send_test_sms_route(payload:TestSmsModel):
    try:
        uid=payload.uid.strip()
        if not uid:
            raise HTTPException(status_code=400,detail="missing_farmer_uid")
        farmer=get_farmer_by_uid(uid)
        if not farmer:
            raise HTTPException(status_code=404,detail="farmer_not_found_in_firestore")
        name=farmer.get("name","Farmer").strip()
        mobile=str(farmer.get("mobile","")).strip()
        location=farmer.get("location","Nagpur")
        if not mobile:
            raise HTTPException(status_code=400,detail="farmer_mobile_missing")
        weather_info=get_weather(location)
        temp=weather_info.get("temp",28)
        humidity=weather_info.get("humidity",45)
        rain=weather_info.get("rain","No")
        irrigation=weather_info.get("irrigation","Morning")
        message=f"Good Morning {name}! Today: Temp {temp}C, Humidity {humidity}%, Rain: {rain}. Best irrigation time: {irrigation}."
        sent=send_sms(mobile,message)
        if sent:
            return {"success":True,"message":"test_sms_sent_successfully"}
        else:
            raise HTTPException(status_code=500,detail="sms_gateway_delivery_failed")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"send_test_sms_exception:{str(e)}")
        raise HTTPException(status_code=500,detail=str(e))
@app.get("/farmer/{uid}")
@app.get("/api/farmer/{uid}")
def get_farmer_data_route(uid:str):
    try:
        farmer=get_farmer_by_uid(uid)
        if not farmer:
            raise HTTPException(status_code=404,detail="farmer_not_found")
        sensors=get_farmer_sensor_data(farmer)
        loc=farmer.get("location","Nagpur")
        weather=get_weather(loc)
        return {"success":True,"farmer":farmer,"sensors":sensors,"weather":weather}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"get_farmer_exception:{str(e)}")
        raise HTTPException(status_code=500,detail=str(e))
@app.post("/update-sensors")
@app.post("/api/update-sensors")
def update_sensors_route(payload:SensorUpdateModel):
    try:
        uid=payload.uid.strip()
        if not uid:
            raise HTTPException(status_code=400,detail="missing_uid")
        sensor_data={"soil_moisture":float(payload.soil_moisture or 35.0),"ph":float(payload.ph or 6.5),"nitrogen":float(payload.nitrogen or 45.0),"temperature":float(payload.temperature or 27.5)}
        updated=create_or_update_farmer({"uid":uid,"sensor_data":sensor_data})
        return {"success":True,"sensors":sensor_data}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"update_sensors_exception:{str(e)}")
        raise HTTPException(status_code=500,detail=str(e))
if __name__=="__main__":
    port_num=int(os.getenv("PORT",8000))
    uvicorn.run("app:app",host="0.0.0.0",port=port_num,reload=False)
