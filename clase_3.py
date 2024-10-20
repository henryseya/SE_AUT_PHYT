import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Abro el navegador
driver = webdriver.Chrome()
# Defino que se maximiza
driver.maximize_window()
# Llamado a la web a automatizar
driver.get('https://institutoweb.com.ar/test/login.html')


with open('mis_datos/datos.csv','r') as csv_archivo:  # indicar el archivo de datos y su nombre en el test
   csv_reader = csv.reader(csv_archivo)     # leo el contenido del archivo globalmente
   next(csv_reader)
   for renglon in csv_reader:               # leo un renglon del contenido global
        var_usuario,var_clave,var_email = renglon # generar 3 variables en base al renglón


        # carga de los elementos de la 1° página en base a sus selectores
        txt_usuario = driver.find_element(By.ID,'tuusuario')
        txt_clave = driver.find_element(By.ID,'tuclave')
        txt_email = driver.find_element(By.ID,'tumail')
        btn_ingresar = driver.find_element(By.CSS_SELECTOR,'body > form > button:nth-child(8)')


        # Acciones de la 1° Página
        txt_usuario.clear()
        txt_usuario.send_keys(var_usuario)
        txt_clave.send_keys(var_clave)
        txt_email.send_keys(var_email)
        time.sleep(5)
        btn_ingresar.click()


        # carga de los elementos de la 2° página en base a sus selectores
        lnk_cerrar = driver.find_element(By.ID,'volver')
        h3_titulo = driver.find_element(By.CSS_SELECTOR,'body > h3') # toma el header h3


        # Acciones de la 2° Página
        if h3_titulo.text == 'Acceso correcto!':
            print('Salió todo perfecto!')
        else:
            print('Un desastre!')


        assert h3_titulo.text == 'Acceso correcto!','Falló el Test, el h3 no cumple el texto esperado'
        assert driver.title == 'Acceso al sistema','Falló el Test, el title no cumple el texto esperado'


        time.sleep(4)
        lnk_cerrar.click() # Click en link 'cerrar sesión'
        time.sleep(4)