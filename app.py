from flask import Flask
from keys import key
import requests

app = Flask(__name__)

@app.route('/')
def tagPhoto():

    # API request URL
    url = 'https://api.projectoxford.ai/vision/v1.0/analyze'

    # URL of the image you want tagged
    imageUrl = 'https://s-media-cache-ak0.pinimg.com/736x/37/11/f6/3711f6644f38c5a0d58ce2853c00ca71.jpg'

    # authorize the API call
    headers = dict()
    headers['Ocp-Apim-Subscription-Key'] = key

    json = { 'url': imageUrl }
    params = { 'visualFeatures' : 'Tags' }
    data = None

    # get the response
    response = requests.request('post', url, json=json, data=data, headers=headers, params=params)

    # get status code
    status = response.status_code

    # get tags
    tags = ''
    response_tags = response.json()['tags']
    for tag in response_tags:
        tags = tags + str(tag['name']) + ' '
    
    return tags