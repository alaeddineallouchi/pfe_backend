import random
import requests
import time
from datetime import datetime

def simulate_sensor(user_id):
    while True:
        SENSOR_NAMES = ["temp", "humidity", "smoke", "movement"]
        sensor_name = SENSOR_NAMES[random.randint(0,3)]
        if sensor_name = "smoke" or "movement" :
            pass
        
        send_sensor_value(value=sensor_value,user=user_id,sensor_type=sensor_name)
        time.sleep(10)

def send_sensor_value(value,user,sensor_type):
    url = f"http://127.0.0.1:5000/{sensor_type}/{user}"  
    headers = {'Content-Type': 'application/json'}
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {'value': value, 'timestamp': timestamp}

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        print('Sensor value sent successfully')
    else:
        print('Failed to send sensor value. Status code:', response.status_code)

REAL_USER_ID = "-NWbwVCkDBhq3Q0QGzfk"

simulate_sensor(user_id=REAL_USER_ID)
