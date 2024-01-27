class FileWriter:
    def __init__(self, path):
        self.file = open(path, "a")
        
    def writeFrame(self, frame):
        self.file.write(frame.to_csv_line() + "\n")
        self.file.flush()