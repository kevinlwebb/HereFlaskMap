
import requests
import os
from flask import Flask,render_template
import csv

latitude = 32.715736
longitude = -117.161087
api_key = os.environ.get('HEREAPIKEY')


def addr_2_coor(address):
    URL = "https://geocode.search.hereapi.com/v1/geocode"
    latitude = 32.715736
    longitude = -117.161087
    query = address
    limit = 5
    api_key = os.environ.get('HEREAPIKEY')

    PARAMS = {
                'apikey': api_key,
                'q':query,
                'limit': limit,
            } 

    # sending get request and saving the response as response object 
    r = requests.get(url = URL, params = PARAMS) 
    data = r.json()
    return data['items'][0]['position']

def csv_2_data(path):
    reader = csv.DictReader(open(path, 'rt'))

    dict_list = []

    for line in reader:
        dict_list.append(line)

    places = []

    for i in range(5):
        coor = addr_2_coor(dict_list[i]['Address'] + ", San Diego, California")
        places.append({
            'title': dict_list[i]['Resource Parent'],
            'address': dict_list[i]['Address'] + ", San Diego, California",
            'latitude': coor['lat'],
            'longitude': coor['lng'],
        })

    return places


def discover(search):
    '''
    Utilizes HERE's discover API to search a word or phrase for Point of Interests
    '''

    URL = "https://discover.search.hereapi.com/v1/discover"
    latitude = 32.715736
    longitude = -117.161087
    query = search
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

    places = []

    for i in range(5):
        places.append({
            'title': data['items'][i]['title'],
            'address': data['items'][i]['address']['label'],
            'latitude': data['items'][i]['position']['lat'],
            'longitude': data['items'][i]['position']['lng'],
        })

    return places

# Utilize this for dynamic information
#places = discover("food pantry")

#Utilize this for information from a csv
places = csv_2_data('data/sample-211-food-banks.csv')

app = Flask(__name__)

@app.route('/')
def map_func():
	return render_template('map.html',
                            latitude = latitude,
                            longitude = longitude,
                            apikey=api_key,
                            places = places
                            )

if __name__ == '__main__':
	app.run(debug = False)
