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
        if GPIO.output(7) == GPIO.HIGH
             print("light is on")
             return app.send_static_file('on.html')
        else:  
             if GPIO.output(7) == GPIO.LOW:
                   print ("light is off")
                   return app.send_static_file('off.html')


@app.route('/Garage', methods=['GET', 'POST'])
def Garage():
        name = request.form['garagecode']
        if name == '12345678':  # 12345678 is the Password that Opens Garage Door (Code if Password is Correct)
                GPIO.output(7, GPIO.LOW)
                time.sleep(1)
                GPIO.output(7, GPIO.HIGH)
                time.sleep(2)

                if GPIO.input(16) == GPIO.HIGH and GPIO.input(18) == GPIO.HIGH:
                  print("Garage is Opening/Closing")
                  return app.send_static_file('Question.html')
                else:
                  if GPIO.input(16) == GPIO.LOW:
                        print ("Garage is Closed")
                        return app.send_static_file('Closed.html')
                  if GPIO.input(18) == GPIO.LOW:
                        print ("Garage is Open")
                        return app.send_static_file('Open.html')

        if name != '12345678':  # 12345678 is the Password that Opens Garage Door (Code if Password is Incorrect)
                if name == "":
                        name = "NULL"
                print("Garage Code Entered: " + name)
                if GPIO.input(16) == GPIO.HIGH and GPIO.input(18) == GPIO.HIGH:
                  print("Garage is Opening/Closing")
                  return app.send_static_file('Question.html')
                else:
                  if GPIO.input(16) == GPIO.LOW:
                        print ("Garage is Closed")
                        return app.send_static_file('Closed.html')
                  if GPIO.input(18) == GPIO.LOW:
                        print ("Garage is Open")
                        return app.send_static_file('Open.html')

@app.route('/stylesheet.css')
def stylesheet():
        return app.send_static_file('stylesheet.css')

@app.route('/Log')
def logfile():
        return app.send_static_file('log.txt')

@app.route('/images/<picture>')
def images(picture):
        return app.send_static_file('images/' + picture)

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=5000)
