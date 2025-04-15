import sqlite3
conn = sqlite3.connect('usuarios.db')  # Abro la conexión
cursor = conn.cursor()  # Creo el cursor para enviar comandos SQL
cursor.execute('''                  
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    nombre TEXT
)
''')             # Inserto datos
cursor.execute("INSERT OR IGNORE INTO users(id, nombre) VALUES (1, 'Juan')")
cursor.execute("INSERT OR IGNORE INTO users(id, nombre) VALUES (2, 'Alicia')")
cursor.execute("INSERT OR IGNORE INTO users(id, nombre) VALUES (3, 'Lola')")
cursor.execute("INSERT OR IGNORE INTO users(id, nombre) VALUES (4, 'Luis')")
cursor.execute("INSERT OR IGNORE INTO users(id, nombre) VALUES (5, 'Marina')")

conn.commit()  # Guardo el cambio


print("Se ha creado la base de datos con éxito")
