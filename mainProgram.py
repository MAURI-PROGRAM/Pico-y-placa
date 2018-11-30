from objectCar import Car
from datetime import datetime,time
import re

print('\t*********************************************************')
print('\t* this program simulates a predictor of "pico y placa"  *')
print('\t*********************************************************\n')

alertMensaje = 'format of date incorrect'
tryMensaje = 'Try introduce again, check the format'
joinMensaje = alertMensaje+'\n'+tryMensaje+'\n'

#Introduce the date and validation
while True:
    date_str = input("Introduce the date whit the follow format  aaaa-mm-dd  example 2018-11-30 \n")
    try:
        datetime.strptime(date_str, '%Y-%m-%d').date()
        validationDate = True
    except:
        validationDate = False
        print(joinMensaje)
        pass
    if(validationDate):
        break

#Introduce the date and validation
while True:
    time_str = input("Introduce the time whit the follow format  hh:mm:ss  example 11:32:22 \n")
    try:
        datetime.strptime(time_str,"%X").time()
        validationDate = True
    except:
        validationDate = False
        print(joinMensaje)
        pass
    if(validationDate):
        break

#Introduce the date and validation
while True:
    licPlatenum = input("Introduce the date whit the follow format {leter-number} XXX-#### or XXX-###  example ABC-1234 \n")
    patron = re.compile('[A-Za-z]{3}[-][1-9]{3,4}$')
    matcher = patron.match(licPlatenum)
    validationPlate = True
    if matcher is None:
        validationPlate = False
        print(joinMensaje)
    if(validationPlate):
        break




