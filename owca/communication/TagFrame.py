class TagFrame:
    def __init__(self, pack_num: int, acc, dir):
        self.pack_num = pack_num
        self.acc = acc
        self.dir = dir

    def to_csv_line(self):
        return f"{self.pack_num}, {self.acc[0]}, {self.acc[1]}, {self.acc[2]}, {self.dir}"

    def toHex(self):
        Hex_message = "11"
        bin_pack = bin(self.pack_num)[2:].zfill(8)
        Hex_message =Hex_message + bin_pack
        for i in range(0,3):
            hex_value = bin(round(self.acc[i] / 0.0392266) + 512)[2:].zfill(10)
            Hex_message = Hex_message + hex_value

        hex_value = bin(round(self.dir*10))[2:].zfill(16)
        Hex_message = Hex_message + hex_value
        Hex_message = hex(int(Hex_message, 2))[2:]
        Hex_message = (' '.join(Hex_message[i:i+2] for i in range(0, len(Hex_message), 2))).strip()
        return Hex_message

    @staticmethod
    def fromHex(hex_string):
        remove_spaces = hex_string.replace(" ", "")
        binary_message = bin(int(remove_spaces, 16))[2:]
        temp_binary = binary_message[2:]

        pack_binary = temp_binary[:8]
        acc_binary = temp_binary[8:38]
        dir_binary = temp_binary[38:]

        pack_num = int(pack_binary, 2)

        acc = [
            float(int(acc_binary[i:i + 10], 2) - 512)*0.0392266 for i in range(0, len(acc_binary), 10)
            ]

        dir =float(int(dir_binary, 2)/10)

        return TagFrame(pack_num, acc, dir)
if __name__ == "__main__":
    a = TagFrame(55,[5,5,2],64.1)
    print(a.toHex())
    b = a.toHex()
    print(TagFrame.fromHex(b).pack_num)
    print(TagFrame.fromHex(b).acc)
    print(TagFrame.fromHex(b).dir)
