var data = {
    image: null
}

function handleFieldChange(value, field) {
    let file = value.target.files[0],
        reader = new FileReader();
    if (!file) {
        alert("Nenhuma imagem foi anexada.");
        return;
    }
    reader.onload = (function (theFile) {
        if (theFile.type.slice(0, 5) === "image") {
            return function (e) {
                let binaryData = e.target.result;
                //Converting Binary Data to base 64
                let base64String = window.btoa(binaryData);
                data[field] = base64String;
                alert(`Imagem ${theFile.name} anexado com sucesso!`);
            };
        } else {
            alert(`O arquivo deve ser uma imagem.`);
            data.image = null;
            return;
        }
    })(file);
    // Read in the image file as a data URL.
    if (file) {
        reader.readAsBinaryString(file);
        file = null;
    }
}

function submit() {
    if (data['image'] === null) {
        alert('Você ainda não selecionou nenhuma imagem.');
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
                data.image = null;
                renderImagemTexto(response);
            })
            .catch(console.error);
    }
}

function galeria() {
    fetch(`http://localhost:5000/imagemTexto`, {
        method: 'get',
        headers: { 'Content-Type': 'application/json' }
    })
        .then(res => res.json())
        .then(response => {
            if (response.length > 1) {
                response.forEach(imagemTexto => renderImagemTexto(imagemTexto));
            } else if (response.length === 1) {
                renderImagemTexto(response[0]);
            }
        })
        .catch(console.error);
}

function renderImagemTexto(imagemTexto) {
    let row_html = document.querySelector("#template_url"),
        div = document.createElement("div"),
        template = `
            <div class="col-md-12">
                <div class="card mb-4 shadow-sm">
                    <img src="data:image/png;base64, ${imagemTexto.imagem}" 
                    alt="${imagemTexto.texto}" style="width: 180px; height: 200px;">
                    <div class="card-body" style="border-top: 1px grey solid">
                        <p class="card-text" data-toggle="tooltip" data-placement="bottom" title='${imagemTexto.texto}'>${imagemTexto.texto}</p>
                    </div>
                </div>
            </div>`
    div.setAttribute('style', "width: 220px; height: 200px; margin-bottom: 85px");
    div.innerHTML = template;
    row_html.appendChild(div)
}