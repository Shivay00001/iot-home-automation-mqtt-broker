import socket
import time
import random

def run_simulation():
    # Connect to local broker
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(('127.0.0.1', 1883))
    except ConnectionRefusedError:
        print("❌ Cannot connect to broker. Run 'python src/broker.py' first.")
        return

    # Send CONNECT packet
    # Fixed: 0x10, Len: 12, ProtoName: MQTT...
    connect_packet = b'\x10\x0C\x00\x04MQTT\x04\x02\x00\x3C\x00\x00'
    s.send(connect_packet)
    
    # Wait for CONNACK
    resp = s.recv(4)
    if resp[0] == 0x20 and resp[1] == 0x02:
        print("✅ Connected to MQTT Broker!")
    
    # Publish Loop
    try:
        while True:
            temp = 20.0 + random.uniform(-2, 5)
            payload = f"{temp:.1f}".encode()
            topic = b"home/livingroom/temp"
            
            # PUBLISH Packet construction (Simplified)
            # Type 3 (0x30), Len = 2 (topic len) + len(topic) + len(payload)
            remaining_len = 2 + len(topic) + len(payload)
            
            header = bytes([0x30, remaining_len])
            topic_len_bytes = bytes([0x00, len(topic)])
            
            packet = header + topic_len_bytes + topic + payload
            s.send(packet)
            
            print(f"📤 Sent {temp:.1f}°C to {topic.decode()}")
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("Stopping device.")
        s.close()

if __name__ == "__main__":
    run_simulation()
