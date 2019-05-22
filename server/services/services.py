import jsons


def image_to_text(imagem):
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    content = imagem
    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Resultado:', texts[0].description)
    return texts[0].description


def to_dict(obj):
    return jsons.dump(obj, strip_privates=True)


def to_dict_list(lista):
    resultado = []
    for item in lista:
        resultado.append(to_dict(item))
    return resultado
