import sqlite3
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

user_input = input("Introduce el ID del usuario: ")

query = f"SELECT * FROM users WHERE id = ?"    #? representa un espacio reservado para insertar un valor seguro
print(f"Consulta protegida ejecutada.")

cursor.execute(query, (user_input, ))    #recordar que al poner la , se trata a user_input como tupla y hacemos que sea inmutable
resultados = cursor.fetchall()

if resultados:
    for fila in resultados:
        print("ID: ", fila[0], "| Nombre:", fila [1])
else:
        print("No se encontró ningún usuario.")

conn.close()