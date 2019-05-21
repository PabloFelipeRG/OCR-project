from models.ImagemTexto import ImagemTexto
import sys
import models.daos.imagemTexto as daoImagemTexto

class ImagemTextoExistente(Exception):
    pass

def listar():
    return daoImagemTexto.listar()

def localizar(id):
    return daoImagemTexto.localizar(id)

def criar(id, imagem, texto):
    criado = ImagemTexto(str(id), imagem, texto)
    print("OBJETO", criado)
    daoImagemTexto.criar(criado)
    return criado