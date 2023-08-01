from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from instr import *
from second_win import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()

    def initUI(self):
        self.btn_next = QPushButton(txt_next)
        self.hello_text = Qlabel(txt_hello)
        self.instruction = Qlabel(txt_instruction)

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.Alignment)
        self.layout_line.addWidget(self.instruction, alignment = Qt.Alignment) 
        self.layout_line.addWidget(self.btn_next, alignment = Qt.Alignment)
        self.setLayout(self.layout_line)

    def next_click(self):
        self.hide()
        self.tw = TestWin()

    def connects(self):
        self.bnt_next.clicked.connect(self.next_click)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

app = QApplication([])
mw = MainWin()
app.exec_()