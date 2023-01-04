import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton
from ex import Fixture
from weather import WeatherTable
from fetchdata import fetchBot
from PyQt5.QtCore import QTimer
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
      
        self.setWindowTitle("data acquisiton")
        self.setGeometry(100, 100, 640, 480)
        
  
        button = QPushButton("weather", self)
        button.move(50, 50)
        button1 = QPushButton("Fixture", self)
        button.move(100, 100)
        
      
        button.clicked.connect(self.redirect)
        button1.clicked.connect(self.redirect1)
        
      
        self.show()
    
    def redirect(self):
      
        self.secondWindow = WeatherTable()
        self.secondWindow.setGeometry(200,200,1920,1080)
        self.secondWindow.show()
    def redirect1(self):
       
        self.thirdWindow = Fixture()
        
       
        
try:
    fetchBot()
except:
    pass    

app = QApplication(sys.argv)  

main = MainWindow()

main.show()
try:
    timer = QTimer()
    timer.timeout.connect(fetchBot)
    timer.start(3000)
except:
    pass    
sys.exit(app.exec_())



