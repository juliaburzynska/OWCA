from Accelerometer import Accelerometer
from Magnetometer import Magnetometer
from communication.TagFrame import TagFrame
from communication.BLE_Module import BLE_Module
from tagconfig import tagConfig

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

