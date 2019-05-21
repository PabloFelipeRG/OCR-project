from flask import Flask, jsonify, request, render_template
from routes.imagemTexto import imagemTexto_api
from config.database import criar_bd
app = Flask(__name__)
app.register_blueprint(imagemTexto_api)
criar_bd()

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=False)
