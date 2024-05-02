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
