from config.database import con
from wrap_connection import transact
from models.ImagemTexto import ImagemTexto

sql_criar = "INSERT INTO ImagemTexto (id, imagem, texto) VALUES (?,?)"
sql_localizar = "SELECT id, imagem, texto FROM ImagemTexto WHERE id = ?"
sql_listar = "SELECT id, imagem, texto FROM ImagemTexto"
sql_remover = "DELETE FROM ImagemTexto WHERE id = ?"
sql_update = "UPDATE ImagemTexto SET imagem = ?, texto = ? WHERE id = ?"

@transact(con)
def listar():
    cursor.execute(sql_listar)
    resultado = []
    for (id, imagem, texto) in cursor.fetchall():
        resultado.append(ImagemTexto(id, imagem, texto))
    return resultado

@transact(con)
def localizar(id):
    cursor.execute(sql_localizar)
    linha = cursor.fetchone()
    if linha == None:
        return None
    return ImagemTexto(linha[0], linha[1], linha[2])

@transact(con)
def criar(imagemTexto):
    cursor.execute(sql_criar, (imagemTexto.id, imagemTexto.imagem, imagemTexto.texto))
    connection.commit()

@transact(con)
def remover(id):
    cursor.execute(sql_remover)

@transact(con)
def atualizar_imagem_texto(id, imagem, texto):
    cursor.execute(sql_update, (id, imagem, texto))
    connection.commit()