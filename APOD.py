import requests
import json
import matplotlib.pyplot as plt
from skimage import io

BASE_URL = 'https://api.nasa.gov/planetary/apod'

with open('key.json', 'r') as file:
    keys = json.load(file)

api_key = keys["API_KEY"]

params = {
    "api_key": api_key
}

res = requests.get(BASE_URL, params)
resJSON = res.json()

url = resJSON['url']
title = resJSON['title']

print(resJSON.get("explanation"))
print(resJSON.get("copyright"))
img = io.imread(url)
# plt.imshow(img)
# plt.title(title)
# plt.show()

XRateLimitLimit = res.headers['X-RateLimit-Limit']
XRateLimitRemaining = res.headers['X-RateLimit-Remaining']
print(XRateLimitLimit)
print(XRateLimitRemaining)
