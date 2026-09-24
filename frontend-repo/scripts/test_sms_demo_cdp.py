import json
import urllib.request
import asyncio
import websockets

async def main():
    req = urllib.request.urlopen("http://localhost:9222/json")
    targets = json.loads(req.read().decode())
    ws_url = targets[0]["webSocketDebuggerUrl"]
    print(f"Connecting to: {ws_url}")

    async with websockets.connect(ws_url) as ws:
        async def evaluate(expr):
            payload = {
                "id": 1,
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

        # 1. Switch to SMS Demo Tab
        print("Navigating to SMS Demo Tab...")
        nav_res = await evaluate("""
        (() => {
            const btns = Array.from(document.querySelectorAll('button'));
            const smsBtn = btns.find(b => b.innerText && (
                b.innerText.includes('SMS Demo') || 
                b.innerText.includes('SMS டெமோ') || 
                b.innerText.includes('SMS')
            ));
            if (smsBtn) {
                smsBtn.click();
                return 'Clicked SMS tab: ' + smsBtn.innerText.trim();
            }
            return 'SMS Tab not found';
        })()
        """)
        print(nav_res)
        await asyncio.sleep(1)

        # 2. Test languages across the requested set
        test_languages = [
            ("en", "English"),
            ("ta", "Tamil"),
            ("hi", "Hindi"),
            ("ml", "Malayalam"),
            ("te", "Telugu"),
            ("ar", "Arabic"),
            ("ja", "Japanese")
        ]

        results = {}

        for code, name in test_languages:
            print(f"\n================ Testing Language: {code} ({name}) ================")
            
            # Switch language via app header dropdown
            await evaluate(f"""
            (() => {{
                const btn = document.querySelector('button[aria-label=\"Select Language\"]');
                if (btn) btn.click();
            }})()
            """)
            await asyncio.sleep(0.4)
            await evaluate(f"""
            (() => {{
                const btns = Array.from(document.querySelectorAll('button'));
                // Match by code or native name
                const target = btns.find(b => b.innerText.includes('{name}') || b.dataset?.lang === '{code}');
                if (target) target.click();
                else {{
                    // Fallback to changing via i18n
                    window.i18n?.changeLanguage('{code}');
                }}
            }})()
            """)
            await asyncio.sleep(0.8)

            # Inspect elements
            screen_info = await evaluate("""
            (() => {
                const h2 = document.querySelector('h2');
                const title = h2 ? h2.innerText : '';
                const p = h2 ? h2.closest('.flex-wrap')?.parentElement?.querySelector('p')?.innerText : '';
                const gatewayBadge = document.querySelector('.bg-sky-100 span:last-child')?.innerText || '';
                const privacyBadge = document.querySelector('.bg-white.border-emerald-300 span:last-child')?.innerText || '';
                const registeredNumberLabel = document.querySelector('.text-emerald-900.font-black')?.innerText || '';
                const maskedPhone = document.querySelector('.font-mono.font-black')?.innerText || '';
                const sendBtn = document.querySelector('button.bg-gradient-to-r span:last-child')?.innerText || '';
                const dir = document.documentElement.dir;
                const lang = document.documentElement.lang;
                return {
                    lang,
                    dir,
                    title,
                    subtitle: p,
                    gatewayBadge,
                    privacyBadge,
                    registeredNumberLabel,
                    maskedPhone,
                    sendBtn
                };
            })()
            """)
            results[code] = screen_info
            print(json.dumps(screen_info, ensure_ascii=False, indent=2))

        # 3. Test sending live SMS in Tamil and observe reactive translation on language switch
        print("\n--- Testing Live SMS Send & Reactive Translation Update ---")
        # Switch to Tamil
        await evaluate("""
        (() => {
            const btn = document.querySelector('button[aria-label=\"Select Language\"]');
            if (btn) btn.click();
        })()
        """)
        await asyncio.sleep(0.4)
        await evaluate("""
        (() => {
            const btns = Array.from(document.querySelectorAll('button'));
            const target = btns.find(b => b.innerText.includes('தமிழ்'));
            if (target) target.click();
        })()
        """)
        await asyncio.sleep(0.8)

        # Click send button
        await evaluate("""
        (() => {
            const sendBtn = document.querySelector('button.bg-gradient-to-r');
            if (sendBtn) sendBtn.click();
        })()
        """)
        # Wait for API response
        await asyncio.sleep(2.5)

        tamil_status = await evaluate("""
        (() => {
            const statusBox = document.querySelector('.animate-fade-in p.font-black');
            const detailsBox = document.querySelector('.animate-fade-in p.font-mono');
            return {
                statusText: statusBox ? statusBox.innerText : 'None',
                details: detailsBox ? detailsBox.innerText : 'None'
            };
        })()
        """)
        print("Tamil Send Status:", json.dumps(tamil_status, ensure_ascii=False, indent=2))

        # Switch to Hindi while status is visible -> verify it automatically becomes Hindi!
        print("\nSwitching to Hindi while status message is displayed...")
        await evaluate("""
        (() => {
            const btn = document.querySelector('button[aria-label=\"Select Language\"]');
            if (btn) btn.click();
        })()
        """)
        await asyncio.sleep(0.4)
        await evaluate("""
        (() => {
            const btns = Array.from(document.querySelectorAll('button'));
            const target = btns.find(b => b.innerText.includes('हिन्दी'));
            if (target) target.click();
        })()
        """)
        await asyncio.sleep(0.8)

        hindi_status = await evaluate("""
        (() => {
            const statusBox = document.querySelector('.animate-fade-in p.font-black');
            const detailsBox = document.querySelector('.animate-fade-in p.font-mono');
            return {
                statusText: statusBox ? statusBox.innerText : 'None',
                details: detailsBox ? detailsBox.innerText : 'None'
            };
        })()
        """)
        print("Hindi Re-rendered Status (No Stale Tamil!):", json.dumps(hindi_status, ensure_ascii=False, indent=2))

        # Switch to Arabic -> verify RTL and Arabic status
        print("\nSwitching to Arabic while status message is displayed...")
        await evaluate("""
        (() => {
            const btn = document.querySelector('button[aria-label=\"Select Language\"]');
            if (btn) btn.click();
        })()
        """)
        await asyncio.sleep(0.4)
        await evaluate("""
        (() => {
            const btns = Array.from(document.querySelectorAll('button'));
            const target = btns.find(b => b.innerText.includes('العربية'));
            if (target) target.click();
        })()
        """)
        await asyncio.sleep(0.8)

        arabic_status = await evaluate("""
        (() => {
            const statusBox = document.querySelector('.animate-fade-in p.font-black');
            const detailsBox = document.querySelector('.animate-fade-in p.font-mono');
            return {
                dir: document.documentElement.dir,
                statusText: statusBox ? statusBox.innerText : 'None',
                details: detailsBox ? detailsBox.innerText : 'None'
            };
        })()
        """)
        print("Arabic Re-rendered Status (No Stale Tamil/Hindi!):", json.dumps(arabic_status, ensure_ascii=False, indent=2))

asyncio.run(main())
