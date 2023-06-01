import json
import datetime
import requests
from flask import Flask, request 
from dataclasses import dataclass
from typing import Optional
from typing import Union

app = Flask(__name__)

@dataclass
class SensorData:
    timestamp: str
    value: Union[float, bool]

    def validate(self):
        if not self.timestamp:
            raise InvalidDataException("Missing timestamp")
        
        try:
            datetime.datetime.strptime(self.timestamp, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise InvalidDataException("Invalid timestamp format")

class InvalidDataException(Exception):
    def __init__(self, message):
        self.message = message

@app.route("/")
def welcome() : 
    return"Hello_World"

@app.route("/temp/<user>", methods=["POST"]) 
def temp(user) : 

    # Step 1: Validate input {timestamp: 111222, tempearature: 32}
    try:
        data_object = SensorData(**request.json)
        data_object.validate()
    except (TypeError, ValueError, InvalidDataException) as e:
        return str(e), 400   
     # make sure timestamp and temperature exist as keys | Make sure the timestamp follows a certain formatting YYYY.MM.DD HH:mm:ss:TZ | DD.MM.YY HH:mm | Make sure temperature is in a certain range
     # Step 2: write to DB
     # a) fetch the existing temp array for this user (rpi that sends the request)
     # b) append the newly sent value to the array
     # c) store this new array to firebase
    payload={}
    headers = {}
    url = f"https://pfee-3c043-default-rtdb.europe-west1.firebasedatabase.app/users/{user}/temp.json"
    try:
        response = requests.get(url, headers=headers, data=payload)
        response.raise_for_status()
        old_temp = response.json()
        if old_temp :  
            old_temp.append(data_object.__dict__)
        else : 
            old_temp = [data_object.__dict__]
        payload = json.dumps(old_temp)
        response = requests.put(url, headers=headers, data=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return "Error during request: " + str(e), 500
    except json.JSONDecodeError as e:
        return "Error decoding JSON response: " + str(e), 500
    except Exception as e:
        return "Error: " + str(e), 500

    return "Data added successfully", 200

@app.route("/humidity/<user>", methods=["POST"])
def humidity(user):
    try:
        data_object = SensorData(**request.json)
        data_object.validate()
    except (TypeError, ValueError, InvalidDataException) as e:
        return str(e), 400

    payload = {}
    headers = {}
    url = f"https://pfee-3c043-default-rtdb.europe-west1.firebasedatabase.app/users/{user}/humidity.json"
    try:
        response = requests.get(url, headers=headers, data=payload)
        response.raise_for_status()
        old_humidity = response.json()
        if old_humidity :  
            old_humidity.append(data_object.__dict__)
        else : 
            old_humidity = [data_object.__dict__]
        payload = json.dumps(old_humidity)
        response = requests.put(url, headers=headers, data=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return "Error during request: " + str(e), 500
    except json.JSONDecodeError as e:
        return "Error decoding JSON response: " + str(e), 500
    except Exception as e:
        return "Error: " + str(e), 500

    return "Data added successfully", 200

@app.route("/smoke/<user>", methods=["POST"])
def smoke(user):
    try:
        data_object = SensorData(**request.json)
        data_object.validate()
    except (TypeError, ValueError, InvalidDataException) as e:
        return str(e), 400

    payload = {}
    headers = {}
    url = f"https://pfee-3c043-default-rtdb.europe-west1.firebasedatabase.app/users/{user}/smoke.json"
    try:
        response = requests.get(url, headers=headers, data=payload)
        response.raise_for_status()
        old_smoke = response.json()
        if old_smoke :  
            old_smoke.append(data_object.__dict__)
        else : 
            old_smoke = [data_object.__dict__]
        payload = json.dumps(old_smoke)
        response = requests.put(url, headers=headers, data=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return "Error during request: " + str(e), 500
    except json.JSONDecodeError as e:
        return "Error decoding JSON response: " + str(e), 500
    except Exception as e:
        return "Error: " + str(e), 500

    return "Data added successfully", 200

@app.route("/movement/<user>", methods=["POST"])
def movement(user):
    try:
        data_object = SensorData(**request.json)
        data_object.validate()
    except (TypeError, ValueError, InvalidDataException) as e:
        return str(e), 400

    payload = {}
    headers = {}
    url = f"https://pfee-3c043-default-rtdb.europe-west1.firebasedatabase.app/users/{user}/movement.json"
    try:
        response = requests.get(url, headers=headers, data=payload)
        response.raise_for_status()
        old_movement = response.json()
        if old_movement :  
            old_movement.append(data_object.__dict__)
        else : 
            old_movement = [data_object.__dict__]

        payload = json.dumps(old_movement)
        response = requests.put(url, headers=headers, data=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return "Error during request: " + str(e), 500
    except json.JSONDecodeError as e:
        return "Error decoding JSON response: " + str(e), 500
    except Exception as e:
        return "Error: " + str(e), 500

    return "Data added successfully", 200



if (__name__=="__main__") : 
    app.run(host="0.0.0.0")