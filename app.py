from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Clave secreta para la sesión, cámbiala por algo más seguro

# Lista de publicaciones del foro (simulación de una base de datos)
posts = []

# Lista de usuarios con permisos para publicar
usuarios_con_permisos = {'usuario1', 'usuario2'}  # Agrega los nombres de usuario permitidos aquí

# Ruta para la página principal del foro
@app.route('/')
def index():
    return render_template('index.html', posts=posts)

# Ruta para agregar un nuevo post
@app.route('/nuevo_post', methods=['GET', 'POST'])
def nuevo_post():
    if 'usuario' not in session or session['usuario'] not in usuarios_con_permisos:
        return redirect(url_for('index'))  # Redirige si el usuario no tiene permisos
    if request.method == 'POST':
        autor = session['usuario']
        titulo = request.form['titulo']
        contenido = request.form['contenido']
        posts.append({"autor": autor, "titulo": titulo, "contenido": contenido})
        return redirect(url_for('index'))
    return render_template('nuevo_post.html')

# Ruta para iniciar sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        if usuario in usuarios_con_permisos:
            session['usuario'] = usuario
            return redirect(url_for('index'))
    return render_template('login.html')

# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
