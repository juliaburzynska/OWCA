import busio
import board
import adafruit_adxl34x
import time


i2c = busio.I2C(board.SCL, board.SDA)

class Accelerometer:
    
    def __init__(self):
        self.sensor = adafruit_adxl34x.ADXL345(i2c)

    def measure(self):
        x_axis = float(self.sensor.acceleration[0])
        y_axis = float(self.sensor.acceleration[1])
        z_axis = float(self.sensor.acceleration[2])
        return [x_axis, y_axis, z_axis]
    

if "__name" == "__main__":
    acc = Accelerometer.measure()
    print(acc) 







    
