from PIL import Image
from flask import Blueprint, jsonify, request, render_template
import base64
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
        base64string = dados['imagem'].encode("ascii")
        imagemBinary = base64.decodebytes(base64string)
        texto = image_to_text(imagemBinary)
        criado = cImagemTexto.criar(dados['id'], dados['imagem'], texto)
        return jsonify(criado)
    except cImagemTexto.ImagemTextoExistente:
        return "Imagem já existe", 409

def image_to_text(imagem):
    import io
    import os
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    content = imagem
    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Resultado:', texts[0].description)
    return texts[0].description