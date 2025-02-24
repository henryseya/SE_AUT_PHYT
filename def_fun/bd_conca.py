import mysql.connector


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
producto ="Sauce Labs Backpack"


#Consultas SQL (Selección del producto por su nombre)
consulta = f"SELECT precio FROM ecommerce where nombre = '{producto}'"
print(consulta)
#ejecutar la consulta
busqueda.execute(consulta)


resultado = busqueda.fetchone()
print(resultado[0])