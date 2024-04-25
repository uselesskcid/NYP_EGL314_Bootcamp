import subprocess
import time 
import pythonosc

def run_command(command):
    text = 'python3 command.py'
    config = text + command
    print(config)
    try:
        output = subprocess.check_output(config, shell=True)
        print(output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.returncode}, {e.output.decode('utf-8')}")

def run_recall(command):
    text = 'python3 recall.py '
    config = text + command
    print(config)
    try:
        output = subprocess.check_output(config, shell=True)
        print(output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.returncode}, {e.output.decode('utf-8')}")
    
def fader(IP, PORT, x, y):
    if 0 <= x <= 31 and 0 <= y <= 100:
        command = f"set MIXER:Current/InCh/Fader/Level {str(x)} 0 {str(y)}"
        run_command(command)
    else:
        print("Invalid x or y value for fader function.")
def mute(IP, PORT, x, y=0):  # y is optional and set to 0 as default
    if 0 <= x <= 31:
        command = f"set MIXER:Current/InCh/Fader/Off {str(x)} 0"
        run_command(command)
    else:
        print("Invalid x value for mute function.")

def Unmute(IP, PORT, x, y=1):  # y is optional and set to 0 as default
    if 0 <= x <= 31:
        command = f"set MIXER:Current/InCh/Fader/On {str(x)} 1"
        run_command(command)
    else:
        print("Invalid x value for Unmute function.")
def Pan(IP, PORT, x, y):
    if 0 <= x <= 31 and --63 <= y <= 63:
        command = f"set MIXER:Current/InCh/Fader/Pan {str(x)} 0 {str(y)}"
        run_command(command)
    else:
        print("Invalid x or y value for Pan function.")

if __name__ == "__main__":
    IP = "192.168.254.197"  # Listen on all available network interfaces
    PORT = 1234  # Choose a port number