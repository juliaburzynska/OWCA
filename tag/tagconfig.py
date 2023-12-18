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
   