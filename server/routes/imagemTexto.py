from PIL import Image
from flask import Blueprint, jsonify, request, render_template
import controllers.imagemTexto as cImagemTexto
imagemTexto_api = Blueprint('imagemTexto_api', __name__, template_folder='../../client/templates')

@imagemTexto_api.route('/handle_data', methods=['POST'])
def handle_data():
    img = Image.open(request.files['file'])
    print(img)
    return 'Success!'

@imagemTexto_api.route('/', methods=['GET'])
def index():
    return render_template('interface.html')

@imagemTexto_api.route('/imagemTexto', methods=['GET'])
def listar():
    lista = cImagemTexto.listar()
    return jsonify(lista)

@imagemTexto_api.route('/imagemTexto/<int:id>', methods=['GET'])
def localizar(id):
    x = cImagemTexto.localizar(id)
    if x != None:
        return jsonify(to_dict(x))
    return '', 404

@imagemTexto_api.route('/imagemTexto', methods=['POST'])
def criar():
    dados = request.get_json()
    print(dados)
    try:
        criado = cImagemTexto.criar(dados['id'], dados['imagem'], dados['texto'])
        return jsonify(criado)
    except cImagemTexto.ImagemTextoExistente:
        return "Imagem já existe", 409

@imagemTexto_api.route('/imagemTexto/<int:id>', methods=['DELETE'])
def remover(id):
    removido = cImagemTexto.remover(id)
    if removido != None:
        return jsonify(removido)
    return '', 404

@imagemTexto_api.route('/imagemTexto/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.get_json()
    try:
        atualizado = cImagemTexto.atualizar(id, dados['id'], dados['nome'])
    except cImagemTexto.ImagemTextoExistente:
        return "Imagem já existe", 409
    if atualizado != None:
        return jsonify(atualizado)
    return '', 404