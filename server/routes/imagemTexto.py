from flask import Blueprint, jsonify, request, render_template
import controllers.imagemTexto as cImagemTexto
import services.services as services
import base64
imagemTexto_api = Blueprint('imagemTexto_api', __name__)


@imagemTexto_api.route('/', methods=['GET'])
def index():
    return render_template('interface.html')


@imagemTexto_api.route('/imagemTexto', methods=['GET'])
def listar():
    lista = cImagemTexto.listar()
    return jsonify(services.to_dict_list(lista))


@imagemTexto_api.route('/imagemTexto/<int:id>', methods=['GET'])
def localizar(id):
    x = cImagemTexto.localizar(id)
    if not (x is None):
        return jsonify(services.to_dict(x))
    return '', 404


@imagemTexto_api.route('/imagemTexto', methods=['POST'])
def criar():
    dados = request.get_json()
    print(dados)
    try:
        base64string = dados['imagem'].encode("ascii")
        imagemBinary = base64.decodebytes(base64string)
        texto = services.image_to_text(imagemBinary)
        criado = cImagemTexto.criar(dados['id'], dados['imagem'], texto)
        return jsonify(services.to_dict(criado))
    except cImagemTexto.ImagemTextoExistente:
        return "Imagem já existe", 409
