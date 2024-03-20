# Project Owca - Object Localization on Defined Terrain
## Project Description:
Project Owca is a group project in the field of Internet of Things (IoT) at the Warsaw University of Technology. It aims to locate objects on a defined terrain using Bluetooth Low Energy (BLE) Beacon technology and transmitting data over WiFi in UDP format to a server, where the location is determined. The project is implemented on the Raspberry Pi platform.
## Technologies Used:
* bluez
* socket
* Python Programming Language
* Jupyter Notebook

## Setup

To ensure proper functionality on both tag and anchor devices, it's necessary to install the `python3-bluez` package. This package provides Python bindings for the Bluez Bluetooth stack, which is essential for Bluetooth Low Energy (BLE) communication.

#### Installation Instructions:
```bash
sudo apt-get update
sudo apt-get install python3-bluez
```


### File description:
* File tag.py

The `tag.py` file is intended to be run on the device to be located within the Owca project. This script is responsible for initiating the localization process and transmitting data to the server.

##### Required Sensors:

1. **Accelerometer (ACC)**: `tag.py` utilizes an accelerometer to measure the device's acceleration.

2. **Magnetometer**: A magnetometer is also required by `tag.py` to measure the direction and strength of the magnetic field.

##### Execution:

To run `tag.py` on the device, simply invoke it using the Python interpreter:

```bash
sudo python tag.py
```
* File anchor.py
The `anchor.py` file is intended to be run on devices deployed around the localized area. Anchors serve as reference points for determining the precise location of the tagged device.

#### Execution:
Similar to tag.py, you can run anchor.py using the Python interpreter:
```bash
sudo python anchor.py
```
* File server.py
The `server.py` file is run on the server and is responsible for receiving data from anchor devices and processing it to determine the location of the tagged device.

#### Execution:
To run server.py, invoke it using the Python interpreter on the server:
```bash
python server.py
```
