import json
import os
from datetime import datetime

from bs4 import BeautifulSoup
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

# The URL of the Bybit P2P page to scrape
url = os.getenv("BYBIT_P2P_URL")

all_offers = []

try:
    with sync_playwright() as p:
        browser = p.firefox.launch()
        page = browser.new_page(ignore_https_errors=True)
        page.goto(url, wait_until='domcontentloaded', timeout=90000) # Increased timeout
        page.wait_for_load_state('networkidle', timeout=60000) # Wait for network to be idle

        # Take a screenshot for debugging
        page.screenshot(path="bybit_page.png")

        # Wait for the content to load. Wait for at least one offer listing to be present.
        page.wait_for_selector('div.trade-item', timeout=60000)

        # Get the rendered HTML content
        html_content = page.content()
        browser.close()

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all individual offer listings
    offer_listings = soup.find_all('div', class_='trade-item')

    if not offer_listings:
        print("No offer listings found. Check HTML structure or selectors.")

    for offer in offer_listings:
        advertiser = offer.find('span', class_='trade-item-nickName')
        price = offer.find('div', class_='trade-item-price')
        quantities = offer.find_all('div', class_='trade-item-quantity')
        payment_methods_elements = offer.find('div', class_='trade-item-payments')

        advertiser_name = advertiser.text.strip() if advertiser else "N/A"
        price_value = price.text.strip() if price else "N/A"

        available_amount = "N/A"
        transaction_limits = "N/A"

        for q in quantities:
            if "Disponible" in q.text:
                available_amount = (
                    q.find('span', class_='trade-item-quantity-span').text.strip()
                    if q.find('span', class_='trade-item-quantity-span')
                    else "N/A"
                )
            elif "Límites de transacciones" in q.text:
                transaction_limits = (
                    q.find('span', class_='trade-item-quantity-span').text.strip()
                    if q.find('span', class_='trade-item-quantity-span')
                    else "N/A"
                )

        payment_methods = []
        if payment_methods_elements:
            for pm in payment_methods_elements.find_all('span', class_='trade-item-payments-item-span'):
                payment_methods.append(pm.text.strip())

        offer_details = {
            "advertiser": advertiser_name,
            "price": price_value,
            "available": available_amount,
            "limits": transaction_limits,
            "payment_methods": payment_methods
        }
        all_offers.append(offer_details)

    if not all_offers:
        print("No offers found after parsing. Check HTML structure or selectors.")
    else:
        print(f"Successfully parsed {len(all_offers)} offers.")

    # Save all the data to a JSON file
    if all_offers:
        # Create the json_files directory if it doesn't exist
        output_dir = os.path.join(os.path.dirname(__file__), 'json_files')
        os.makedirs(output_dir, exist_ok=True)

        # Generate timestamped filename
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"bybit_offers_{timestamp}.json"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(all_offers, f, ensure_ascii=False, indent=4)
        print(f"Data for {len(all_offers)} offers saved to {filepath}")
    else:
        print("No offers found.")


except Exception as e:
    print(f"An unexpected error occurred: {e}")
