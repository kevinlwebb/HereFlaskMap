# HERE Flask Map

## Instructions (Skip steps 2 and 3 if .pkl file and .db database exists):
1. Run the following command to install necessary libraries.
```
pip3 install -r requirements.txt
```

2. Set Environment Variable `HEREAPIKEY` with key. Below is an example for Mac Terminal:
```
export HEREAPIKEY=givenkeyfromwebsite
```

3. Place HERE JavaScript key in file `map.html` on line `'apikey': 'placekeyhere'` .

4. Run the following command in the app's directory to run the web app.
```
python3 map.py
```

5. Go to http://127.0.0.1:5000

## Demo
![](readme/demo.gif)