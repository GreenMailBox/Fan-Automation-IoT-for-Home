# Fan-Automation-IoT-for-Home
Fan Automation: IoT for Home
Author: Joshua Hemingway
Date: April 22, 2021

Overview
Fan Automation is an IoT-based solution designed to automate fan control in homes based on various environmental factors like temperature and humidity. This tool utilizes a combination of hardware components including temperature and humidity sensors along with software functionalities to control fans accordingly.

Installation
To use Fan Automation, you'll need to install the following modules:

paho-mqtt
Adafruit_DHT
You can install these modules via pip:
pip install paho-mqtt Adafruit_DHT
Clone the repository:
git clone https://github.com/yourusername/Fan-Automation.git
Navigate to the project directory:
cd Fan-Automation

Run the program:
python fan_automation.py
Follow the on-screen instructions to input necessary parameters such as API key, ZIP code, and preset temperature.

Functionality
Fan Automation operates as follows:

It retrieves environmental data such as temperature and humidity from sensors.
It fetches weather forecast data using the AccuWeather API based on the provided ZIP code.
Based on the collected data, it controls the state of the fan (ON/OFF) using MQTT protocol.
The program runs continuously, updating data and controlling the fan as per the predefined parameters.
Additional Notes
The program includes an option to configure the fan to be always on during specific times at night.
Ensure that the necessary hardware components such as temperature and humidity sensors are properly connected to the system.
Make sure to provide accurate API keys and ZIP codes for precise weather data retrieval.
Contributions
Contributions to this project are welcome. Feel free to submit bug reports, feature requests, or pull requests via GitHub.

License
Fan Automation is licensed under the GNU General Public License (GPL). See LICENSE for more details.

Make sure to create a file named LICENSE in your project directory and include the text of the GNU GPL license or a reference to it.
