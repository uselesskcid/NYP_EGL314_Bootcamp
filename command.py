import sys
import socket

# Host is console's IP
host = "192.168.0.128"
# Port must be 49280
port = 49280

# create command
args = sys.argv
args.pop(0)
command = ''
for tmp in args:
    if command != '':
        command += ' '
    command += tmp
command += '\n'

print(f"Sending command: {command}")  # Add this line to print the command being sent

# connect socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
s.connect((host, port))

# send command
s.sendall(command.encode())

# receive a message before closing socket
received_data = s.recv(1500)
print(f"Received data: {received_data}")  # Add this line to print received data

# close socket
s.close()