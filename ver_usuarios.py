import sqlite3
print("Script iniciado")
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
usuarios = cursor.fetchall()

for user in usuarios:
    print("ID:", user[0], "| Nombre:", user[1])



conn.close()


