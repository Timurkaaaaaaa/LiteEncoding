import sys
from PyQt5 import QtWidgets
from ui import Ui_LiteEncoding

class MainApp(QtWidgets.QMainWindow, Ui_LiteEncoding):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Подключение кнопок к методам
        self.EncodeASCII16.clicked.connect(self.encode_ascii16)
        self.EncodeASCII10.clicked.connect(self.encode_ascii10)
        self.EncodeASCII2.clicked.connect(self.encode_ascii2)
        self.EncodeBASE64.clicked.connect(self.encode_base64)
        self.DecodeASCII16.clicked.connect(self.decode_ascii16)
        self.DecodeASCII10.clicked.connect(self.decode_ascii10)
        self.DecodeASCII2.clicked.connect(self.decode_ascii2)
        self.DecodeBASE64.clicked.connect(self.decode_base64)

    def encode_ascii16(self):
        input_text = self.InputText.toPlainText()  # Получаем текст из многострочного поля
        self.OutputText.setText(input_text.encode("windows-1251", "replace").hex())

    def encode_ascii10(self):
        print("Нажата кнопка Encode ASCII (decimal)")

    def encode_ascii2(self):
        print("Нажата кнопка Encode ASCII (binary)")

    def encode_base64(self):
        print("Нажата кнопка Encode BASE64")

    def decode_ascii16(self):
        print("Нажата кнопка Decode ASCII (hexadecimal)")

    def decode_ascii10(self):
        print("Нажата кнопка Decode ASCII (decimal)")

    def decode_ascii2(self):
        print("Нажата кнопка Decode ASCII (binary)")

    def decode_base64(self):
        print("Нажата кнопка Decode BASE64")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
