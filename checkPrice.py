from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# 1. Setup Options
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")

# 2. Initialize Driver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

items = [
    "molt_augmented",
    "molt_efficiency",
    "melee_influence",
    "magus_lockdown",
    "energy_conversion",
    "arcane_energize",
    "health_conversion"
]

try:
    for item in items:
        url = f"https://warframe.market/items/{item}?type=buy"
        driver.get(url)
        print(f"\nITEM: {item}")

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".order-row__price--hn3HU"))
        )
        
        price_element = driver.find_elements(By.CSS_SELECTOR, ".order-row__price--hn3HU b")
        
        for i, price_el in enumerate(price_element[:3], start=1):
            price = price_el.get_attribute("textContent").strip()

            if price:
                print(f"  {i}. {price} platinum")

finally:    
    driver.quit()   