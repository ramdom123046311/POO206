
from flask import Flask,jsonify,render_template,request,url_for,flash,redirect
from flask_mysqldb import MySQL
import MySQLdb

app= Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="dbflask"

app.secret_key='mysecretkey'
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
     try:
          cursor= mysql.connection.cursor()
          cursor.execute('SELECT* From tb_albums')
          consultaTodo= cursor.fetchall()
          return render_template('formulario.html', errores={},albums=consultaTodo)
      
     except Exception as e:
          print('Error al consultar todo: '+e)
          return render_template('formulario.html',errores={},albums=[])
     
     finally:
          cursor.close()

#ruta de consulta
@app.route('/consulta')
def consulta():
     return render_template('consulta.html')

#ruta de consulta
@app.route('/guardarAlbum',methods=['Post'])
def guardar():
     
     #listas o diccionarios
     errores={}
     
     #obtener los datos al insertar (Variables de la vista)
     Vtitulo= request.form.get('txtTitulo','').strip()
     Vartista= request.form.get('txtArtista','').strip()
     Vanio= request.form.get('txtAnio','').strip()
     
     if not Vtitulo:
          errores['txtTitulo']= 'Nombre del album obligatorio'
     if not Vartista:
          errores['txtArtista']='Nombre de artista obligatorio'
     if not Vanio:
          errores['txtAnio']='Anio obligatorio'
     elif not Vanio.isdigit() or int(Vanio)< 1800 or int(Vanio)> 2100:
          errores['txtAnio']= 'ingresa un anio valido'
          
     if not errores: 
          try:
              cursor= mysql.connection.cursor()
              cursor.execute('insert into tb_albums(album,artista,anio) values(%s,%s,%s)',(Vtitulo,Vartista,Vanio))
              mysql.connection.commit()
              flash('Album se ha guardado correctamente en bd')
              return redirect(url_for('home'))

          except Exception as e:
           mysql.connection.rollback()
           return ('algo fallo'+ str(e))
           return redirect(url_for('home'))
      
          finally:
               cursor.close()
               
     return render_template('formulario.html', errores=errores)

#ruta detalle
@app.route('/detalle/<int:id>')
def detalle(id):
     try:
          cursor= mysql.connection.cursor()
          cursor.execute('SELECT * FROM tb_albums WHERE id=%s' ,(id,))
          consulta1= cursor.fetchone()
          return render_template('consulta.html',album=consulta1)
      
     except Exception as e:
          print('Error al consultar id: '+str(e))
          return redirect(url_for('home'))
     
     finally:
          cursor.close()
     


#ruta try-catch
@app.errorhandler(404)
def paginaNoE(e):
     return 'Cuidado error de capa 8 !!!',404



if __name__ == '__main__':
    app.run(port=5000,debug=True)
    