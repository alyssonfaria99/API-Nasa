import requests
import json

with open('key.json', 'r') as file:
    keys = json.load(file)

api_key = keys["API_KEY"]
params = {
    "api_key": api_key
}
BASE_URL = "https://api.nasa.gov/mars-photos/api/v1"
endpoint = "/manifests/curiosity"

res = requests.get(BASE_URL+endpoint,params=params)
if(res.status_code == 500):
    print('Servidor indisponível.')
else:
    resJSON = res.json()
    photo_manifest = resJSON.get('photo_manifest')
    max_sol = photo_manifest['max_sol']
    max_date = photo_manifest['max__date']
    print(max_sol)
    print(max_date)