import json
import urllib.request
import asyncio
import websockets

TEST_LANGUAGES = [
    ("en", "English"),
    ("ta", "Tamil"),
    ("hi", "Hindi"),
    ("ml", "Malayalam"),
    ("te", "Telugu"),
    ("ar", "Arabic"),
    ("ja", "Japanese"),
    ("fr", "French")
]

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

        for code, name in TEST_LANGUAGES:
            print(f"\n=======================================================")
            print(f"  Testing Language: {code.upper()} ({name})")
            print(f"=======================================================")

            # Switch language
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
                const target = btns.find(b => b.innerText.includes('{name}'));
                if (target) {{
                    target.click();
                }} else {{
                    window.i18n?.changeLanguage('{code}');
                }}
            }})()
            """)
            await asyncio.sleep(0.8)

            # Read text
            info = await evaluate("""
            (() => {
                const h2 = document.querySelector('h2');
                const main = h2 ? h2.closest('.max-w-4xl') : null;
                const title = h2 ? h2.innerText : '';
                const regLabel = document.querySelector('.text-emerald-900.font-black')?.innerText || '';
                const masked = document.querySelector('.font-mono.font-black')?.innerText || '';
                const sendBtn = document.querySelector('button.bg-gradient-to-r span:last-child')?.innerText || '';
                const privacy = document.querySelector('.border-emerald-300 span:last-child')?.innerText || '';
                const dir = document.documentElement.dir;
                return {
                    lang: document.documentElement.lang,
                    dir,
                    title,
                    registeredNumberLabel: regLabel,
                    maskedPhone: masked,
                    privacyBadge: privacy,
                    sendButtonText: sendBtn
                };
            })()
            """)
            print(json.dumps(info, ensure_ascii=False, indent=2))

        # Test Send Live SMS and reactive language update
        print("\n=======================================================")
        print("  Testing Live SMS Send & Dynamic Language Switch")
        print("=======================================================")

        # Switch to Tamil
        print("1. Switching to Tamil...")
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
            const target = btns.find(b => b.innerText.includes('Tamil') || b.innerText.includes('தமிழ்'));
            if (target) target.click();
        })()
        """)
        await asyncio.sleep(0.8)

        # Click send SMS
        print("2. Clicking 'Send Live Test SMS'...")
        await evaluate("""
        (() => {
            const sendBtn = document.querySelector('button.bg-gradient-to-r');
            if (sendBtn) sendBtn.click();
        })()
        """)
        await asyncio.sleep(2.5)

        tamil_status = await evaluate("""
        (() => {
            const statusP = document.querySelector('.animate-fade-in p.font-black');
            const detailsP = document.querySelector('.animate-fade-in p.font-mono');
            return {
                status: statusP ? statusP.innerText : 'None',
                details: detailsP ? detailsP.innerText : 'None'
            };
        })()
        """)
        print("Tamil Status Box:", json.dumps(tamil_status, ensure_ascii=False, indent=2))

        # Switch to Hindi while status is visible
        print("\n3. Switching to Hindi while status is displayed...")
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
            const target = btns.find(b => b.innerText.includes('Hindi') || b.innerText.includes('हिन्दी'));
            if (target) target.click();
        })()
        """)
        await asyncio.sleep(0.8)

        hindi_status = await evaluate("""
        (() => {
            const statusP = document.querySelector('.animate-fade-in p.font-black');
            const detailsP = document.querySelector('.animate-fade-in p.font-mono');
            return {
                status: statusP ? statusP.innerText : 'None',
                details: detailsP ? detailsP.innerText : 'None'
            };
        })()
        """)
        print("Hindi Status Box (Instant Reactive Relocalization):", json.dumps(hindi_status, ensure_ascii=False, indent=2))

        # Switch to Arabic while status is visible
        print("\n4. Switching to Arabic while status is displayed...")
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
            const target = btns.find(b => b.innerText.includes('Arabic') || b.innerText.includes('العربية'));
            if (target) target.click();
        })()
        """)
        await asyncio.sleep(0.8)

        arabic_status = await evaluate("""
        (() => {
            const statusP = document.querySelector('.animate-fade-in p.font-black');
            const detailsP = document.querySelector('.animate-fade-in p.font-mono');
            return {
                dir: document.documentElement.dir,
                status: statusP ? statusP.innerText : 'None',
                details: detailsP ? detailsP.innerText : 'None'
            };
        })()
        """)
        print("Arabic Status Box (Instant Reactive Relocalization in RTL):", json.dumps(arabic_status, ensure_ascii=False, indent=2))

asyncio.run(main())
