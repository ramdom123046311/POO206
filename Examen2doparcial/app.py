
from flask import Flask,jsonify,render_template,request,url_for,flash,redirect
from flask_mysqldb import MySQL
import MySQLdb

app= Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="peliculas"

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
          cursor.execute("SELECT * FROM tb_albums WHERE state = 1")
          consultaTodo= cursor.fetchall()
          return render_template('formulario.html', errores={},peliculas=consultaTodo)
      
     except Exception as e:
          print('Error al consultar todo: '+e)
          return render_template('formulario.html',errores={},peliculas=[])
     
     finally:
          cursor.close()
            
#ruta confirmar eliminacion
@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_album(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE tb_albums SET state = 0 WHERE id = %s", (id,))
        mysql.connection.commit()
        return redirect('/')
    except Exception as e:
        mysql.connection.rollback()
        return f"Error al eliminar el álbum: {str(e)}"
    finally:
        cursor.close()
#ruta eliminar
@app.route('/eliminar/<int:id>')
def eliminar_confirmacion(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM tb_peliculas WHERE id = %s", (id,))
        pelicula = cursor.fetchone()
        return render_template('confirmDel.html', pelicula=pelicula)
    except Exception as e:
        print("Error al cargar confirmación:", str(e))
        return redirect(url_for('home'))
    finally:
        cursor.close()

#ruta de consulta
@app.route('/consulta')
def consulta():
     return render_template('consulta.html')

#ruta de consulta
@app.route('/guardarPelicula',methods=['Post'])
def guardar():
     
     #listas o diccionarios
     errores={}
     
     #obtener los datos al insertar (Variables de la vista)
     Vtitulo= request.form.get('txtTitulo','').strip()
     Vdirector= request.form.get('txtDirector','').strip()
     Vanio= request.form.get('txtAnio','').strip()
     Vgenero= request.form.get('txtGenero','').strip()
     
     if not Vtitulo:
          errores['txtTitulo']= 'Nombre del titulo obligatorio'
     if not Vdirector:
          errores['txtDirector']='Nombre de director obligatorio'
     if not Vgenero:
          errores['txtGenero']='Nombre de genero obligatorio'
     if not Vanio:
          errores['txtAnio']='Anio obligatorio'
     elif not Vanio.isdigit() or int(Vanio)< 1800 or int(Vanio)> 2100:
          errores['txtAnio']= 'ingresa un anio valido'
          
     if not errores: 
          try:
              cursor= mysql.connection.cursor()
              cursor.execute('insert into tb_albums(album,artista,anio) values(%s,%s,%s)',(Vtitulo,Vdirector,Vgenero,Vanio))
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
     

@app.route('/actualizar/<int:id>', methods=['GET'])
def actualizar(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tb_peliculas WHERE id=%s', (id,))
        album = cursor.fetchone()
        return render_template('actualizar.html', album=album)

    except Exception as e:
        print('Error al consultar para actualizar: ' + str(e))
        return redirect(url_for('home'))

    finally:
        cursor.close()

@app.route('/guardarCambios/<int:id>', methods=['POST'])
def guardarCambios(id):
    Vtitulo = request.form.get('txtTitulo', '').strip()
    Vartista = request.form.get('txtArtista', '').strip()
    Vanio = request.form.get('txtAnio', '').strip()

    errores = {}

    if not Vtitulo:
        errores['txtTitulo'] = 'El título es obligatorio.'
    if not Vartista:
        errores['txtArtista'] = 'El artista es obligatorio.'
    if not Vanio or not Vanio.isdigit() or int(Vanio) < 1800 or int(Vanio) > 2100:
        errores['txtAnio'] = 'Año inválido.'

    if errores:
        return render_template('actualizar.html', album=(id, Vtitulo, Vartista, Vanio), errores=errores)

    try:
        cursor = mysql.connection.cursor()
        cursor.execute("""
            UPDATE tb_albums
            SET album=%s, artista=%s, anio=%s
            WHERE id=%s
        """, (Vtitulo, Vartista, Vanio, id))
        mysql.connection.commit()
        flash('Album actualizado correctamente')
        return redirect(url_for('home'))

    except Exception as e:
        mysql.connection.rollback()
        return f"Error al actualizar el album: {str(e)}"

    finally:
        cursor.close()

#ruta try-catch
@app.errorhandler(404)
def paginaNoE(e):
     return 'Cuidado error de capa 8 !!!',404



if __name__ == '__main__':
    app.run(port=5000,debug=True)