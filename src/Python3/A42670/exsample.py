import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import random


class Window(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.figure = plt.figure()
        self.axes = self.figure.add_subplot(111)
        # We want the axes cleared every time plot() is called
        self.axes.hold(False)
        self.canvas = FigureCanvas(self.figure)

        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar.hide()

        # Just some button
        self.button1 = QtWidgets.QPushButton('Plot')
        self.button1.clicked.connect(self.plot)

        self.button2 = QtWidgets.QPushButton('Save')
        self.button2.clicked.connect(self.save)

        # set the layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        btnlayout = QtWidgets.QHBoxLayout()
        btnlayout.addWidget(self.button1)
        btnlayout.addWidget(self.button2)
        qw = QtWidgets.QWidget(self)
        qw.setLayout(btnlayout)
        layout.addWidget(qw)

        self.setLayout(layout)

    def save(self):
        from pathlib import Path
        file_name, _ = QFileDialog.getSaveFileName(self)
        if len(file_name) == 0:
            return
        print(file_name)
        file_name = str(Path(file_name).with_suffix(".png"))
        print(file_name)
        self.figure.savefig(file_name)

    def plot(self):
        ''' plot some random stuff '''
        data = [random.random() for i in range(25)]
        self.axes.plot(data, '*-')
        self.canvas.draw()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())
