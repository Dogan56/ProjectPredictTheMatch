import sys
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem,QMainWindow
from table import getdata


class Fixture(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(200, 200, 1920, 1080)
        self.table = QTableWidget()
        self.table_data = getdata()[1]
        self.table_header = getdata()[0]
        self.num_rows = len(self.table_data)
        self.num_columns = len(self.table_data[0])
        self.table.setRowCount(self.num_rows)
        self.table.setColumnCount(self.num_columns)
        self.Fixture()
    def Fixture(self):
        for i, header in enumerate(self.table_header):
            item = QTableWidgetItem(header)
            self.table.setHorizontalHeaderItem(i, item)
        for i in range(self.num_rows):
            for j in range(self.num_columns):
                item = QTableWidgetItem(str(self.table_data[i][j]))
                self.table.setItem(i, j, item)
        self.table.setGeometry(200,200,1920,1080)
        self.table.setWindowTitle("Fixture")
        self.table.show()
              