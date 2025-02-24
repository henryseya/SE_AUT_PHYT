'''
def obtener_selectores():
    #En base a un diccionario de python
    formulario = {
        "browse":{
            "cards-1":"#design-tab-pane > div > div:nth-child(1) > div > a > div > div > h5",
            "cards-2":"#design-tab-pane > div > div:nth-child(2) > div > a > div > div > h5",
            "cards-3":"#design-tab-pane > div > div:nth-child(3) > div > a > div > div > h5"
        }
    }


    return formulario['browse']
'''

def selectores_formulario():
    formulario = {
            "nombre":"firstName",
            "apellido":"lastName",
            "nombre_usuario":"username",
            "email":"email",
            "direccion1":"address",
            "direccion2":"address2",
            "pais":"address2",
        }
    return formulario