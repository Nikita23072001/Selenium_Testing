from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import creds
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.facebook.com/")

title = driver.title
assert title == "Facebook – zaloguj się lub zarejestruj"

driver.find_element(By.NAME, "email").clear()
driver.find_element(By.NAME, "email").send_keys(creds.creds()[0])
driver.find_element(By.NAME, "pass").clear()
driver.find_element(By.NAME, "pass").send_keys(creds.creds()[1])
print(driver.find_element(By.NAME, "login"))