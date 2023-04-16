from flask import Flask 

app = Flask(__name__)


@app.route("/")
def welcome() : 
    return"Hello_World"


@app.route("/temp")
def welcome() : 
    return"temp is 20 deg"

if (__name__=="__main__") : 
    app.run()
