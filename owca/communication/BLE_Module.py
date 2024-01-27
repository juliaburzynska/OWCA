import sys
import bluetooth._bluetooth as bluez
import os
import time
import struct


class BLE_Module:

    def __init__(self, id):
        self.id = id

    def transmit(self, Hex_Frame):
        Beacon = f"sudo hcitool -i hci0 cmd 0x08 0x0008 18 08 09 50 42 4c 33 5f {self.id} 0E 1F {Hex_Frame}"
        os.system(Beacon)
        time.sleep(0.1)
        os.system('sudo hcitool -i hci0 cmd 0x08 0x000A 01')
        time.sleep(0.1)

    @staticmethod
    def receive(sock):
        cmd_pkt = struct.pack("<BB", 0x01, 0x00)
        bluez.hci_send_cmd(sock, 0x08, 0x000c, cmd_pkt)

        flt = bluez.hci_filter_new()
        bluez.hci_filter_all_events(flt)
        bluez.hci_filter_set_ptype(flt, bluez.HCI_EVENT_PKT)
        sock.setsockopt( bluez.SOL_HCI, bluez.HCI_FILTER, flt )

        packet = sock.recv(255)

        if sys.version_info > (3, 0):
            dataString =  ''.join('%02x' % struct.unpack("B", bytes([x]))[0] for x in packet)
        else:
            dataString =  ''.join('%02x' % struct.unpack("B", x)[0] for x in packet)

        if dataString[32:42] == '50424c335f':
            #print(dataString)

            Tag_Frame_Data = dataString[50:62]

            Device_ID = dataString[42:46]
            Rx_Power = str((256 - int(dataString[-2:], 16)))

            return [Tag_Frame_Data, Device_ID, Rx_Power]
