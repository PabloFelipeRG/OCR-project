def image_to_text(base64 = False):
    import io
    import os
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    if(base64 == False):
        file_name = os.path.join(os.path.dirname(__file__),'../assets/images/texto.png')
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()
        image = vision.types.Image(content=content)
    else:
        image = base64

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Resultado:', texts[0].description)
    return texts[0].description