from flask import Flask
from flask import render_template, request, redirect
from flaskext.mysql import MySQL


app = Flask(__name__)
mysql=MySQL()

app.config ['MYSQL_DATABSE_HOST']='localhost'
app.config ['MYSQL_DATABSE_USER']='root'
app.config ['MYSQL_DATABSE_PASSWORD']=''
app.config ['MYSQL_DATABSE_DB']='sitio'
mysql.init_app(app)

@app.route('/')
def inicio():
    return render_template('sitio/index.html')

@app.route('/peliculas')
def peliculas():
    return render_template('sitio/peliculas.html')

@app.route('/nosotros')
def nosotros():
    return render_template('sitio/nosotros.html')

@app.route('/admin/')
def admin_index():
    return render_template('admin/index.html')

@app.route('/admin/login')
def admin_login():
    return render_template('admin/login.html')

@app.route('/admin/peliculas')
def admin_peliculas():
    return render_template('/admin/peliculas.html')

@app.route('/admin/peliculas/guardar', methods=['POST'])
def admin_peliculas_guardar():
    _nombre=request.form['txtNombre']
    _URL=request.form['txtURL']
    _Archivo=request.files['txtImagen']   
    return redirect('/admin/peliculas')

if __name__ == '__main__':
    app.run(debug=True)