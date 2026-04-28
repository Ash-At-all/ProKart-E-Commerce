from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import json
import time
import re

def clean_price(text):
    match = re.search(r'₹[\d,]+', text)
    return match.group() if match else "N/A"

def clean_rating(text):
    matches = re.findall(r'\d+\.\d+', text)
    for match in matches:
        val = float(match)
        if 0 < val <= 5:
            return str(val)
    return "N/A"

def clean_name(text):
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if len(line) > 10 and 'Compare' not in line and 'Bank' not in line and '₹' not in line and line not in ['Login', 'Cart', 'More']:
            return line
    return "N/A"

def scrape_flipkart(search_query):
    options = webdriver.ChromeOptions()
    # Headless bilkul band
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    url = f"https://www.flipkart.com/search?q={search_query}"
    driver.get(url)
    time.sleep(6)
    
    # Login popup close karo
    try:
        close = driver.find_element(By.CSS_SELECTOR, "button._2KpZ6l._2doB4z")
        close.click()
        time.sleep(1)
    except:
        pass
    
    # Slowly scroll karo
    for i in range(1, 8):
        driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight * {i/7});")
        time.sleep(1.5)
    
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)

    products = []
    
    # Sabhi classes try karo
    cards = driver.find_elements(By.CLASS_NAME, "k7wcnx")
    print(f"k7wcnx: {len(cards)}")
    
    if not cards:
        cards = driver.find_elements(By.CSS_SELECTOR, "div.yrDfl4.jODOEE")
        print(f"yrDfl4.jODOEE: {len(cards)}")
    
    if not cards:
        cards = driver.find_elements(By.CLASS_NAME, "yrDfl4")
        print(f"yrDfl4: {len(cards)}")

    if not cards:
        cards = driver.find_elements(By.CLASS_NAME, "GnxRXv")
        print(f"GnxRXv: {len(cards)}")
    
    print(f"Total Cards found: {len(cards)}")
    
    for card in cards:
        try:
            full_text = card.text.strip()
            print("CARD:", full_text[:150])
            
            # Skip navbar elements
            if full_text in ['Login', 'Cart', 'More', ''] or len(full_text) < 10:
                continue

            # Name
            try:
                name_el = card.find_element(By.CSS_SELECTOR, "a[title]")
                name = name_el.get_attribute("title")
            except:
                try:
                    name_el = card.find_element(By.TAG_NAME, "a")
                    name = name_el.text.strip().split('\n')[0]
                except:
                    name = clean_name(full_text)

            if not name or len(name) < 5 or name == "N/A":
                continue

            # Price
            try:
                price_el = card.find_element(By.CSS_SELECTOR, "[class*='Nx9bqj']")
                price = price_el.text.strip()
            except:
                price = clean_price(full_text)

            # Rating
            try:
                rating_el = card.find_element(By.CSS_SELECTOR, "[class*='XQDdHH']")
                rating = rating_el.text.strip()
            except:
                rating = clean_rating(full_text)

            # Image
            try:
                image = card.find_element(By.TAG_NAME, "img").get_attribute("src")
            except:
                image = "N/A"

            products.append({
                "name": name,
                "price": price,
                "rating": rating,
                "image": image
            })
            print(f"✓ Added: {name[:50]}")

        except:
            continue
    
    driver.quit()
    return products

# Menu
print("=" * 40)
print("  PROKART - Flipkart Scraper")
print("=" * 40)
print("Available Categories:")
print("  1. phones")
print("  2. laptops")
print("  3. audio")
print("  4. accessories")
print("=" * 40)

category = input("Category enter karo (phones/laptops/audio/accessories): ").strip().lower()
product_name = input("Product name enter karo (e.g. boat earphone, gaming mouse): ").strip()

if category not in ["phones", "laptops", "audio", "accessories"]:
    print("❌ Invalid category! phones/laptops/audio/accessories mein se choose karo")
else:
    print(f"\n🔍 Scraping '{product_name}' for category '{category}'...")
    results = scrape_flipkart(product_name)

    for p in results:
        p["category"] = category
        if p["price"] != "N/A":
            try:
                p["price"] = int(str(p["price"]).replace("₹", "").replace(",", ""))
                p["original"] = p["price"]
            except:
                p["price"] = 0
                p["original"] = 0
        else:
            p["price"] = 0
            p["original"] = 0

        if p["rating"] != "N/A":
            try:
                p["rating"] = float(p["rating"])
            except:
                p["rating"] = 4.0
        else:
            p["rating"] = 4.0

        p["reviews"] = 0
        p["badge"] = ""

    print(f"\n✅ {len(results)} products found!")

    try:
        with open("flipkart_data.json", "r", encoding="utf-8") as f:
            existing = json.load(f)
    except:
        existing = []

    max_id = max([p.get("id", 0) for p in existing], default=100)
    for i, p in enumerate(results):
        p["id"] = max_id + i + 1

    existing.extend(results)

    with open("flipkart_data.json", "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)

    print(f"🎉 Total {len(existing)} products saved in flipkart_data.json!")