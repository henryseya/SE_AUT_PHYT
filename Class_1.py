import time
from selenium import webdriver


driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver.get("https://www.google.com.ar")
driver.get("https://devapp.swevenbpm.com")


time.sleep(5)
driver.quit()