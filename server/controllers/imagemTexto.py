from models.ImagemTexto import ImagemTexto
import sys
sys.path.append('../../client/services/ocr_service.py')
import models.daos.imagemTexto as daoImagemTexto

class ImagemTextoExistente(Exception):
    pass

def listar():
    return daoImagemTexto.listar()

def localizar(id):
    return daoImagemTexto.localizar(id)

def criar(id, imagem, texto):
    image_to_text()
    if localizar(id) != None:
        raise ImagemTextoExistente()
    criado = ImagemTexto(id, imagem, texto)
    daoImagemTexto.criar(criado)
    return criado

def remover(id):
    existente = localizar(id)
    if existente == None:
        return None
    daoImagemTexto.remove(id)
    return existente

def atualizar(id, imagem):
    existente = localizar(id)
    if existente == None:
        return None
    image_to_text()
    daoImagemTexto.atualizar_imagem_texto(id, imagem, texto)
    return existente