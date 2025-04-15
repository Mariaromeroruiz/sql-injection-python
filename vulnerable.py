import sqlite3
conn = sqlite3.connect('usuarios.db')    #abro la conexión
cursor = conn.cursor()        #creo el cursor para enviar comandos sql

user_input = input("Introduce el ID del usuario: ")     #creamos el input para que el usuario añada la información en texto

query = f"SELECT * FROM users WHERE id = {user_input};"
print(f"Consulta ejecutada: {query}")     #hacemos la consulta que queremos junto con el input

cursor.execute(query)    #ejecuta la consulta en la base de datos
resultados = cursor.fetchall()   #trae los resultados

if resultados:
    for fila in resultados:
        print("ID: ", fila[0], "| Nombre:", fila [1])
else:
        print("No se encontró ningún usuario.")

conn.close()
