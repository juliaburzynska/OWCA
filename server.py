from owca.communication.wifitransmission import WiFiTransmission
from owca.file.filewriter import FileWriter
from datetime import datetime



class Server:
    def __init__(self, wifi, fileWriter):
        self.wifi = wifi
        self.fileWriter = fileWriter
        
    def run(self):
        self.fileWriter.file.write("anchorID, rssi, tagID, ts, packNum, acc[0], acc[1], acc[2], dir\n")
        while True:
            anchorframe = self.wifi.receive()
            self.fileWriter.writeFrame(anchorframe)
  


if __name__ == '__main__':
    time = datetime.now().strftime(%Y_%m_%d_%H;%M;%S)
    wifi = WiFiTransmission('0.0.0.0', 8888)
    fileWriter = FileWriter("data\\received_data" + time + ".csv")
    server = Server(wifi, fileWriter)
    server.run()

