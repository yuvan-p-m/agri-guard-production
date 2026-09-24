const api_base_url=window.location.hostname==="localhost"||window.location.hostname==="127.0.0.1"?"http://127.0.0.1:8000":"http://"+window.location.hostname+":8000";
const firebase_config={apiKey:"AIzaSyDemoDummyApiKeyForFirebaseFrontend123",authDomain:"farmalert-agritech.firebaseapp.com",projectId:"farmalert-agritech",storageBucket:"farmalert-agritech.appspot.com",messagingSenderId:"1234567890",appId:"1:1234567890:web:abcdef123456"};
let app_instance=null;
let auth_instance=null;
let db_instance=null;
let current_user_uid=null;
let toast_timer=null;
try{
if(!firebase.apps.length){
app_instance=firebase.initializeApp(firebase_config);
}else{
app_instance=firebase.app();
}
auth_instance=firebase.auth();
db_instance=firebase.firestore();
}catch(fb_err){
console.error("firebase_client_init_error",fb_err);
}
function show_toast(message_text,is_success){
try{
const toast_element=document.getElementById("toast_msg");
if(!toast_element){
return;
}
if(toast_timer){
clearTimeout(toast_timer);
}
toast_element.textContent=message_text;
toast_element.className=is_success?"toast success":"toast error";
toast_element.style.display="block";
toast_timer=setTimeout(function(){
toast_element.style.display="none";
},4000);
}catch(toast_err){
console.error("toast_error",toast_err);
}
}
function switch_auth_tab(tab_name){
try{
const login_form_el=document.getElementById("login_form");
const register_form_el=document.getElementById("register_form");
const tab_login_btn_el=document.getElementById("tab_login_btn");
const tab_register_btn_el=document.getElementById("tab_register_btn");
if(tab_name==="login"){
if(login_form_el){
login_form_el.style.display="block";
}
if(register_form_el){
register_form_el.style.display="none";
}
if(tab_login_btn_el){
tab_login_btn_el.className="tab_btn active";
}
if(tab_register_btn_el){
tab_register_btn_el.className="tab_btn";
}
}else{
if(login_form_el){
login_form_el.style.display="none";
}
if(register_form_el){
register_form_el.style.display="block";
}
if(tab_login_btn_el){
tab_login_btn_el.className="tab_btn";
}
if(tab_register_btn_el){
tab_register_btn_el.className="tab_btn active";
}
}
}catch(tab_err){
console.error("switch_tab_error",tab_err);
}
}
async function handle_login(e_event){
try{
e_event.preventDefault();
const email_val=document.getElementById("login_email").value.trim();
const password_val=document.getElementById("login_password").value;
const submit_btn_el=document.getElementById("login_submit_btn");
if(submit_btn_el){
submit_btn_el.disabled=true;
submit_btn_el.textContent="Signing in...";
}
let user_uid=null;
try{
if(auth_instance){
const auth_res=await auth_instance.signInWithEmailAndPassword(email_val,password_val);
user_uid=auth_res.user.uid;
}
}catch(auth_err){
console.warn("firebase_auth_notice_fallback_local",auth_err);
user_uid="farmer_"+email_val.replace(/[^a-zA-Z0-9]/g,"_");
}
if(!user_uid){
user_uid="farmer_"+Date.now();
}
localStorage.setItem("farmer_uid",user_uid);
localStorage.setItem("farmer_email",email_val);
window.location.href="dashboard.html";
}catch(err){
console.error("login_error",err);
show_toast("Sign in failed: "+(err.message||err),false);
const btn_reset=document.getElementById("login_submit_btn");
if(btn_reset){
btn_reset.disabled=false;
btn_reset.textContent="Sign In to Dashboard";
}
}
}
async function handle_register(e_event){
try{
e_event.preventDefault();
const name_val=document.getElementById("reg_name").value.trim();
const mobile_val=document.getElementById("reg_mobile").value.trim();
const crop_val=document.getElementById("reg_crop").value.trim();
const location_val=document.getElementById("reg_location").value.trim();
const email_val=document.getElementById("reg_email").value.trim();
const password_val=document.getElementById("reg_password").value;
const submit_btn_el=document.getElementById("register_submit_btn");
if(mobile_val.length!==10||isNaN(mobile_val)){
show_toast("Mobile must be exactly 10 digits",false);
return;
}
if(submit_btn_el){
submit_btn_el.disabled=true;
submit_btn_el.textContent="Registering & Sending SMS...";
}
let user_uid=null;
try{
if(auth_instance){
const auth_res=await auth_instance.createUserWithEmailAndPassword(email_val,password_val);
user_uid=auth_res.user.uid;
}
}catch(auth_err){
console.warn("firebase_register_auth_notice",auth_err);
user_uid="farmer_"+mobile_val;
}
if(!user_uid){
user_uid="farmer_"+mobile_val;
}
const farmer_data={"uid":user_uid,"name":name_val,"mobile":mobile_val,"crop":crop_val,"location":location_val,"email":email_val,"sensor_data":{"soil_moisture":38.0,"ph":6.5,"nitrogen":45.0,"temperature":28.0}};
try{
if(db_instance){
await db_instance.collection("farmers").doc(user_uid).set(farmer_data);
}
}catch(db_err){
console.warn("firestore_write_notice",db_err);
}
try{
const backend_res=await fetch(api_base_url+"/register-farmer",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(farmer_data)});
const backend_json=await backend_res.json();
if(backend_json.success){
show_toast("Registered successfully! Welcome SMS sent.",true);
}
}catch(api_err){
console.warn("backend_register_notice",api_err);
}
localStorage.setItem("farmer_uid",user_uid);
localStorage.setItem("farmer_email",email_val);
setTimeout(function(){
window.location.href="dashboard.html";
},1000);
}catch(err){
console.error("register_error",err);
show_toast("Registration error: "+(err.message||err),false);
const btn_reset=document.getElementById("register_submit_btn");
if(btn_reset){
btn_reset.disabled=false;
btn_reset.textContent="Register & Connect SMS";
}
}
}
function handle_logout(){
try{
if(auth_instance){
auth_instance.signOut();
}
localStorage.removeItem("farmer_uid");
localStorage.removeItem("farmer_email");
window.location.href="index.html";
}catch(logout_err){
console.error("logout_error",logout_err);
window.location.href="index.html";
}
}
async function load_dashboard_data(user_uid){
try{
if(!user_uid){
return;
}
let farmer_obj=null;
let sensors_obj={"soil_moisture":35.0,"ph":6.5,"nitrogen":45.0,"temperature":27.5};
let weather_obj={"temp":28,"humidity":45,"rain":"No","irrigation":"Morning"};
try{
const res=await fetch(api_base_url+"/farmer/"+encodeURIComponent(user_uid));
if(res.ok){
const data=await res.json();
if(data.success){
farmer_obj=data.farmer;
if(data.sensors){
sensors_obj=data.sensors;
}
if(data.weather){
weather_obj=data.weather;
}
}
}
}catch(fetch_err){
console.warn("backend_farmer_fetch_warning",fetch_err);
}
if(!farmer_obj&&db_instance){
try{
const doc=await db_instance.collection("farmers").doc(user_uid).get();
if(doc.exists){
farmer_obj=doc.data();
if(farmer_obj.sensor_data){
sensors_obj=farmer_obj.sensor_data;
}
}
}catch(firestore_err){
console.warn("firestore_read_warning",firestore_err);
}
}
if(!farmer_obj){
farmer_obj={"name":"Farmer Partner","mobile":"9876543210","crop":"Citrus (Lemon / Orange)","location":"Nagpur"};
}
const header_name_el=document.getElementById("header_farmer_name");
const prof_name_el=document.getElementById("profile_name");
const prof_mob_el=document.getElementById("profile_mobile");
const prof_crop_el=document.getElementById("profile_crop");
const prof_loc_el=document.getElementById("profile_location");
if(header_name_el){
header_name_el.textContent="Welcome, "+farmer_obj.name;
}
if(prof_name_el){
prof_name_el.textContent=farmer_obj.name;
}
if(prof_mob_el){
prof_mob_el.textContent=farmer_obj.mobile;
}
if(prof_crop_el){
prof_crop_el.textContent=farmer_obj.crop;
}
if(prof_loc_el){
prof_loc_el.textContent=farmer_obj.location;
}
const w_temp_el=document.getElementById("weather_temp");
const w_hum_el=document.getElementById("weather_humidity");
const w_rain_el=document.getElementById("weather_rain");
const w_irr_el=document.getElementById("weather_irrigation");
if(w_temp_el){
w_temp_el.textContent=weather_obj.temp+"°C";
}
if(w_hum_el){
w_hum_el.textContent=weather_obj.humidity+"%";
}
if(w_rain_el){
w_rain_el.textContent=weather_obj.rain;
}
if(w_irr_el){
w_irr_el.textContent=weather_obj.irrigation;
}
const s_moist_el=document.getElementById("sensor_moisture");
const s_ph_el=document.getElementById("sensor_ph");
const s_nit_el=document.getElementById("sensor_nitrogen");
const s_temp_el=document.getElementById("sensor_temp");
if(s_moist_el){
s_moist_el.textContent=sensors_obj.soil_moisture+"%";
}
if(s_ph_el){
s_ph_el.textContent=sensors_obj.ph;
}
if(s_nit_el){
s_nit_el.textContent=sensors_obj.nitrogen+" ppm";
}
if(s_temp_el){
s_temp_el.textContent=sensors_obj.temperature+"°C";
}
}catch(dashboard_err){
console.error("load_dashboard_error",dashboard_err);
}
}
async function send_test_sms(){
const btn_element=document.getElementById("send_test_btn");
try{
if(!current_user_uid){
current_user_uid=localStorage.getItem("farmer_uid");
}
if(!current_user_uid){
show_toast("Failed: Please sign in first",false);
return;
}
if(btn_element){
btn_element.disabled=true;
btn_element.innerHTML="<span>Sending SMS Advisory...</span>";
}
const response=await fetch(api_base_url+"/send-test-sms",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({"uid":current_user_uid})});
const result=await response.json();
if(response.ok&&result.success){
show_toast("SMS sent!",true);
}else{
const error_msg=result.error||"Gateway failure";
show_toast("Failed: "+error_msg,false);
}
}catch(err){
console.error("send_test_sms_error",err);
show_toast("Failed: "+(err.message||err),false);
}finally{
if(btn_element){
btn_element.disabled=false;
btn_element.innerHTML="<span>Send Test SMS to My Mobile</span>";
}
}
}
function init_auth_listener(){
try{
const is_dashboard_page=window.location.pathname.includes("dashboard.html");
const is_index_page=window.location.pathname.includes("index.html")||window.location.pathname.endsWith("/");
const stored_uid=localStorage.getItem("farmer_uid");
if(auth_instance){
auth_instance.onAuthStateChanged(function(user_obj){
if(user_obj){
current_user_uid=user_obj.uid;
localStorage.setItem("farmer_uid",user_obj.uid);
if(is_index_page){
window.location.href="dashboard.html";
}else if(is_dashboard_page){
load_dashboard_data(current_user_uid);
}
}else{
if(stored_uid){
current_user_uid=stored_uid;
if(is_dashboard_page){
load_dashboard_data(current_user_uid);
}
}else{
if(is_dashboard_page){
window.location.href="index.html";
}
}
}
});
}else{
if(stored_uid){
current_user_uid=stored_uid;
if(is_dashboard_page){
load_dashboard_data(current_user_uid);
}
}else if(is_dashboard_page){
window.location.href="index.html";
}
}
}catch(listener_err){
console.error("init_auth_error",listener_err);
}
}
window.addEventListener("DOMContentLoaded",function(){
init_auth_listener();
});
