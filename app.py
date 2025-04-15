from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

HTML = '''
    <h2>Consulta de Usuarios</h2>
    <form method="POST">
        <input type="text" name="user_input" placeholder="Introduce ID o payload">
        <button type="submit">Consultar</button>
    </form>
    {% if resultado %}
        <ul>
            {% for fila in resultado %}
                <li>ID: {{ fila[0] }} | Nombre: {{ fila[1] }}</li>
            {% endfor %}
        </ul>
    {% elif resultado is not none %}
        <p>No se encontró ningún usuario.</p>
    {% endif %}
'''

#  VERSIÓN VULNERABLE
@app.route("/vulnerable", methods=["GET", "POST"])
def vulnerable():
    resultado = None
    if request.method == "POST":
        user_input = request.form["user_input"]
        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE id = {user_input};"
        try:
            cursor.execute(query)
            resultado = cursor.fetchall()
        except:
            resultado = []
        conn.close()
    return render_template_string(HTML, resultado=resultado)

#  VERSIÓN SEGURA
@app.route("/seguro", methods=["GET", "POST"])
def seguro():
    resultado = None
    if request.method == "POST":
        user_input = request.form["user_input"]
        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE id = ?"
        try:
            cursor.execute(query, (user_input,))
            resultado = cursor.fetchall()
        except:
            resultado = []
        conn.close()
    return render_template_string(HTML, resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
