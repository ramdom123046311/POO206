from flask import Flask, jsonify
from flask_mysqldb import MySQL
from config import Config
from extensions import mysql

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    mysql.init_app(app)
    
    from controllers.albumController import albumBP
    app.register_blueprint(albumBP)
    
    @app.route('/DBCheck')
    def DB_check():
        try:
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT 1')
            cursor.close()
            return jsonify({'status': 'ok', 'message': 'Conectado con exito'}), 200
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)}), 500

    @app.errorhandler(404)
    def paginaNoE(e):
        return 'Cuidado error de capa 8 !!!', 404

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5000, debug=True)
