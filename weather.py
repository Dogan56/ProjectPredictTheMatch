import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem,QLineEdit
import json
from PyQt5.QtCore import Qt
from datetime import datetime

class WeatherTable(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather")
        self.setGeometry(200, 200, 1920, 1080)
      
        self.table = QTableWidget(self)
        
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["City", "Temperature", "Feels Like", "Pressure", "Humidity", "Description","Time"])
        self.setCentralWidget(self.table)
        self.table.setGeometry(20,0,500,500)
        
        self.city_input = QLineEdit(self)
        self.city_input.move(10, 10)
        
        self.city_input.returnPressed.connect(self.filter_by_city)
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        
    def populate_table(self):
        path = r"app\weather.json"
        with open(path,"r") as f:
            data = json.load(f)
        for city_data in data:
            city, forecast_data = city_data
            for i, period in enumerate(forecast_data["list"]):
                time = datetime.fromtimestamp(period["dt"])
                self.table.setItem(i, 0, QTableWidgetItem(city))
           
                self.table.setItem(i, 1, QTableWidgetItem(str(period["main"]["temp"])))
            
                self.table.setItem(i, 2, QTableWidgetItem(str(period["main"]["feels_like"])))
            
                self.table.setItem(i, 3, QTableWidgetItem(str(period["main"]["pressure"])))
       
                self.table.setItem(i, 4, QTableWidgetItem(str(period["main"]["humidity"])))
        
                self.table.setItem(i, 5, QTableWidgetItem(period["weather"][0]["description"]))
                self.table.setItem(i, 6, QTableWidgetItem(str(time)))
    def filter_by_city(self):
        city_name = self.city_input.text()
        self.table.clear()
        
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["City", "Temperature", "Feels Like", "Pressure", "Humidity", "Description","Time"])
        path = r"app/weather.json"
        with open(path,"r") as f:
            data = json.load(f)
            city_data = []
            x = 0
            a = 0
            myData = []
            while x<len(data):
                
                if(list(data[x].keys())[0] == city_name):
                    city_data.append(data[x][city_name])
                    a+=1
                           
                x+=1
            self.table.setRowCount(24*a)        
            myData = []

            for i in city_data:
                myData.append({city_name:i})
            myData = reversed(myData)    
            
            if city_data:
                i = 0
                for x in myData:
                   forecast_data = x[city_name] 
                   
                   for c, period_data in enumerate(reversed(forecast_data["list"])):
                    time = datetime.fromtimestamp(period_data["dt"])
                    self.table.setItem(i, 0, QTableWidgetItem(city_name))
                    self.table.setItem(i, 1, QTableWidgetItem(str(period_data["main"]["temp"])))
                    self.table.setItem(i, 2, QTableWidgetItem(str(period_data["main"]["feels_like"])))
                    self.table.setItem(i, 3, QTableWidgetItem(str(period_data["main"]["pressure"])))
                    self.table.setItem(i, 4, QTableWidgetItem(str(period_data["main"]["humidity"])))
                    self.table.setItem(i, 5, QTableWidgetItem(period_data["weather"][0]["description"]))
                    self.table.setItem(i, 6, QTableWidgetItem(str(time)))
                    i+=1
                   
    
            


