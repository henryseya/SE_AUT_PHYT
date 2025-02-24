import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from includes.funciones import espera,escribir,mi_click,nuevo_driver,navegar,maximiza


# abro el navegador
driver = nuevo_driver('Chrome')
# maximiza la pantalla
maximiza()
# abre el site requerido
navegar()
espera('WAIT_CORTO')

body = driver.find_element(By.TAG_NAME, 'body')
str_nombre = driver.find_element(By.ID, 'firstName')
str_apellido = driver.find_element(By.ID, 'lastName')
str_nombre_usuario = driver.find_element(By.ID, 'username')
str_email = driver.find_element(By.ID, 'email')
str_direccion1 = driver.find_element(By.ID, 'address')
str_direccion2 = driver.find_element(By.ID, 'address2')
# Select de Pais
# El indice empieza en 1
cbo_pais_option = "2" # lo defino como string para contatenarlo al llamar al selector
cbo_pais = driver.find_element(By.CSS_SELECTOR, '#country > option:nth-child('+ cbo_pais_option +')')

# Select de la provincia
cbo_provincia_option = "3"
cbo_provincia = driver.find_element(By.CSS_SELECTOR, '#state > option:nth-child('+ cbo_provincia_option +')')

str_cod_postal = driver.find_element(By.ID, 'zip')
chk_dir_envio = driver.find_element(By.ID, 'same-address')
chk_guarda_info = driver.find_element(By.ID, 'save-info')
str_nombre_tarjeta = driver.find_element(By.ID, 'cc-name')
str_numero_tarjeta = driver.find_element(By.ID, 'cc-number')
str_fecha_expiracion = driver.find_element(By.ID, 'cc-expiration')
int_cvv = driver.find_element(By.ID, 'cc-cvv')
btn_continuar = driver.find_element(By.CSS_SELECTOR, 'body > div > main > div.row.g-5 > div.col-md-7.col-lg-8 > form > button')



escribir(str_nombre, "Marcelito")
escribir(str_apellido, "Kaos")
escribir(str_nombre_usuario, "ZombieEater")
escribir(str_email, "kaosinc@gmail.com")
escribir(str_direccion1, "Av. del Libertador 666")
#escribir(cbo_pais, "Bahia Blanca")
cbo_pais.click()
cbo_provincia.click()
escribir(str_cod_postal, "1702")

body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)

chk_dir_envio.click()
chk_guarda_info.click()

int_ccv=''
escribir(str_nombre_tarjeta, 'Mongo Aurelio')
escribir(str_numero_tarjeta, '5411 1234 5678 9100')
escribir(str_fecha_expiracion,'12/29')
escribir(int_ccv,'432') 

btn_continuar.click()


espera('WAIT_LARGO')

# Proceso página de resultados
btn_resultado = driver.find_element(By.CSS_SELECTOR,  'body > form > button')

#print (btn_resultado.text)

assert btn_resultado.text == "El pago fue procesado correcxtamente!", "Hizo PUF!"

if btn_resultado.text == "El pago fue procesado correctaxmente!":
    print("Todo ok")
else:
    print("Houston, we've a problem")

espera('WAIT_MEDIO')