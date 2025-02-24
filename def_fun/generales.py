import time
from selenium import webdriver

driver = None
############################## Funciones del driver
#def nuevo_driver(navegador,pagina):
def nuevo_driver(navegador):
    global driver
    if navegador=='Chrome':
        driver = webdriver.Chrome()
        return driver
    elif navegador=='Firefox':
        driver = webdriver.Firefox()
        return driver

def maximiza():
    global driver
    driver.maximize_window()

def navegar():
    global driver
    driver.get("https://www.saucedemo.com/")
###################################### Funciones de Elementos
#reemplaza al click
def mi_click(elemento):
    elemento.click()

#reemplaza el send.keys
def escribir(selector,dato_a_escribir):
    selector.send_keys(dato_a_escribir)
    #time.sleep(1)

def selecciona(by,selector):
    global driver
    return driver.find_element(by, selector) 

###################################### Funciones de espera
#reemplaza al sleep de python
def espera(tipo_espera):
    if tipo_espera == 'WAIT_CORTO':
        time.sleep(1)
    elif tipo_espera == 'WAIT_MEDIO':
        time.sleep(2)
    elif tipo_espera == 'WAIT_LARGO':
        time.sleep(3)