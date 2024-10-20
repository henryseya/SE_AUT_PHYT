import csv

with open('mis_datos/datos.csv','r') as csv_archivo:  # indicar el archivo de datos y su nombre en el test
   csv_reader = csv.reader(csv_archivo)     # leo el contenido del archivo globalmente
   for renglon in csv_reader:               # leo un renglon del contenido global
      var_usuario,var_clave,var_email = renglon # generar 3 variables en base al renglón
      print(var_email )

