from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from def_fun.generales import espera,escribir,mi_click,nuevo_driver,navegar,maximiza,selecciona
from def_fun.bd import busca_precio

'''
Cambios introducidos:
- Le comenté el maximize para que no moleste.
- En todos los lugares donde se podía, usé como selectores los atributos "data-test".
- Declare constantes para los tiempos de espera, que es una buena práctica para tocar en un lado, y cambia en todos los lugares el valor
- Respecto al XPATH, no funciona cuando el selector incluye el TEXT, pero ya tomándolo sin el TEXT, se lo puede trabajar tal como hicimos en clase, dejo las lineas comentadas, igual uso el data-test, ya que esta disponible y el resto es idéntico.
- En la consola deja los valores tomados de la página.
'''
# abro el navegador
#driver = nuevo_driver('Chrome',pagina=nuevo_driver)
driver = nuevo_driver('Chrome')
# maximiza la pantalla
maximiza()
# abre el site requerido
navegar()


espera('WAIT_CORTO')
# Seleccionar los cuadros de texto y boton Login
# txt_usuario = selecciona(By.CSS_SELECTOR,'[data-test="username"]')
txt_usuario = selecciona(By.CSS_SELECTOR, '[data-test="username"]')
txt_clave = selecciona(By.CSS_SELECTOR, '[data-test="password"]')
btn_login = selecciona(By.CSS_SELECTOR, '[data-test="login-button"]')

# Incorporo los datos e ingreso en la ecommerce

escribir(txt_usuario,'standard_user')

txt_clave.send_keys('secret_sauce')

mi_click(btn_login)

espera('WAIT_CORTO')

# Aserción del encabezado
lbl_encabezado = selecciona(
    # no tiene data-test  - Encabezado de la página -
    By.CSS_SELECTOR, '#header_container > div.primary_header > div.header_label > div')

assert lbl_encabezado.text == 'Swag Labs', "Falló la aserción del encabezado"
assert driver.title == 'Swag Labs', "Falló la aserción del Título de la pestaña"

# Selección del producto a adquirir - Botón de agregar al carrito del 1° producto
btn_producto1 = selecciona(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
btn_producto1.click()
espera('WAIT_CORTO')

# btn_producto1 = selecciona(By.ID, 'add-to-cart-sauce-labs-backpack')
# botón del carrito de compras
btn_carrito = selecciona(By.CSS_SELECTOR, '#shopping_cart_container > a')  # no tiene data-test
btn_carrito.click()
espera('WAIT_CORTO')

# Hago click en el botón del checkout 
btn_checkout = selecciona(By.CSS_SELECTOR, '#checkout')
btn_checkout.click()

# Ingreso los datos personales
txt_nombre = selecciona(By.CSS_SELECTOR, '[data-test="firstName"]')
txt_apellido = selecciona(By.CSS_SELECTOR, '[data-test="lastName"]')
txt_zip = selecciona(By.CSS_SELECTOR, '[data-test="postalCode"]')
btn_continue = selecciona(By.CSS_SELECTOR, '[data-test="continue"]')

# Envío de datos para el checkout
txt_nombre.send_keys('Nombre Del Comprador')
txt_apellido.send_keys('Apellido Del Comprador')
txt_zip.send_keys('1414')
btn_continue.click()

# Click en el botón para ir a "pagar"

# Aserciones de los importe y de el/los productos que están en el carrito
espera('WAIT_MEDIO')

# Con este XPATH anda, pero no toma el pedacito de texto.
# lbl_precio_producto = selecciona(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]')
# //*[@id="checkout_summary_container"]/div/div[2]/div[6]/text()[1]  <---  ese /text()[1]  es lo que no toma.

lbl_precio_producto = selecciona(By.CSS_SELECTOR, '[data-test="subtotal-label"]')

# print(lbl_precio_producto.text)
# Obtener el precio del producto sin el mensaje Item total: $
dbl_precio_producto = float(lbl_precio_producto.text.rsplit('$', 1)[1])

# Busca precio en la base de datos
# 
precio_a_chequear = float(busca_precio('Sauce Labs Backpack'))
print("Precio según BD" + str(precio_a_chequear))
# asert del precio
assert dbl_precio_producto == precio_a_chequear, "El precio de la base es distinto"

# 2da opcion para convertir el $29.99 string en 29.99 numerico flotante
#dbl_precio_producto = lbl_precio_producto.text  # $29.99  --> 29.99 --> convertirlo a numero
#dbl_precio_producto = dbl_precio_producto.replace('Item total: $',"")  # ahora el valor es 29.99 / eliminé el $
#dbl_precio_producto = float(dbl_precio_producto) # convierto el valor que ahora es un alfanumerico (string) a numero flotante

print(f'{"Precio según página:"} {dbl_precio_producto}')
dbl_tax_producto = dbl_precio_producto * .08
print(f'{"Impuesto calculado:"} {dbl_tax_producto}')
# sumo el tax con el precio del producto y redondeo a 2 decimales
dbl_precio_total = round(dbl_precio_producto + dbl_tax_producto, 2)
print(f'{"Precio total calculado:"} {dbl_precio_total}')

#obtengo el valor del total a pagar
dbl_total_a_pagar = selecciona(By.CSS_SELECTOR, '[data-test="total-label"]')
# convertir el total $... string en ... numerico flotante
dbl_total_a_pagar = dbl_total_a_pagar.text  # $29.99  --> 29.99 --> convertirlo a numero
dbl_total_a_pagar = dbl_total_a_pagar.replace('Total: $',"")  # ahora el valor es 29.99 / eliminé el $
dbl_total_a_pagar= round(float(dbl_total_a_pagar),2) # convierto el valor que ahora es un alfanumerico (string) a numero flotante

assert dbl_total_a_pagar == dbl_precio_total, "Falló la aserción del total a pagar"

# Abrir el menú
espera('WAIT_CORTO')

btn_finish = selecciona(By.CSS_SELECTOR, '[data-test="finish"]')
btn_finish.click()

# Abrir el menú
espera('WAIT_CORTO')

btn_menu = selecciona(By.ID, 'react-burger-menu-btn')
btn_menu.click()

espera('WAIT_CORTO')

btn_logout = selecciona(By.ID, 'logout_sidebar_link')
btn_logout.click()
espera('WAIT_CORTO')
driver.quit()  # cierra el navegador