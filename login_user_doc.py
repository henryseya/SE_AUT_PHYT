#--------------------------Llmada de librerías
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#------------------------Abrir Navegador
driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
#driver = webdriver.Safari()

#------------------------Operaciones en Navegador
driver.maximize_window()

#------------------------Sitio para automatizar
driver.get('https://institutoweb.com.ar/test/login.html')

#----------------------Operaciones en Archivo CSV
#Con el archivo buscalo, lee el archivo y guardalo en csv_archivo
with open('mis_datos/datos.csv','r') as csv_archivo:
    csv_reader = csv.reader(csv_archivo)
    #Pasa por alto la primera fila del archivo
    next(csv_reader)
    #recorrido por el archivo csv_archivo
    for renglon in csv_reader:
        #el recorrido se guardan en las siguientes 3 varias
        var_usuario,var_clave,var_email = renglon

        #cargar elementos en el drive en cada input
        txt_usuario = driver.find_element(By.ID,'tuusuario')
        txt_clave = driver.find_element(By.ID,'tuclave')
        txt_email = driver.find_element(By.ID,'tumail')
        btn_ingresar = driver.find_element(By.CSS_SELECTOR,'body > form > button:nth-child(8)')

        #Enviando valores a cada input
        txt_usuario.clear()
        txt_usuario.send_keys(var_usuario)
        txt_clave.send_keys(var_clave)
        txt_email.send_keys(var_email)
        time.sleep(5)
        btn_ingresar.click()

        #despues de ingresar cada usuario - se debe volver  - para cargar los siguientes
        lnk_cerrar = driver.find_element(By.ID,'volver')
        #Elemento que sirve para validar que el ingreso fue correcto
        h3_titulo = driver.find_element(By.CSS_SELECTOR,'body > h3')

        #Las asersiones se toman con algun elemento despues de ingresa para validar el ingreso
        #if h3_titulo.text == 'Acceso correcto!':
            #print('Salió todo perfecto!')
        #else:
            #print('Un desastre!')
        #otra forma de buscar o validar aserciones
        #assert h3_titulo.text == 'Acceso correcto!','Falló el Test, el h3 no cumple el texto esperado'
        assert driver.title == 'Acceso al sistema','Falló el Test, el title no cumple el texto esperado'


        time.sleep(4)
        lnk_cerrar.click() # Click en link 'cerrar sesión'
        time.sleep(4)