Fan Automation: IoT for Home
Author: Joshua Hemingway
Date: April 22, 2021

Overview
Fan Automation is an IoT-based solution designed to automate fan control in homes based on various environmental factors like temperature and humidity. The project aims to address the problem of inefficient cooling during hot summer days by providing an automated solution that optimizes fan usage, thus reducing electricity wastage.

Initial Problem
During the summer, many people rely on air conditioning to lower the temperature inside their homes. However, on particularly hot days, air conditioning alone may not be effective. Introducing fans can provide additional cooling, but manually controlling them can be cumbersome and wasteful. Users often leave fans running continuously, leading to unnecessary electricity consumption.

Project Design
The project's design revolves around automatically powering fans located in the user's home whenever a temperature sensor detects that the room is above a specific threshold. The fan will continue to run until the room temperature drops below the specified threshold. Additionally, the system will incorporate features such as automatically turning off the fan at night and considering humidity levels, as high humidity can reduce the effectiveness of fans. Weather data will also be accessed to determine the best times to activate or deactivate the fan.

How it Makes Use of the Internet
SONOFF S31 Lite Zigbee Smart Plug: Enables remote control of the fan across the network.
Accessing Temperature/Humidity Database: Utilizes a DHT 11 temperature/humidity sensor to gather environmental data.
Accessing Global Time: Determines optimal times to turn off the device based on user sleep patterns.
Accessing Weather Data: Predicts the best times to activate or deactivate the fan based on weather conditions.
Challenges
Understanding the functionality of the DHT 22 temperature/humidity sensor and coding a program to interact with it.
Configuring a Zigbee bridge to enable communication with the SONOFF S31 Lite Zigbee Smart Plug.
Utilizing API data to determine the most suitable times to operate the fan.
Circuit/Schematic Diagram
[Insert Circuit/Schematic Diagram Here]

Parts List
1x DHT 11 temperature/humidity sensor
1x SONOFF S31 Lite Zigbee smart plug
1x Fan
1x CC2531 adapter to create a ZigBee bridge
1x LCD1602
1x 5k resistor (10k resistor can also be used)
1x LED
Project Setup - Dependencies
Zigbee2mqtt Dependencies
Before configuring the program, several dependencies need to be downloaded to the Raspberry Pi:

Zigbee2mqtt: Follow the steps outlined on the Zigbee2mqtt website for installation and setup.
Mosquitto: Install Mosquitto, the MQTT broker, using the command sudo apt-get install mosquitto.
Dependencies for Sending Messages to IoT Devices with Python
Update the ~/.bashrc file to reflect Python 3.7 as the default Python version.

bash
Copy code
curl -O https://bootstrap.pypa.io/get-pip.py
sudo python3.7 get-pip.py
pip install paho-mqtt
Dependencies for DHT11
Install Adafruit_DHT, which is used to interface with the DHT 11 temperature/humidity sensor.

bash
Copy code
sudo pip install Adafruit_DHT
