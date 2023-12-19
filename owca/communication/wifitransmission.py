import socket
from anchorframe import AnchorFrame


class WiFiTransmission:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def transmit(self, anchorFrame):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.sendto(anchorFrame.to_json().encode('utf-8'), (self.ip, int(self.port)))
       
    def receive(self):
       with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
           sock.bind((self.ip, self.port))
           data, addr = sock.recvfrom(1024)
           return AnchorFrame.from_json(data.decode('utf-8'))
               