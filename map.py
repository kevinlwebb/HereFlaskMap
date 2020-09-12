
import requests
import os
from flask import Flask,render_template

URL = "https://discover.search.hereapi.com/v1/discover"
latitude = 32.715736
longitude = -117.161087
query = 'hospital'
limit = 5
api_key = os.environ.get('HEREAPIKEY')

PARAMS = {
            'apikey': api_key,
            'q':query,
            'limit': limit,
            'at':'{},{}'.format(latitude,longitude)
         } 

# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 
data = r.json()

hospitals = []

for i in range(5):
    hospitals.append({
        'title': data['items'][i]['title'],
        'address': data['items'][i]['address']['label'],
        'latitude': data['items'][i]['position']['lat'],
        'longitude': data['items'][i]['position']['lng'],
    })


app = Flask(__name__)

@app.route('/')
def map_func():
	return render_template('map.html',
                            latitude = latitude,
                            longitude = longitude,
                            apikey=api_key,
                            hospitals = hospitals
                            )

if __name__ == '__main__':
	app.run(debug = False)
