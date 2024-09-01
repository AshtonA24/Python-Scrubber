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
# chrome_options.add_argument("--headless")  # Run in headless mode
# chrome_options.add_argument("--disable-gpu")  # Optional: Disable GPU acceleration
chrome_options.add_argument("--window-size=1x1")  # Set the window size

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

def open_to_search_results(driver, search):
    driver.get("https://www.depop.com/")
    buttons = driver.find_elements(by=By.CLASS_NAME, value="sc-hjcAab")
    buttons[1].click()
    driver.implicitly_wait(10)
    text_box = driver.find_element(by=By.ID, value="searchBar__input")
    text_box.send_keys(search)
    text_box.send_keys(Keys.RETURN)
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)  # Wait for content to load


def get_post_urls(driver):
    urls = []
    print("***********************************")
    driver.implicitly_wait(5)
    post_element = driver.find_elements(by=By.CLASS_NAME, value="jvVDKQ")
    for element in post_element:
        url = element.get_attribute("href")
        urls.append(url)
    return urls


def process_results(driver, urls):
    descriptions = []
    for url in urls:
        driver.get(url)
        driver.implicitly_wait(5)
        description = driver.find_element(by=By.CLASS_NAME, value="styles__TextContainer-sc-d367c36f-1")
        description_text = description.text
        img_element = driver.find_element(by=By.CLASS_NAME, value='styles__StyledImg-sc-ae87dc0d-3')
        img = img_element.get_attribute('src')
        description_url_img_combo = [description_text, url, img]
        descriptions.append(description_url_img_combo)
    return descriptions


open_to_search_results(driver=driver, search='baggy jean thigh leg opening')
urls = get_post_urls(driver=driver)
print(process_results(driver=driver, urls=urls))
print("***********************************")
driver.quit()








