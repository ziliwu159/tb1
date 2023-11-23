from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:9999/")

email = driver.find_element(By.XPATH, '//input[@name="email"]')
password = driver.find_element(By.XPATH, '//input[@name="password"]')
login_btn = driver.find_element(By.XPATH, '//button[@type="submit"]')

email.send_keys("admin@if.local")
time.sleep(3)
password.send_keys("rahasia123")
time.sleep(1)
login_btn.click()

time.sleep(3)

current_url = driver.current_url

if '/dashboard' in current_url:
  status = "Login Successful"
elif '/' in current_url:
  status = "Login Failed!"
else:
  status = "Failed! Unknown Error!"

waktu_skrg = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open('uji_login.txt', 'a') as file:
  if '<h1>Internal Server Error</h1>' in driver.page_source:
    file.write(f"Fitur Login - diuji pada : {waktu_skrg} - Status : Error - Internal Server Error\n")
  else:
    file.write(f"Fitur Login - diuji pada : {waktu_skrg} - Status : {status}\n")

driver.quit()




