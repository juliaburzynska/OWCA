import bluetooth._bluetooth as bluez
from owca.communication.BLE_Module import BLE_Module
import sys
from owca.communication.TagFrame import TagFrame
from owca.communication.anchorframe import AnchorFrame
from owca.communication.wifitransmission import WiFiTransmission
from datetime import datetime

try:
        sock = bluez.hci_open_dev()
except:
        print ("Error accessing bluetooth")
        
ip = '192.168.211.160'
port = 8888
anchorID = 1


while True:
    try:
        Frame = BLE_Module.receive(sock)
        if Frame != None:
            tagHex = Frame[0]
            tagID = Frame[1]
            rssi = Frame[2]
            tagFrame = TagFrame.fromHex(tagHex)
            wifi = WiFiTransmission(ip, port)
            print(wifi.ip)
            dt = datetime.now()
            ts = datetime.timestamp(dt)
            anchor = AnchorFrame(tagFrame, anchorID, rssi, tagID, ts)
            wifi.transmit(anchor)            
            
    except KeyboardInterrupt:
        sys.exit()
    except Exception:
          pass
