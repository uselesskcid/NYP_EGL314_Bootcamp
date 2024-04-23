from pythonosc import udp_client

def QL1():
    receive_ip = "192.168.254.184"
    receive_port = 2084
    addr = "/print"
    message = "wassup"
    send_message(receive_ip, receive_port, addr, message)

def MA3():
    receive_ip = "192.168.254.217"
    receive_port = 5101
    addr = "/print"
    message = "wassup2"
    send_message(receive_ip, receive_port, addr, message)

def send_message(receiver_ip, receiver_port, address, message):
    try:
        client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
        client.send_message(address, message)
        print("Message sent successfully.")
    except:
        print("Message not sent")

# FOR INFO: IP address and port of the receiving Raspberry Pi
PI_A_ADDR = "192.168.254.184"  # wlan ip
PORT = 2084

PI_B_ADDR = "192.168.254.217"  # wlan ip
PORT_B = 5101

addr = "/print"
msg = "suppp"
send_message(PI_B_ADDR, PORT_B, addr, msg)
