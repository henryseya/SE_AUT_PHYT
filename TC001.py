import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#abro el navegador
driver = webdriver.Chrome()

#maximiza la pantalla
driver.maximize_window()

#abre el site requerido
driver.get("https://www.saucedemo.com/")
time.sleep(1)
#Seleccionar los cuadros de texto y boton Login
#txt_usuario = driver.find_element(By.CSS_SELECTOR,'[data-test="username"]')
txt_usuario = driver.find_element(By.ID,'user-name')
txt_clave = driver.find_element(By.CSS_SELECTOR,'[data-test="password"]')
btn_login= driver.find_element(By.CSS_SELECTOR,'[data-test="login-button"]')

# Incorporo los datos e ingreso en la ecommerce
txt_usuario.send_keys('standard_user')
txt_clave.send_keys('secret_sauce')
btn_login.click()

####### Aserción del encabezado
lbl_encabezado = driver.find_element(By.CSS_SELECTOR,'#header_container > div.primary_header > div.header_label > div')
assert lbl_encabezado.text == 'Swag Labs',"Falló la aserción del encabezado"
assert driver.title == 'Swag Labs',"Falló la aserción del Título de la pestaña"

#assertEqual

########## Selección del producto a adquirir
btn_producto1 = driver.find_element(By.ID,'add-to-cart-sauce-labs-backpack')
btn_carrito = driver.find_element(By.CSS_SELECTOR,'#shopping_cart_container > a')
btn_producto1.click()
time.sleep(2)
btn_carrito.click()
time.sleep(2)

############# Abrir el menú
btn_menu = driver.find_element(By.ID,'react-burger-menu-btn')
btn_menu.click()

time.sleep(4)

btn_logout = driver.find_element(By.ID,'logout_sidebar_link')
btn_logout.click()






# cierra el navegador
time.sleep(4)
driver.quit()  

