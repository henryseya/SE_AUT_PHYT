#----------------Llamando librerías
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


#---------------Llamando explorador a utilizar
driver = webdriver.Chrome()
#drive = webdriver.Firefox()
#drive = webdriver.Edge()
#drive = webdriver.Safari()

#---------------Site for test
driver.get("https://www.saucedemo.com/")
#Maimizar la Ventana.
driver.maximize_window()
time.sleep(2)


#---------------TC001 Login
#Encontrando elementos para el Login - Declarando e igualando variables - Enviamos datos de ingreso
#txt_usuario = driver.find_element(By.ID,'user-name')
txt_usuario = driver.find_element(By.CSS_SELECTOR,'[data-test="username"]').send_keys('standard_user')
txt_clave = driver.find_element(By.CSS_SELECTOR,'[data-test="password"]').send_keys('secret_sauce')
btn_login = driver.find_element(By.CSS_SELECTOR,'[data-test="login-button"]').click()
#Time Usado para visualiar
time.sleep(2)

#---------------Aserción del Login
#lbl_encabezado = driver.find_element(By.CSS_SELECTOR,'#header_container > div.primary_header > div.header_label > div')
assert driver.title == 'Swag Labs',"Falla el proceso de Login"


#---------------Encontrando elementos para agregar al Carrito de Compras - Declarando e igualando variables - Enviamos el click
btn_product1 = driver.find_element(By.CSS_SELECTOR,'[data-test="add-to-cart-sauce-labs-backpack"]').click()
#Time para visualiar
time.sleep(1)
btn_product2 = driver.find_element(By.CSS_SELECTOR,'[data-test="add-to-cart-sauce-labs-bike-light"]').click()
#time para visualizar
time.sleep(1)
btn_product3 = driver. find_element(By.CSS_SELECTOR,'[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
#time para visualizar
time.sleep(1)
btn_product4 = driver.find_element(By.CSS_SELECTOR,'[data-test="add-to-cart-sauce-labs-fleece-jacket"]').click()
#time para visualiazr
time.sleep(1)
#hacer scroll para los otros productos
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#time para visualiazr el scroll
time.sleep(1)
btm_product5 = driver.find_element(By.CSS_SELECTOR,'[data-test="add-to-cart-sauce-labs-onesie"]').click()
#time para visualiazr
time.sleep(1)
btn_prodduct6 = driver.find_element(By.CSS_SELECTOR,'[data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()
#time para visualiar
time.sleep(1)
#Seleccionados productos ir a Resumen de Carrito de compras.
#hacer scroll para subir en la pantalla - Necesario para presionar el boton Carrito de compras
driver.execute_script("window.scrollTo(0, 0);")
#Time visualiazr el scroll hacia arriba.
time.sleep(1)
btn_car = driver.find_element(By.CSS_SELECTOR,'.shopping_cart_link').click()
#time sleep para visualizar
time.sleep(1)

#---------------Pantalla Resumen de compras-esto es para cuando siga avanzando iba a ser un asser pero no se como comparar valores de una pantalla para la otra y así poder hacer un asser efectivo
#txt_res_produc1 = driver.find_element('[data-test="item-4-title-link"]')#Sauce Labs Backpack
#txt_res_product2 = driver.find_element('[data-test="item-0-title-link"]')#Sauce Labs Bike Light

#---------------Proceso Checkout
#hacer scroll para presionar el botón de checkout
#time para visualiar
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
btn_checkput = driver.find_element(By.CSS_SELECTOR,'[data-test="checkout"]').click()

#---------------Proceso Checkout Step 1 - Ingresar Datos.
txt_firstname = driver.find_element(By.CSS_SELECTOR,'[data-test="firstName"]').send_keys("TESTNAME")
#time para visualizar
time.sleep(1)
txt_lastname = driver.find_element(By.CSS_SELECTOR,'[data-test="lastName"]').send_keys("TESTLASTNAME")
#time para visualiar
time.sleep(1)
txt_postalcode = driver.find_element(By.CSS_SELECTOR,'[data-test="postalCode" ]').send_keys("TESTPOSTALCODE")
#time para visualiar
time.sleep(1)
#hacer scroll para presionar el botón de continue
#time para visualiar
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
btn_continue = driver.find_element(By.CSS_SELECTOR,'[data-test="continue"]').click()
#time sleep para visualizar
time.sleep(1)



#---------------Proceso Logout
btn_menu = driver.find_element(By.CSS_SELECTOR,'#react-burger-menu-btn').click()
#time para visualiar
time.sleep(1)
btn_logout = driver.find_element(By.CSS_SELECTOR,'[data-test="logout-sidebar-link"]').click()
#time para visualiar
time.sleep(1)

#Cerrar navegador
time.sleep(1)
driver.quit()


