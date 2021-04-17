from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import time

# settings

USERNAME = "<your username>"
PASSWORD = "<your password>"
POST_URL = "<https://post_url.com>"
COMMENT_TEXT = "<comment text>"
DRIVER_PATH = '<driver path>'

# init 

driver = webdriver.Chrome(DRIVER_PATH)

driver.get("http://www.instagram.com")

try:
    from local_settings import * # for development
except: 
    pass

# login page

username_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'username')))
password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'password')))

username_field.clear()
username_field.send_keys(USERNAME)

password_field.clear()
password_field.send_keys(PASSWORD)

login_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
login_button.click()

# save info page

save_info_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Salvar informações"]')))
save_info_button.click()

# goal page

driver.get("https://www.google.com")
driver.get(POST_URL) 

coment_textarea = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder='Adicione um comentário...']")))

while(True):
    try:    
        coment_textarea.click()
        coment_textarea.send_keys(COMMENT_TEXT)
    except:
        coment_textarea = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder='Adicione um comentário...']")))
        coment_textarea.click()
        coment_textarea.send_keys(COMMENT_TEXT)

    coment_textarea.send_keys(Keys.ENTER)
    time.sleep(10)