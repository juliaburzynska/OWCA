from qmc5883l import py_qmc5883l


class Magnetometer:
    def __init__(self):
        self.sensor = py_qmc5883l.QMC5883L()
        
    def measure(self):
        return self.sensor.get_bearing()
        
    
        

