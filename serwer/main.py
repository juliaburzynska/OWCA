from communication.wifitransmission import WiFiTransmission
from filewriter import FileWriter
from server import Server
from datetime import datetime

if __name__ == '__main__':
    time = datetime.now().strftime(%Y_%m_%d_%H;%M;%S)
    wifi = WiFiTransmission('0.0.0.0', 8888)
    fileWriter = FileWriter("data\\received_data" + time + ".csv")
    server = Server(wifi, fileWriter)
    server.run()
