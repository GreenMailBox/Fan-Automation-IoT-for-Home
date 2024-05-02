# **Fan Automation: IoT for Home**

**Author:** Joshua Hemingway  
**Date:** April 22, 2021  

## **Overview**

**Fan Automation** automates fan control in homes based on temperature and humidity, reducing electricity wastage.

### **Initial Problem**

Hot summer days make air conditioning inefficient. Manual fan control leads to electricity wastage.

### **Project Design**

Automatically powers fans when room temperature exceeds a threshold. Turns off fans when temperature drops. Considers humidity and weather data for optimal operation.

### **How it Uses the Internet**

- **SONOFF S31 Lite Zigbee Smart Plug:** Enables remote fan control.
- **Temperature/Humidity Database:** Uses DHT 11 sensor for data.
- **Global Time:** Turns off fans at night.
- **Weather Data:** Determines ideal fan operation times.

### **Challenges**

- Understanding DHT 22 sensor and coding.
- Configuring Zigbee bridge.
- Using API data for fan control.

## **Circuit/Schematic Diagram **
![image](https://github.com/GreenMailBox/Fan-Automation-IoT-for-Home/assets/80927465/9ed12163-4471-4b0f-854e-e6b3f25b2713)
![image](https://github.com/GreenMailBox/Fan-Automation-IoT-for-Home/assets/80927465/e2ee8a6e-1d16-43f7-8bf5-4865317202c0)

### **Dependencies**

- **Zigbee2mqtt:** Follow [installation guide](https://www.zigbee2mqtt.io/getting_started/running_zigbee2mqtt.html).
- **Mosquitto:** Install MQTT broker with `sudo apt-get install mosquitto`.
- **Python Dependencies:**
  ```bash
  curl -O https://bootstrap.pypa.io/get-pip.py
  sudo python3.7 get-pip.py
  pip install paho-mqtt
  pip install Adafruit_DHT
  
### **Parts List**

- **DHT 11 temperature/humidity sensor**
- **SONOFF S31 Lite Zigbee smart plug**
- **Fan**
- **CC2531 adapter**
- **LCD1602**
- **5k resistor** (10k resistor also works)
- **LED**

### **Algorithm Description**

Below is a list of functions discussing what will be accomplished with our program:

1. **Obtaining User Input:** A Python function obtains user input for the temperature at which they would like to keep the fan on. This includes settings for always-on mode at night and usual hours when the user is sleeping or not at home.

2. **Fan Activation based on Environmental Data:** A Python function takes humidity and temperature measurements from the DHT22 sensor, compares them with the user-inputted parameters, and remotely turns on the fan when necessary.

3. **Displaying Environmental Data:** A Python function displays the current temperature and humidity on the LCD screen, along with other important information such as the duration the fan has been on.

After setting up automatic fan control based on user parameters, we can integrate AccuWeather's API data:

1. **Location Identification:** A Python function takes a zip code and API key and returns the location ID as a string for that zip code.

2. **Current Conditions Retrieval:** A Python function takes the location ID and API key, returning the current weather conditions as a Python list for later parsing.

3. **Past 24 Hours Conditions Retrieval:** A Python function takes the location ID and API key, returning the conditions from the past 24 hours as a Python list for later parsing.

Once AccuWeather's API data is ready for parsing, we can enhance our program further:

1. **Forecast Data Parsing:** A Python function detects forecast data, checks the minimum/maximum temperatures over the past 6 hours, and displays them.

2. **Forecasted High and Low Temperature Display:** A Python function detects forecast data for the current day, displaying the forecasted high and low temperatures. If both temperatures are above 80°F, the fan will be on throughout the day regardless of the indoor temperature.
