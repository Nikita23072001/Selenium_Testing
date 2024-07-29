from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

title = driver.title
print(title)
assert title == "Facebook – zaloguj się lub zarejestruj"



# time.sleep(20)