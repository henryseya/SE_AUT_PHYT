import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#caja_de_busqueda.send_keys(Keys.ENTER)
#---------------------------------------------------
explorador = webdriver.Chrome()
#explorador = webdriver.Firefox()
#explorador = webdriver.Edge()
#miweb.set_window_size(1200, 600)
explorador.maximize_window()
explorador.get("https://app.swevenbpm.com/")
#---------------------------------------------------------------
usuario = explorador.find_element(By.ID,"email")
usuario.send_keys("henry.herrera+vbqa@technoglobalinc.com")
#---------------------------------------------------------------
contrasena = explorador.find_element(By.ID,"password")
contrasena.send_keys("Yase2241$")
#---------------------------------------------------------------
Pboton= explorador.find_element(By.CSS_SELECTOR, ".accounts--btn").click()
#---------------------------------------------------------------
time.sleep(10)
explorador.quit()