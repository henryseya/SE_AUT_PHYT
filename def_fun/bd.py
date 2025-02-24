import mysql.connector


def busca_precio(producto):
    #Datos de acceso a la base de datos
    conexion= mysql.connector.connect(
        host="cursotesting.com.ar",
        user="testing",
        password="cursoperformance",
        database="productos"
        )


    #conectarme con la BD
    busqueda = conexion.cursor()
    # Nombre del producto a buscar
    #producto ="Sauce Labs Backpack"


    #Consultas SQL (Selección del producto por su nombre)
    consulta = f"SELECT nombre,precio FROM ecommerce where nombre = '{producto}'"
 
    #ejecutar la consulta
    busqueda.execute(consulta)


    resultado = busqueda.fetchone()
    busqueda.close()
    conexion.close()


    #print(resultado[0])
    return resultado[1]