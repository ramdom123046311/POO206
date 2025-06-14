
from flask import Flask,jsonify
from flask_mysqldb import MySQL
import MySQLdb

app= Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="dbflask"

mysql= MySQL(app)

#ruta para probar conexion a mysql
@app.route('/DBCheck')
def DB_check():
     try:
          cursor= mysql.connection.cursor()
          cursor.execute('select 1')
          return jsonify( {'status':'ok','message':'Conectado con exito'} ),200     
     except MySQLdb.MySQLError as e:return jsonify( {'status':'error','message':str(e)} ),500
       

#ruta simple
@app.route('/')
def home():
     return 'hola mundo flask'   

#ruta con parametros
@app.route('/saludo/<nombre>')
def saludar(nombre):
     return 'hola,'+nombre+'!!!'

#ruta try-catch
@app.errorhandler(404)
def paginaNoE(e):
     return 'Cuidado error de capa 8 !!!',404

#ruta doble
@app.route('/usuario')
@app.route('/usuaria')
def dobleroute():
     return 'Soy el mismo recurso del servidor'

#ruta con parametros
@app.route('/formulario',methods=['POST'])
def formulario():
     return 'soy un formulario'

if __name__ == '__main__':
    app.run(port=5000,debug=True)