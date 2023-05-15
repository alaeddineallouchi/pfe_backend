from flask import Flask 

app = Flask(__name__)


@app.route("/")
def welcome() : 
    return"Hello_World"


@app.route("/temp", method="POST") 
def temp() : 
    # Step 1: Validate input {timestamp: 111222, tempearature: 32}
    data_object = request.get_json()
    # make sure timestamp and temperature exist as keys | Make sure the timestamp follows a certain formatting YYYY.MM.DD HH:mm:ss:TZ | DD.MM.YY HH:mm | Make sure temperature is in a certain range
    
    # Step 2: write to DB
    status_code = request.post(url_to_fire_base)
    if status_code != 204:
        #raise an error, or notify
    return 200

@app.route("/temp", method="GET") 
def temp() : 
    # Read value from firebase
    response = request.get(url_to_fire_base)
    if response.status_code != 200:
        #raise an error, or notify
    return response.get_json()

@app.route("/humidity")
def humidity() : 
    return "yes or no "

@app.route("/smoke")
def smoke() : 
    return"no smoke "

@app.route("/movement")
def movement() : 
    return "yes or no "


if (__name__=="__main__") : 
    app.run(host="0.0.0.0")
