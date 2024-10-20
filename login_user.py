import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#caja_de_busqueda.send_keys(Keys.ENTER)
#---------------------------------------------------
driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
#miweb.set_window_size(1200, 600)
driver.maximize_window()
driver.get("https://app.swevenbpm.com/")
#---------------------------------------------------------------
txt_usuario = driver.find_element(By.ID,"email")
txt_usuario.clear
txt_usuario.send_keys("henry.herrera+vbqa@technoglobalinc.com")
#---------------------------------------------------------------
txt_contrasena = driver.find_element(By.ID,"password")
txt_contrasena.clear
txt_contrasena.send_keys("Yase2241$")
#---------------------------------------------------------------
btn_Pboton= driver.find_element(By.CSS_SELECTOR, ".accounts--btn").click()
#---------------------------------------------------------------
assert driver.title == 'SWEVEN-Portal','ACCESO FALLÓ'

if driver.title == 'SWEVEN-Portal':
    print("ACCESO CORRECTO")
else:
    Print ("FALLÓ ACCESO")
    
time.sleep(4)
driver.quit()