import json
import urllib.request
import asyncio
import websockets
import base64
import os

async def main():
    req = urllib.request.urlopen("http://localhost:9222/json")
    targets = json.loads(req.read().decode())
    ws_url = targets[0]["webSocketDebuggerUrl"]
    print(f"Connecting to: {ws_url}")

    async with websockets.connect(ws_url) as ws:
        async def evaluate(expr):
            msg_id = 1
            payload = {
                "id": msg_id,
                "method": "Runtime.evaluate",
                "params": {
                    "expression": expr,
                    "returnByValue": True,
                    "awaitPromise": True
                }
            }
            await ws.send(json.dumps(payload))
            resp = await ws.recv()
            data = json.loads(resp)
            return data.get("result", {}).get("result", {}).get("value")

        # 1. Check current language and switch to Govt Schemes tab
        print("Switching tab to Govt Schemes...")
        switch_tab_res = await evaluate("""
        (() => {
            // Find tab button for govt schemes
            const buttons = Array.from(document.querySelectorAll('button'));
            const govtBtn = buttons.find(b => b.textContent && (
                b.textContent.includes('Govt Schemes') || 
                b.textContent.includes('அரசு திட்டங்கள்') || 
                b.textContent.includes('योजना')
            ));
            if (govtBtn) {
                govtBtn.click();
                return "Clicked via button text: " + govtBtn.textContent.trim();
            }
            // Or look for icon or aria
            return "Tab button not found directly, checking available nav tabs: " + buttons.map(b => b.textContent.trim()).filter(Boolean).join(' | ');
        })()
        """)
        print("Tab switch result:", switch_tab_res)

        await asyncio.sleep(1)

        # Let's test languages
        test_languages = ['ta', 'hi', 'te', 'ar', 'ja', 'en']
        results = {}

        for lang in test_languages:
            print(f"\n--- Testing Language: {lang} ---")
            # Switch language via i18n
            res = await evaluate(f"""
            (() => {{
                if (window.i18n) {{
                    window.i18n.changeLanguage('{lang}');
                }} else {{
                    localStorage.setItem('agriguard_language', '{lang}');
                    localStorage.setItem('i18nextLng', '{lang}');
                    document.documentElement.lang = '{lang}';
                    if (['ar', 'ur'].includes('{lang}')) {{
                        document.documentElement.dir = 'rtl';
                    }} else {{
                        document.documentElement.dir = 'ltr';
                    }}
                    window.dispatchEvent(new Event('storage'));
                }}
                return document.documentElement.lang;
            }})()
            """)
            
            # Or use React trigger / language selector button if available
            await evaluate(f"""
            (() => {{
                // Find language selector button if available
                const selects = Array.from(document.querySelectorAll('select'));
                // Or language dropdown
                const selectLang = selects.find(s => Array.from(s.options).some(o => o.value === '{lang}'));
                if (selectLang) {{
                    selectLang.value = '{lang}';
                    selectLang.dispatchEvent(new Event('change', {{ bubbles: true }}));
                }}
            }})()
            """)
            await asyncio.sleep(0.8)

            # Check rendered text in the GovtSchemesTab
            info = await evaluate("""
            (() => {
                const h2 = document.querySelector('h2');
                const title = h2 ? h2.textContent : '';
                const badge = document.querySelector('.bg-agri-100 span');
                const badgeText = badge ? badge.textContent : '';
                const schemeCards = Array.from(document.querySelectorAll('.group h3')).map(h => h.textContent);
                const schemeSub = Array.from(document.querySelectorAll('.group h3 + p')).map(p => p.textContent);
                const schemeBenefits = Array.from(document.querySelectorAll('.group .bg-slate-50\\/90 span:last-child')).map(s => s.textContent);
                const categoryBadges = Array.from(document.querySelectorAll('.group span.shadow-2xs')).map(s => s.textContent);
                const dir = document.documentElement.dir;
                return {
                    title,
                    badgeText,
                    schemeCount: schemeCards.length,
                    firstScheme: schemeCards[0] || '',
                    firstSchemeFullName: schemeSub[0] || '',
                    firstBenefit: schemeBenefits[0] || '',
                    firstCategory: categoryBadges[0] || '',
                    dir
                };
            })()
            """)
            results[lang] = info
            print(f"Results for {lang}:", json.dumps(info, ensure_ascii=False, indent=2))

        print("\nAll language test completed successfully!")

asyncio.run(main())
