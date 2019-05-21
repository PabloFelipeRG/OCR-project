var data = {
    image: null
}

function handleFieldChange(value, field) {
    let file = value.target.files[0];
    var reader = new FileReader();
    reader.onload = (function (theFile) {
        return function (e) {
            let binaryData = e.target.result;
            //Converting Binary Data to base 64
            let base64String = window.btoa(binaryData);
            data[field] = base64String;
            console.log(data);
        };
    })(file);
    // Read in the image file as a data URL.
    reader.readAsBinaryString(file);
}

function submit() {
    if (data['image'] === null) {
        alert('Você ainda não selecionou nenhuma imagem!')
        return;
    } else {
        fetch(`http://localhost:5000/imagemTexto`, {
            method: 'post',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                id: Math.floor((Math.random() * 10000) + 1),
                imagem: data['image']
            })
        })
            .then(res => res.json())
            .then(response => {
                console.log(response);
            })
            .catch(console.error);
    }
}