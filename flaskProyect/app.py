
from flask import Flask

app= Flask(__name__)


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