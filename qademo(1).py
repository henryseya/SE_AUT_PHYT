import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://demoqa.com/text-box/')
time.sleep(1) # orden de python 
driver.find_element(By.ID,'userName').send_keys('Juan Gomez')

txt_email = driver.find_element(By.ID,'userEmail')
txt_email.send_keys('gomez@hotmail.com')


txt_adress = driver.find_element(By.ID,'currentAddress')
txt_adress.send_keys('San Juan 2020')

txt_perm_adress = driver.find_element(By.ID,'permanentAddress')
txt_perm_adress.send_keys('Rosario 5050'+Keys.TAB)

time.sleep(1) # orden de python 
btn_enviar = driver.find_element(By.ID,'submit')
btn_enviar.click()

msg_email = driver.find_element(By.ID,'email')

if('gomez@hotmail.com' in msg_email.text ):
    print('El test se ejecutó correctamente')

time.sleep(3) # orden de python 

driver.close()
