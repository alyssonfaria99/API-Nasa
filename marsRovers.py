import requests
import json
import matplotlib.pyplot as plt
from skimage import io

with open('key.json', 'r') as file:
    keys = json.load(file)

api_key = keys["API_KEY"]
BASE_URL = "https://api.nasa.gov/mars-photos/api/v1"
endpoint = "/rovers/curiosity/photos"
cameras = ['NAVCAM']

while True:
    pagina = 1

    params = {
        "api_key": api_key,
        "sol": 2,
        "page": pagina
    }

    res = requests.get(BASE_URL+endpoint, params=params)
    resJSON = res.json()
    fotos = resJSON.get('photos')

    if not fotos:
        print("Acabaram as fotos.")
        break

    for foto in fotos:
        if foto['camera']['name'] in cameras:
            url = foto['img_src']
            id = foto['id']

            img = io.imread(url)
            plt.imshow(img)
            plt.title(f"Página {pagina} | Câmera: {foto['camera']['name']} | ID: {id}")
            plt.show()

    pagina += 1
    

