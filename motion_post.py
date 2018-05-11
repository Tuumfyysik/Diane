# Python 3.6

import urllib.request
from json import dumps
import datetime
import config as cfg

# define url, headers and parameters of POST request

api_key = cfg.api['api_key']
device = cfg.device['name']
url = cfg.api['url']

headers = {}
params = {
    "api_key": api_key,
    "device": device,
    "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "image_name": "image1.jpg"
}

# prepare POST data

data = dumps(params).encode('ascii')
req = urllib.request.Request(url, data, headers=headers)

try:
    response = urllib.request.urlopen(req)
    print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("http error: ", e.reason)