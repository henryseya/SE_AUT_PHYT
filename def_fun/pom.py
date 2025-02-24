import time


def varios_clicks(selector, cantidad):
    for i in range(cantidad):  # repetir cantidad de veces la orden siguiente
       selector.click()
       espera(1)


def espera(segundos):
    time.sleep(segundos)   