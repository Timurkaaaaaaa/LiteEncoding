import sys
from PyQt5 import QtWidgets
from ui import Ui_LiteEncoding
import base64

class MainApp(QtWidgets.QMainWindow, Ui_LiteEncoding):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.EncodeASCII16.clicked.connect(self.encode_ascii16)
        self.EncodeASCII10.clicked.connect(self.encode_ascii10)
        self.EncodeASCII2.clicked.connect(self.encode_ascii2)
        self.EncodeBASE64.clicked.connect(self.encode_base64)
        self.DecodeASCII16.clicked.connect(self.decode_ascii16)
        self.DecodeASCII10.clicked.connect(self.decode_ascii10)
        self.DecodeASCII2.clicked.connect(self.decode_ascii2)
        self.DecodeBASE64.clicked.connect(self.decode_base64)

    def encode_ascii16(self):
        input_text = self.InputText.toPlainText()
        self.OutputText.setText(input_text.encode("windows-1251", "replace").hex())

    def encode_ascii10(self):
        input_text = self.InputText.toPlainText()
        encoded_bytes = input_text.encode('windows-1251')
        output_string = ''.join(str(byte) for byte in encoded_bytes)
        self.OutputText.setText(output_string)

    def encode_ascii2(self):
        input_text = self.InputText.toPlainText()
        encoded_bytes = input_text.encode('windows-1251')
        binary_string = ''.join(format(byte, '08b') for byte in encoded_bytes)
        self.OutputText.setText(binary_string)

    def encode_base64(self):
        input_text = self.InputText.toPlainText()
        data_bytes = input_text.encode('utf-8')
        encoded_data = base64.b64encode(data_bytes)
        encoded_string = encoded_data.decode('utf-8')
        self.OutputText.setText(encoded_string)

    def decode_ascii16(self):
        hex_input = self.InputText.toPlainText()
        bytes_object = bytes.fromhex(hex_input)
        decoded_string = bytes_object.decode('windows-1251')
        self.OutputText.setText(decoded_string)


    def decode_ascii10(self):
        input = self.InputText.toPlainText()
        byte_values = [int(input[i:i + 3]) for i in range(0, len(input), 3)]
        decoded_string = bytes(byte_values).decode('windows-1251')
        self.OutputText.setText(decoded_string)

    def decode_ascii2(self):
        binary_string = self.InputText.toPlainText()

        bytes_list = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
        byte_array = bytearray(int(byte, 2) for byte in bytes_list)
        decoded_string = byte_array.decode('windows-1251')

        self.OutputText.setText(decoded_string)

    def decode_base64(self):
        input_text = self.InputText.toPlainText()
        decoded_data = base64.b64decode(input_text)
        decoded_string = decoded_data.decode('utf-8')
        self.OutputText.setText(decoded_string)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
