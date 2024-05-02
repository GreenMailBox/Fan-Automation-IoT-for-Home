#Joshua Hemingway
#4/22/2021
#final project
#Fan Automation, IOT for the home

# in order for the program to work you will need to install the following
#modules paho-mqtt, Adafruit_DHT to use with python

#Import neccessary modules
import Adafruit_DHT
import time
import json
import time
import urllib.request
import paho.mqtt.client as mqtt
import I2C_LCD_driver
from gpiozero import Button
from gpiozero import LED
from datetime import datetime

#set global variables
thelcd = I2C_LCD_driver.lcd()
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 19
led16 = LED(16, active_high = False)

timeday = 25
timenight = 25
API = input("api key: ")
zip = input("zip code: ")
preset = input("Preset Temp: ")
onnight = False



#Defining the init values, by default clear lcd, turn off led, and run the API
# as it is assumed first startup there will be new api info
def init():

    #connect to the client which uses port 1883 by default and is called local host
    #when publishing messages 0x00124b00226a68b0 is the device you are sending messages to
    #This will be different for everyone
    #link quality is not necessary for publishing messages, but it doesn't hurt to have
    #state assignments are on off and toggle
    client = mqtt.Client()
    client.connect("localhost",1883,60)
    client.publish("zigbee2mqtt/0x00124b00226a68b0/set", '{"linkquality":107,"state":"OFF"}');
    client.disconnect();

    #clear lcd
    thelcd.lcd_clear()
    led16.off()

    #check and proceed if user wants whitenoise from fan
    night = input("Enter anything if you want to configure fans to be always on at night:")
    if night:
        onnight = True
        nightparam()
    else:
        onnight = False
        getLocation(zip, API)

#Set user parameters for always on times at night
def nightparam():
    global timenight
    global timeday
    timenight = int(input("Enter start time to keep fans on 0-24, military time:"))
    timeday = int(input("Enter end time to keep fans on 0-24, military time:"))
    getLocation(zip, API)

def display(fahrenheit, humidity, maxtemp, mintemp, hotenoughlow, hotenoughhigh):
     #display temperature to display
    fan_control(fahrenheit, humidity, hotenoughlow, hotenoughhigh)

    thelcd.lcd_display_string("Current temp:", 1, 1)
    thelcd.lcd_display_string(str(fahrenheit) + "F", 2, 1)
    time.sleep(2)
    thelcd.lcd_clear()

   #Display humidity percentage to display
    thelcd.lcd_display_string("Humidity :", 1, 1)
    thelcd.lcd_display_string(str(humidity) + "%" , 2, 1)
    time.sleep(2)
    thelcd.lcd_clear()
    #Display max temp summary
    thelcd.lcd_display_string("6 hour max sum : "  , 1, 1)
    thelcd.lcd_display_string(str(maxtemp) + "F", 2, 1)
    time.sleep(2)
    thelcd.lcd_clear()
    #Display min temp summary
    thelcd.lcd_display_string("6 hour Min sum : " , 1, 1)
    thelcd.lcd_display_string(str(mintemp) + "F", 2, 1)
    time.sleep(2)
    thelcd.lcd_clear()
    #Display min temp summary
    thelcd.lcd_display_string("High Real Feel: " , 1, 1)
    thelcd.lcd_display_string(str(hotenoughhigh) + "F", 2, 1)
    time.sleep(2)
    thelcd.lcd_clear()
    #Display min temp summary
    thelcd.lcd_display_string("Low Real Feel: " , 1, 1)
    thelcd.lcd_display_string(str(hotenoughlow) + "F", 2, 1)
    time.sleep(2)
    thelcd.lcd_clear()


#Run API every 4 hours, to update information, also updating
#every 4 hours will prevent going over free trial limit
def runAPI():
    start_time = time.time()
    while True:
        sleep_time = 14400
        if (time.time() - start_time) > sleep_time:
            start_time = time.time()
            getLocation(zip, API)
        else:
            getInfo()

# Get Location ID, based on current ZIP Code
def getLocation(zip, API):
    search_add="http://dataservice.accuweather.com/locations/v1/postalcodes/search?apikey=" + API + "&q=" + zip + '&details=true'
    with urllib.request.urlopen(search_add) as url:
        data = json.loads(url.read().decode())
        f = open("/home/pi/Downloads/accu.tmp","w")
    f.write(json.dumps(data))
    f.close()
    getLocationID()

#Get location key from location information and pass to other API calls
def getLocationID():
    f = open("/home/pi/Downloads/accu.tmp","r")
    data=json.loads(f.read())
    f.close()
    location_key=data[0]['Key']
    getForcast(location_key, API)
    five_day_forcast(location_key, API)

    #get dailyforcast information for location and write to file
def getForcast(location_key, API):
    dailyForcast = "http://dataservice.accuweather.com/currentconditions/v1/" + location_key + "?apikey=" + API + '&details=true'
    with urllib.request.urlopen(dailyForcast) as url:
        data = json.loads(url.read().decode())
        g = open("/home/pi/Downloads/daily.tmp","w")
    g.write(json.dumps(data))
    g.close()
    getInfo()

    #get five day forcast for location, and store to file
def five_day_forcast(location_key, API):
    five_day = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/" + location_key +"?apikey=" + API + '&details=true'
    with urllib.request.urlopen(five_day) as url:
        data = json.loads(url.read().decode())
        i = open("/home/pi/Downloads/five_day.tmp","w")
    i.write(json.dumps(data))
    i.close()
    getInfo()


def getInfo():
    #gather api information from file created
    f = open("/home/pi/Downloads/daily.tmp","r")
    daily=json.loads(f.read())
    f.close()

    g = open("/home/pi/Downloads/five_day.tmp","r")
    fiveday= json.loads(g.read())
    g.close()

    #gather 6 hour summary high temp
    #gather 6 hour summary low temp
    maxtemp=daily[0]['TemperatureSummary']['Past6HourRange']['Maximum']['Imperial']['Value']
    mintemp=daily[0]['TemperatureSummary']['Past6HourRange']['Minimum']['Imperial']['Value']

    #in case we want to grab other forcasts days in future
    #i set it up, as a loop to gather additional day info
    x = 0
    for i in fiveday['DailyForecasts']:
        if x == 0:
            hotenoughlow=i['RealFeelTemperature']['Minimum']['Value']
            hotenoughhigh=i['RealFeelTemperature']['Maximum']['Value']
        x = x + 1
    check_temp(maxtemp, mintemp, hotenoughlow, hotenoughhigh)
    #Control fan based on parameters
def fan_control(fahrenheit, humidity, hotenoughlow, hotenoughhigh):
    now = str(datetime.now())
    compare = (now[-15]) + (now[-14])
    compare = int(compare)
    print(timeday)
    print(timenight)
    #check time of day against user specified always on period
    if timeday is not 25 and timenight <= compare < timeday:
        client = mqtt.Client()
        client.connect("localhost",1883,60)
        client.publish("zigbee2mqtt/0x00124b00226a68b0/set", '{"linkquality":107,"state":"ON"}');
        client.disconnect();
        led16.on()

    # aleviatea the problem where fans wont turn on, if
    # they set start time as a high number/ 22 and end time at 8/ lower number
    if timenight > timeday and timenight >= compare < timeday:
        client = mqtt.Client()
        client.connect("localhost",1883,60)
        client.publish("zigbee2mqtt/0x00124b00226a68b0/set", '{"linkquality":107,"state":"ON"}');
        client.disconnect();
        led16.on()

    # At 95 degrees fans are not effective, thus fan turn off
    elif fahrenheit > 95:
        print("FAN OFF, TEMP TO HOT")
        client = mqtt.Client()
        client.connect("localhost",1883,60)
        client.publish("zigbee2mqtt/0x00124b00226a68b0/set", '{"linkquality":107,"state":"OFF"}');
        client.disconnect();
        led16.off()
    # sources are everywhere based on humidity levels and what is to high
    #highest source said 65, so that is what i will consider to hot for
    #fans to be working properly
    elif int(fahrenheit) > int(preset) and int(humidity) < 65:
        led16.on()
        client = mqtt.Client()
        client.connect("localhost",1883,60)
        client.publish("zigbee2mqtt/0x00124b00226a68b0/set", '{"linkquality":107,"state":"ON"}');
        client.disconnect();
    elif hotenoughhigh > 80 and hotenoughlow > 80:
        client = mqtt.Client()
        client.connect("localhost",1883,60)
        client.publish("zigbee2mqtt/0x00124b00226a68b0/set", '{"linkquality":107,"state":"ON"}');
        client.disconnect();
        led16.on()
    else:
        client = mqtt.Client()
        client.connect("localhost",1883,60)
        client.publish("zigbee2mqtt/0x00124b00226a68b0/set", '{"linkquality":107,"state":"OFF"}');
        client.disconnect();
        led16.off()
    #Gather temperature/Humidity values from sensor conver to F
    #Run API and control fan, with values
def check_temp(maxtemp, mintemp, hotenoughlow, hotenoughhigh):
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None and humidity < 100:
        fahrenheit = int(temperature * 1.8 + 32)
        display(fahrenheit, humidity, maxtemp, mintemp, hotenoughlow, hotenoughhigh)
    else:
        pass


#start program
init()
runAPI()
