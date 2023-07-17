import sys

from PySide2.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QMessageBox

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
matplotlib.use('Qt5Agg')

class FunctionPlotterView:
    def __init__(self , app):
        self.app = app

    def setup(self , controller):
        self.window = QMainWindow()
        self.window.setWindowTitle("Function Plotter")
        self.function_label = QLabel("Enter a function")
        self.function_input = QLineEdit()
        self.min_x_label = QLabel("Enter Min x Value")
        self.min_x_input = QLineEdit()
        self.max_x_label = QLabel("Enter Max x Value")
        self.max_x_input = QLineEdit()
        self.plot_button = QPushButton('Plot')

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.plot_button.clicked.connect(controller.plot)

        layout = QVBoxLayout()
        layout.addWidget(self.function_label)
        layout.addWidget(self.function_input)
        layout.addWidget(self.min_x_label)
        layout.addWidget(self.min_x_input)
        layout.addWidget(self.max_x_label)
        layout.addWidget(self.max_x_input)
        layout.addWidget(self.plot_button)
        layout.addWidget(self.canvas)
        widget = QWidget()
        widget.setLayout(layout)
        self.window.setCentralWidget(widget)
        
    
    def start_app(self):
        self.window.show()
        sys.exit(self.app.exec_())
    
    def show_error_window(self , window_title,error_message):
        QMessageBox.critical(self.window , window_title , error_message)
    
    def show_plot(self , x , y , title):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(x, y)
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.set_title(title)
        ax.grid(True)
        self.canvas.draw()