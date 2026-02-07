import argparse
import asyncio
from src.broker import MQTTBroker

def main():
    parser = argparse.ArgumentParser(description="IoT MQTT Broker")
    parser.parse_args()
    
    broker = MQTTBroker()
    try:
        asyncio.run(broker.start())
    except KeyboardInterrupt:
        print("Broker stopped.")

if __name__ == "__main__":
    main()
