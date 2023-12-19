import os
import time

def tagConfig():
   os.system('sudo hciconfig hci0 up')
   time.sleep(0.1)
   os.system('sudo hciconfig hci0 reset')
   time.sleep(0.1)
   os.system('sudo hciconfig hci0 noscan')
   time.sleep(0.1)
   os.system('sudo hciconfig hci0 noleadv')
   time.sleep(0.1)
   os.system('bluetoothctl reset-alias')
   time.sleep(0.1)
   os.system('sudo hcitool -i hci0 cmd 0x03 0x0013 \
     50 42 4C 33 5F 00 01 00 \
     00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \
     00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \
     00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \
     00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \
     00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \
     00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \
     00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \
     00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \
     00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \
     00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \
     00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \
     00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00')
   time.sleep(0.1)
   os.system('sudo hciconfig hci0 reset')
   time.sleep(0.1)
   os.system('sudo hcitool -i hci0 cmd 0x08 0x0005 58 35 33 4C 42 50')
   time.sleep(0.1)
   os.system('sudo hcitool -i hci0 cmd 0x08 0x0006 A0 00 A0 00 03 01 00 11 22 33 44 55 66 07 00')  
   time.sleep(0.1)
   


from owca.sensors.Accelerometer import Accelerometer
from owca.sensors.Magnetometer import Magnetometer
from owca.communication.TagFrame import TagFrame
from owca.communication.BLE_Module import BLE_Module



if __name__ == "__main__":

  tagConfig()

  # Set id in range 0 - 65535
  id = '1'
  id = hex(int(id))[2:].zfill(4)
  id = ' '.join(id[i:i+2] for i in range(0, len(id), 2))

  pack_num = 0
  accelerometer = Accelerometer()
  magnetometer = Magnetometer()
  beacon = BLE_Module(id)


  while True:
      acc = accelerometer.measure()
      dir = magnetometer.measure()

      tagFrame = TagFrame(pack_num, acc, dir)
      beacon.transmit(tagFrame.toHex())
      pack_num = (pack_num + 1)%256
