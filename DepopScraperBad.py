from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time
import sys
import io
from selenium.webdriver.chrome.options import Options

# Set up Chrome options to run in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")  # Optional: Disable GPU acceleration
chrome_options.add_argument("--window-size=1920x1080")  # Set the window size

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.depop.com/")

driver.implicitly_wait(5)

def full_search(driver):
    jeans = []
    for i in range (0,16):
        try:
            print("***********************************")
            jeans_clickable = driver.find_elements(by=By.CLASS_NAME, value="jvVDKQ")
            print(len(jeans_clickable))
            # WebDriverWait(driver, 10).until(EC.element_to_be_clickable(jeans_clickable[i]))
            jeans_clickable[i].click()
            driver.implicitly_wait(5)
            description = driver.find_element(by=By.CLASS_NAME, value="styles__TextContainer-sc-d367c36f-1")
            description_text = description.text
            jeans.append(description_text)
            print(description_text)
            driver.back()
            time.sleep(0.7)
        except ElementClickInterceptedException:
            print(f"Element {i} could not be clicked, skipping.")
            driver.refresh()
            time.sleep(0.35)
            continue
    return jeans


buttons = driver.find_elements(by=By.CLASS_NAME, value="sc-hjcAab")
buttons[1].click()

driver.implicitly_wait(5)
text_box = driver.find_element(by=By.ID, value="searchBar__input")
text_box.send_keys("baggy jean thigh leg opening")
text_box.send_keys(Keys.RETURN)
time.sleep(2)
print(full_search(driver=driver))
print("***********************************")
driver.quit()








