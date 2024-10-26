#--------------------Librerías
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdrive.common.by import By
from selenium.webdriver.common.keys import Keys

#-----------------------Habilitar el explorador a usar
driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
#driver = webdriver.Safari()
#-----------------------ejecuciones en el explorador
driver.maximize_window()
driver.get('https://demoqa.com/text-box')
time.sleep(1)
#-----------------------------------------------inputs encontrar y llenar
#driver.find_element(By.ID,'userName').send_keys('Henry Herrera')
txt_username = driver.find_element(By.ID,'userName')
txt_username.send_keys('Henry Herrera')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
txt_email = driver.find_element(By.ID,'userEmail')
txt_email.send_keys('henry.herrera@insti.com')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
txt_address = driver.find_element(By.ID,'currentAddress')
txt_address.send_keys('Maracay')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
txt_perm_addres = driver.find_element(By.ID,'permanentAddress')
txt_perm_addres.send_keys('Montaña Fresca')#+Keys.TAB
time.sleep(1)
txt_perm_addres.send_keys(Keys.TAB)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(1)

btn_submit = driver.find_element(By.ID,'submit').click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)

#btn_submit.click()

#----------------------Aserción clase
#msg_email = driver.find_element(By.ID,'email')

#if('gomez@hotmail.com' in msg_email.text ):
    #print('El test se ejecutó correctamente')

#else:
    #print('NO EXISTE ESE EMAIL EN LA RESPUESTA')

#----------Aserción Henry
txt_res_name = driver.find_element(By.ID,'name')
txt_res_email = driver.find_element(By.ID,'email')
time.sleep(1)
txt_res_address = driver.find_element(By.CSS_SELECTOR, ".border > #currentAddress")
txt_res_perm_address = driver.find_element(By.CSS_SELECTOR,'.border > #permanentAddress')


if('Henry Herrera' in txt_res_name.text and 'henry.herrera@insti.com' in txt_res_email.text and 'Maracay' in txt_res_address.text and 'Montaña Fresca' in txt_res_perm_address.text):
    print ('CORRECTO')
    
else:
    print ('IMCORRECTO')



time.sleep(1)


#time.sleep(5)

#-----Cerrando explorador
driver.close()