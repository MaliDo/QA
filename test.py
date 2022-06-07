from webbrowser import get
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
import time
import json

with open('data.json') as d:
   data = json.load(d)

for i in data['input']:
    driver = webdriver.Chrome('/Applications/chromedriver')
    driver.get('https://redtigerav.github.io/qa-webinar/')

    full_name = driver.find_element(By.ID, 'mat-input-0')
    full_name.send_keys(i['full_name_data'])

    get_pic = driver.find_element(By.XPATH, '//input[@type=\"file\"]').send_keys(i['get_pic_path'])

    birth_city = driver.find_element(By.ID, 'mat-input-1')
    birth_city.send_keys(i['birth_city_data'])

    birthday = driver.find_element(By.ID, 'mat-input-2')
    birthday.send_keys(i['birthday_data'])

    zip_code = driver.find_element(By.ID, 'mat-input-3')
    zip_code.send_keys(i['zip_code_data'])

    city = driver.find_element(By.ID, 'mat-input-4')
    city.send_keys(i['city_data'])

    street = driver.find_element(By.ID, 'mat-input-5')
    street.send_keys(i['street_data'])

    address = driver.find_element(By.ID, 'mat-input-6')
    address.send_keys(i['address_data'])

    recipient_bank = driver.find_element(By.ID, 'mat-input-7')
    recipient_bank.send_keys(i['recipient_bank_data'])

    bank_id = driver.find_element(By.ID, 'mat-input-8')
    bank_id.send_keys(i['bank_id_data'])

    corr_acct = driver.find_element(By.ID, 'mat-input-9')
    corr_acct.send_keys(i['corr_acct_data'])

    tin = driver.find_element(By.ID, 'mat-input-10')
    tin.send_keys(i['tin_data'])

    reg_reason = driver.find_element(By.ID, 'mat-input-11')
    reg_reason.send_keys(i['reg_reason_data'])

    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    time.sleep(5)
    driver.close()