from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#relacionar el script actual con el archivo selectores.py
from def_fun.selectores import obtener_selectores
from def_fun.pom import varios_clicks,espera

###################  traigo los selectores a una variable
mis_selectores = obtener_selectores()  #obtiene todos los datos de pantalla
#selecciono solamente el menu de todos los demas selectores
mi_menu = mis_selectores['menu']['contactenos']
los_zoom = mis_selectores['iframe']

driver = webdriver.Chrome()
driver.implicitly_wait(1) # impacta en toda la carga
driver.maximize_window()
driver.get("https://institutoweb.com.ar/ejemplo1/")

lnk_contacto = driver.find_element(By.LINK_TEXT,mi_menu)
lnk_contacto.click()
#espera(2)
#Indicar a selenium que los próximos selectores están dentro de un iframe
iframe_selector = driver.find_element(By.CSS_SELECTOR,"#section_5 > div > div > div.col-lg-5.col-12.mb-4.mb-lg-0 > iframe")
#Espera explicita para el google map de 3 segundos
WebDriverWait(driver,3).until(EC.frame_to_be_available_and_switch_to_it(iframe_selector))

#driver.switch_to.frame(0)


#Click sobre el Zoom + 
btn_zoom_mas = driver.find_element(By.CSS_SELECTOR,los_zoom['zoom-in'])
# hago varios clicks sobre un elemento
varios_clicks(btn_zoom_mas,7)

btn_zoom_menos = driver.find_element(By.CSS_SELECTOR,los_zoom['zoom-out'])

# hago varios clicks sobre un elemento
varios_clicks(btn_zoom_menos,9)

espera(4)
driver.quit()