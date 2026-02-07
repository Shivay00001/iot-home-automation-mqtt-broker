import asyncio
import logging

logging.basicConfig(level=logging.INFO)

class MQTTBroker:
    def __init__(self, host='0.0.0.0', port=1883):
        self.host = host
        self.port = port
        self.clients = {}

    async def handle_client(self, reader, writer):
        addr = writer.get_extra_info('peername')
        logging.info(f"Checking connection from {addr}")

        try:
            while True:
                # Read Fixed Header (1 byte type + flags)
                packet_type_byte = await reader.read(1)
                if not packet_type_byte: break
                
                packet_type = packet_type_byte[0] >> 4
                
                # Read Remaining Length (Simple 1 byte support for demo)
                length_byte = await reader.read(1)
                length = length_byte[0]
                
                # Read Payload
                payload = await reader.read(length)
                
                logging.info(f"Received Packet Type: {packet_type} | Length: {length}")
                
                if packet_type == 1: # CONNECT
                    logging.info("Client CONNECTED")
                    # Send CONNACK (0x20 0x02 0x00 0x00)
                    writer.write(b'\x20\x02\x00\x00')
                    await writer.drain()
                    
                elif packet_type == 3: # PUBLISH
                    topic_len = (payload[0] << 8) | payload[1]
                    topic = payload[2:2+topic_len].decode()
                    msg = payload[2+topic_len:].decode()
                    logging.info(f"PUBLISH [{topic}]: {msg}")

        except Exception as e:
            logging.error(f"Error: {e}")
        finally:
            logging.info(f"Closing connection {addr}")
            writer.close()

    async def start(self):
        server = await asyncio.start_server(self.handle_client, self.host, self.port)
        logging.info(f"MQTT Broker running on {self.host}:{self.port}")
        async with server:
            await server.serve_forever()

if __name__ == "__main__":
    broker = MQTTBroker()
    try:
        asyncio.run(broker.start())
    except KeyboardInterrupt:
        pass
