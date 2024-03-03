from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Lista de publicaciones del foro (simulación de una base de datos)
posts = [
    {"autor": "Usuario1", "titulo": "Primer Post", "contenido": "¡Hola, mundo!", "imagen": "imagen1.jpg"},
    {"autor": "Usuario2", "titulo": "Segundo Post", "contenido": "¡Hola, foro!", "imagen": "imagen2.jpg"}
]

# Ruta para la página principal del foro
@app.route('/')
def index():
    return render_template('index.html', posts=posts)

# Ruta para agregar un nuevo post
@app.route('/nuevo_post', methods=['GET', 'POST'])
def nuevo_post():
    if request.method == 'POST':
        autor = request.form['autor']
        titulo = request.form['titulo']
        contenido = request.form['contenido']
        imagen = request.files['imagen']
        if imagen.filename != '':
            imagen.save(os.path.join('static', 'imagenes', imagen.filename))
        posts.append({"autor": autor, "titulo": titulo, "contenido": contenido, "imagen": imagen.filename})
        return redirect(url_for('index'))
    return render_template('nuevo_post.html')

if __name__ == '__main__':
    app.run(debug=True)
