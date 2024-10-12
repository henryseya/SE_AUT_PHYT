import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#caja_de_busqueda.send_keys(Keys.ENTER)


miweb = webdriver.Chrome()
#miweb.set_window_size(1200, 600)
miweb.maximize_window()
miweb.get("https://www.google.com.ar")


caja_de_busqueda = miweb.find_element(By.ID,"APjFqb")


caja_de_busqueda.send_keys("Comida Italiana"+Keys.ENTER)


time.sleep(5)
miweb.quit()