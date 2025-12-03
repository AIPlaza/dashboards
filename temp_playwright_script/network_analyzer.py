import asyncio
from playwright.async_api import async_playwright
import json
import re

async def analyze_binance_p2p_requests(url):
    results = []
    async with async_playwright() as p:
        # Launch browser in headless mode
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Set up request interception
        page.on("request", lambda request: asyncio.create_task(handle_request(request, results)))

        print(f"Navigating to {url}...")
        try:
            await page.goto(url, wait_until="networkidle", timeout=90000) # Increased timeout
            print("Page loaded. Waiting for additional requests...")
            # Give it a bit more time for all dynamic content to load and requests to fire
            await asyncio.sleep(20) # Increased sleep time
        except Exception as e:
            print(f"Navigation failed: {e}")
        finally:
            await browser.close()
    return results

async def handle_request(request, results):
    if request.resource_type == "xhr" or request.resource_type == "fetch":
        # Capture all XHR/Fetch requests for analysis
        is_relevant = True
        
        if is_relevant:
            data = {
                "url": request.url,
                "method": request.method,
                "post_data": None
            }
            if request.method == "POST":
                try:
                    post_data_str = request.post_data
                    if post_data_str:
                        try:
                            # Attempt to parse as JSON, otherwise keep as string
                            data["post_data"] = json.loads(post_data_str)
                        except json.JSONDecodeError:
                            data["post_data"] = post_data_str
                except Exception as e:
                    print(f"Error getting POST data for {request.url}: {e}")
            results.append(data)

if __name__ == "__main__":
    target_url = "https://p2p.binance.com/"
    captured_requests = asyncio.run(analyze_binance_p2p_requests(target_url))

    print("\n--- Captured Relevant XHR/Fetch Requests ---")
    if captured_requests:
        for i, req in enumerate(captured_requests):
            print(f"Request {i+1}:")
            print(f"  URL: {req['url']}")
            print(f"  Method: {req['method']}")
            if req['post_data']:
                print(f"  Payload: {json.dumps(req['post_data'], indent=2)}")
            print("-" * 30)
    else:
        print("No relevant XHR/Fetch requests found based on filtering criteria.")