def obtener_selectores():
    #En base a un diccionario de python
    pantalla= {
        "menu":{
            "contactenos": "CONTACT",
            "inicio":"HOME",
            "preguntas":"Faqs"
        },
        "iframe": {
            "zoom-in": "#mapDiv > div > div.gm-style > div:nth-child(13) > div > div > div > button:nth-child(1)",
            "zoom-out": "#mapDiv > div > div.gm-style > div:nth-child(13) > div > div > div > button:nth-child(3)"
        },
        "browse":{
            "cards-1":"#design-tab-pane > div > div:nth-child(1) > div > a > div > div > h5",
            "cards-2":"#design-tab-pane > div > div:nth-child(2) > div > a > div > div > h5",
            "cards-3":"#design-tab-pane > div > div:nth-child(3) > div > a > div > div > h5"
        }
    }


    return pantalla