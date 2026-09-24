const API_BASE_URL="http://127.0.0.1:8000/api";
let chart_instance=null;

async function fetch_marketplace_data(){
  const crop_val=document.getElementById("crop-select").value;
  const state_val=document.getElementById("state-select").value;

  fetch_crop_alert(crop_val);
  fetch_mandi_prices(crop_val,state_val);
  fetch_price_forecast(crop_val,state_val);
}

async function fetch_crop_alert(crop_val){
  try{
    const res=await fetch(`${API_BASE_URL}/crop-alert?crop=${encodeURIComponent(crop_val)}`);
    const data=await res.json();
    if(data&&data.status==="success"){
      document.getElementById("crop-alert-box").classList.remove("hidden");
      document.getElementById("alert-title").textContent=`Crop Calendar Advisory — ${data.crop}`;
      document.getElementById("alert-message").textContent=data.message;
      document.getElementById("alert-rec").textContent=`💡 ${data.recommendation}`;
    }
  }catch(e){
    console.warn("Crop alert notice:",e);
  }
}

async function fetch_mandi_prices(crop_val,state_val){
  const table_body=document.getElementById("mandi-table-body");
  table_body.innerHTML='<tr><td colspan="6" class="py-6 text-center text-slate-400">Loading live mandi rates...</td></tr>';

  try{
    const res=await fetch(`${API_BASE_URL}/mandi-prices`,{
      method:"POST",
      headers:{"Content-Type":"application/json"},
      body:JSON.stringify({crop:crop_val,state:state_val})
    });
    const data=await res.json();
    const records=data.records||[];

    document.getElementById("last-updated-text").textContent=data.last_updated||"Live";

    if(records.length===0){
      table_body.innerHTML='<tr><td colspan="6" class="py-6 text-center text-rose-600 font-bold">No price data available for your crop in your state today. Try again tomorrow.</td></tr>';
      document.getElementById("best-market-banner").classList.add("hidden");
      return;
    }

    const sorted_records=[...records].sort((a,b)=>Number(b.modal_price)-Number(a.modal_price));
    const best_rec=sorted_records[0];
    const worst_rec=sorted_records[sorted_records.length-1];

    if(best_rec){
      document.getElementById("best-market-banner").classList.remove("hidden");
      document.getElementById("best-market-text").textContent=`Best market today: ${best_rec.market} (${best_rec.district}) at ₹${best_rec.modal_price}/quintal`;
      document.getElementById("best-market-badge").textContent=`₹${best_rec.modal_price} / Q`;
    }

    table_body.innerHTML=sorted_records.map((r)=>{
      const is_best=best_rec&&r.market===best_rec.market&&r.modal_price===best_rec.modal_price;
      const is_worst=worst_rec&&r.market===worst_rec.market&&r.modal_price===worst_rec.modal_price;

      let row_cls="bg-white hover:bg-slate-50";
      if(is_best){
        row_cls="bg-emerald-50 font-bold border-l-4 border-emerald-600";
      }else if(is_worst){
        row_cls="bg-rose-50 text-rose-950 border-l-4 border-rose-500";
      }

      return `<tr class="${row_cls}">
        <td class="py-3 px-4 font-black">
          ${r.market}
          ${is_best?'<span class="ml-2 px-2 py-0.5 bg-emerald-600 text-white rounded-full text-[9px]">BEST</span>':''}
          ${is_worst?'<span class="ml-2 px-2 py-0.5 bg-rose-500 text-white rounded-full text-[9px]">LOWEST</span>':''}
        </td>
        <td class="py-3 px-4 text-slate-600">${r.district}</td>
        <td class="py-3 px-4 text-center font-mono">₹${r.min_price}</td>
        <td class="py-3 px-4 text-center font-mono">₹${r.max_price}</td>
        <td class="py-3 px-4 text-right font-mono font-black text-emerald-950">₹${r.modal_price}</td>
        <td class="py-3 px-4 text-right text-slate-500 font-mono text-[11px]">${r.arrival_date}</td>
      </tr>`;
    }).join("");

  }catch(e){
    table_body.innerHTML='<tr><td colspan="6" class="py-6 text-center text-rose-600 font-bold">Failed to load mandi prices. Please retry.</td></tr>';
  }
}

async function fetch_price_forecast(crop_val,state_val){
  try{
    const res=await fetch(`${API_BASE_URL}/price-forecast`,{
      method:"POST",
      headers:{"Content-Type":"application/json"},
      body:JSON.stringify({crop:crop_val,state:state_val})
    });
    const data=await res.json();
    render_forecast_chart(data);
    render_verdict_card(data);
  }catch(e){
    console.warn("Forecast fetch notice:",e);
  }
}

function render_forecast_chart(data){
  const ctx=document.getElementById("priceTrendChart").getContext("2d");
  if(chart_instance){
    chart_instance.destroy();
  }

  const hist_prices=(data.weekly_prices||[]).map((w)=>w.price);
  const labels=(data.weekly_prices||[]).map((w,i)=>`W${i+1}`);
  const forecast=data.forecast||[];

  const full_labels=[...labels,"+W1 (F)","+W2 (F)","+W3 (F)"];
  const hist_series=[...hist_prices,null,null,null];
  const last_hist_val=hist_prices[hist_prices.length-1];
  const forecast_series=new Array(hist_prices.length-1).fill(null);
  forecast_series.push(last_hist_val,...forecast);

  chart_instance=new Chart(ctx,{
    type:"line",
    data:{
      labels:full_labels,
      datasets:[
        {
          label:"Historical (8 Weeks)",
          data:hist_series,
          borderColor:"#4F46E5",
          backgroundColor:"#4F46E5",
          borderWidth:3,
          tension:0.3,
          pointRadius:4
        },
        {
          label:"3-Week Forecast",
          data:forecast_series,
          borderColor:"#10B981",
          backgroundColor:"#10B981",
          borderWidth:3,
          borderDash:[6,6],
          tension:0.3,
          pointRadius:5
        }
      ]
    },
    options:{
      responsive:true,
      plugins:{
        tooltip:{
          callbacks:{
            label:(c)=>`₹${c.parsed.y} / Quintal`
          }
        }
      },
      scales:{
        y:{
          ticks:{
            callback:(v)=>`₹${v}`
          }
        }
      }
    }
  });
}

function render_verdict_card(data){
  const v_title=document.getElementById("verdict-title");
  const v_badge=document.getElementById("verdict-badge");
  const v_rec=document.getElementById("verdict-rec");
  const v_count=document.getElementById("verdict-count");
  const v_box=document.getElementById("verdict-box");

  const pct=data.pct_change||0;
  const trend=data.trend||"STABLE";

  if(trend==="RISING"){
    v_box.className="p-5 rounded-2xl border-2 bg-emerald-50 border-emerald-300 text-emerald-950";
    v_badge.className="px-3 py-1 rounded-full text-xs font-black bg-emerald-600 text-white";
    v_title.textContent="Prices rising — Hold your crop";
  }else if(trend==="FALLING"){
    v_box.className="p-5 rounded-2xl border-2 bg-rose-50 border-rose-300 text-rose-950";
    v_badge.className="px-3 py-1 rounded-full text-xs font-black bg-rose-600 text-white";
    v_title.textContent="Prices falling — Sell now";
  }else{
    v_box.className="p-5 rounded-2xl border-2 bg-blue-50 border-blue-300 text-blue-950";
    v_badge.className="px-3 py-1 rounded-full text-xs font-black bg-blue-600 text-white";
    v_title.textContent="Prices stable";
  }

  v_badge.textContent=`${pct>0?`+${pct}%`:`${pct}%`} 3-Week`;
  v_rec.textContent=`🎯 Recommendation: ${data.recommendation||"Monitor local mandi rates"}`;
  v_count.textContent=`Based on ${data.record_count||50} price records from last 8 weeks across ${data.state||"State"}`;
}

document.addEventListener("DOMContentLoaded",()=>{
  document.getElementById("crop-select").addEventListener("change",fetch_marketplace_data);
  document.getElementById("state-select").addEventListener("change",fetch_marketplace_data);
  document.getElementById("refresh-btn").addEventListener("click",fetch_marketplace_data);

  document.getElementById("toggle-mandi-btn").addEventListener("click",()=>{
    const el=document.getElementById("mandi-section-body");
    el.classList.toggle("hidden");
  });

  document.getElementById("toggle-forecast-btn").addEventListener("click",()=>{
    const el=document.getElementById("forecast-section-body");
    el.classList.toggle("hidden");
  });

  fetch_marketplace_data();
});
