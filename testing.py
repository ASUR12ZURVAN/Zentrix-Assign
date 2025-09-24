from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import string
import time


def random_email():
    name = ''.join(random.choices(string.ascii_lowercase, k=7))
    domain = ''.join(random.choices(string.ascii_lowercase, k=5))
    return f"{name}@{domain}.com"


def random_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))


driver = webdriver.Chrome()  
driver.maximize_window()

driver.get("http://127.0.0.1:8000/")  

time.sleep(2)  


email_input = driver.find_element(By.ID, "email")
password_input = driver.find_element(By.ID, "password")


email_input.send_keys(random_email())
password_input.send_keys(random_password())


submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit_button.click()


time.sleep(5)


driver.quit()
