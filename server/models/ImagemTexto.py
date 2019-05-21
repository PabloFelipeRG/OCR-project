class ImagemTexto():
    def __init__(self, id, imagem, texto):
        self._id = id
        self._imagem = imagem
        self._texto = texto

    @property
    def id(self):
        return self._id

    @property
    def imagem(self):
        return self._imagem

    @property
    def texto(self):
        return self._texto
