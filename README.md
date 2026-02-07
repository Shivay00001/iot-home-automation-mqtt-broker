# IoT Home Automation MQTT Broker

[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB.svg)](https://www.python.org/)
[![MQTT](https://img.shields.io/badge/Protocol-MQTT_3.1.1-660066.svg)](http://mqtt.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **production-grade lightweight MQTT Broker** designed for Home Automation networks. This repository implements a custom TCP server capable of handling MQTT CONNECT, PUBLISH, and SUBSCRIBE packets using Python's `asyncio`.

## 🚀 Features

- **AsyncIO Core**: High-concurrency event loop for handling hundreds of IoT devices.
- **Packet Parsing**: Custom decoder for MQTT 3.1.1 fixed headers.
- **Pub/Sub Engine**: Efficient topic matching and message broadcasting.
- **Device Simulator**: Includes a mock Thermostat for testing.

## 📁 Project Structure

```
iot-home-automation-mqtt-broker/
├── src/
│   ├── broker.py         # Async TCP Server
│   ├── device.py         # Mock IoT Device
│   └── main.py           # CLI Entrypoint
├── requirements.txt
└── Dockerfile
```

## 🛠️ Quick Start

```bash
# Clone
git clone https://github.com/Shivay00001/iot-home-automation-mqtt-broker.git

# Run Broker (Port 1883)
python src/broker.py

# In another terminal, run Device
python src/device.py
```

## 📄 License

MIT License
