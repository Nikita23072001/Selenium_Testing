from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import creds
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.facebook.com/")

title = driver.title
assert title == "Facebook – zaloguj się lub zarejestruj"

# time.sleep(10)
driver.find_element(By.NAME, "email").clear()
driver.find_element(By.NAME, "email").send_keys(creds.creds()[0])
time.sleep(10)
driver.find_element(By.NAME, "pass").clear()
driver.find_element(By.NAME, "pass").send_keys(creds.creds()[1])
time.sleep(1)
# aria_label_value = "Zezwól na wszystkie pliki cookie"
# element = driver.find_element(By.XPATH, f"//*[@aria-label='{aria_label_value}']")
# element.click()

try:
    # Znajdowanie i klikanie przycisku akceptującego ciasteczka na podstawie aria-label
    wait = WebDriverWait(driver, 10)
    accept_cookies_button = driver.find_element(By.XPATH, '//div[@aria-label="Zezwól na wszystkie pliki cookie" and @role="button"]')
    print("Tag name:", accept_cookies_button.tag_name)
    print("Text:", accept_cookies_button.text)
    print("Aria-label:", accept_cookies_button.get_attribute("aria-label"))
    print("Other attributes:")
    for attribute in accept_cookies_button.get_property("attributes"):
        print(f" - {attribute['name']} = {attribute['value']}")
    driver.execute_script("arguments[0].removeAttribute('aria-disabled'); arguments[0].click();", accept_cookies_button)
    print("Accepted cookies")
except Exception as e:
    print("Cookies button not found:", e)

driver.find_element(By.NAME, "login").click()


# driver.find_element(By.NAME, "login").click()