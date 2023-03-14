import pymysql

conexion = pymysql.connect(host = 'localhost', user = 'root', passwd= '', 
                           db = 'software_prueba')
conn = conexion.cursor()
conn.execute("select nombre, apellido, semestre, grupo, tutor from alumnos")
print("___________________________________________________")
print()
print("Nombre  | Apellido  |  Semestre  |  Grupo  |  Tutor")
print("___________________________________________________")
for nombre, apellido, semestre, grupo, tutor in conn.fetchall():
    print(nombre, " | " , apellido, " | " ,semestre, " | " , grupo, " | " , tutor)
    print("___________________________________________________")
conn.close()

