from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)


try:
    index = 1

    for i in range(1, 5):
        url = f"https://quotes.toscrape.com/js/page/{6}/"
        driver.get(url)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "quote"))
        )
        quote_element = driver.find_elements(By.CSS_SELECTOR, ".quote .text")
        author_element = driver.find_elements(By.CSS_SELECTOR, ".quote .author")

        for i, (quote_el,author_el) in enumerate(zip(quote_element,author_element), start=1):
            quote = quote_el.get_attribute("textContent").strip()
            author = author_el.get_attribute("textContent").strip()
            print(f" {index}.  {author}... {quote}\n")
            index += 1
        

finally:
    driver.quit()
