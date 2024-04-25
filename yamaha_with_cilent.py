from pythonosc import udp_client
import time

# Define the OSC client
def send_message(receiver_ip, receiver_port, address, message):
    try:
        client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
        client.send_message(address, message)
        print("Message sent successfully.")
    except Exception as e:
        print(f"Error: {e}")
        print("Message not sent")

# Define the ranges for x and y
X_RANGE = range(0, 31)  # Channels 0 to 31
Y_RANGE_LEVEL = range(-32768, 1000)  # Level range from -32768 to 1000
Y_RANGE_ON_OFF = range(0, 1)  # ON: 1, OFF: 0
Y_RANGE_PAN = range(-63, 63)  # Pan range from -63 (Left) to 63 (Right)

#Define QL1_IP and QL1_Port
QL1_IP = '192.168.0.128'
QL1_Port = 49280

def set_fader_level(x, y):
    if x not in X_RANGE or y not in Y_RANGE_LEVEL:
        print("Invalid values for x or y.")
        return
    send_message(QL1_IP, QL1_Port, "/set_fader_level", x, y)  # Replace with Yamaha IP address and port

def set_fader_on_off(x, y):
    if x not in X_RANGE or y not in Y_RANGE_ON_OFF:
        print("Invalid values for x or y.")
        return
    send_message(QL1_IP, QL1_Port, "/set_fader_on_off", x, y)  # Replace with Yamaha IP address and port

def set_pan(x, y):
    if x not in X_RANGE or y not in Y_RANGE_PAN:
        print("Invalid values for x or y.")
        return
    send_message(QL1_IP, QL1_Port, "/set_pan", x, y)  # Replace with Yamaha IP address and port
