class Distance:
    def __init__(self, rssi, prop_const):
        self.rssi = rssi
        self.prop_const = prop_const

    def get(self):
        rssi_base = -50  #power [dBm] at 1m
        s = 1 / (10 ** ((self.rssi - rssi_base) / (10 * self.prop_const)))
        return s
