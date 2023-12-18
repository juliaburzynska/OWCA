class Server:
    def __init__(self, wifi, fileWriter):
        self.wifi = wifi
        self.fileWriter = fileWriter
        
    def run(self):
        self.fileWriter.file.write("anchorID, rssi, tagID, ts, packNum, acc[0], acc[1], acc[2], dir\n")
        while True:
            anchorframe = self.wifi.receive()
            self.fileWriter.writeFrame(anchorframe)
  
