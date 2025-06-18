
from flask import Flask,jsonify,render_template
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
       

#ruta de inicio
@app.route('/')
def home():
     return render_template('formulario.html') 


#ruta de consulta
@app.route('/consulta')
def consulta():
     return render_template('consulta.html')

#ruta try-catch
@app.errorhandler(404)
def paginaNoE(e):
     return 'Cuidado error de capa 8 !!!',404



if __name__ == '__main__':
    app.run(port=5000,debug=True)
    