import time
from datetime import datetime
from flask import Flask, render_template, request

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, GPIO.LOW)




app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
return app.send_static_file('switch.html')

@app.route('/Garage', methods=['GET', 'POST'])
def Garage():
        name = request.form['garagecode']
        if name == '0' and GPIO.output(7) == GPIO.LOW:  # 12345678 is the Password that Opens Garage Door (Code if Password is Correct)
                GPIO.output(7, GPIO.HIGH)
        else GPIO.output(7, GPIO.LOW)
               
        

@app.route('/stylesheet.css')
def stylesheet():
        return app.send_static_file('stylesheet.css')



if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=5000)
