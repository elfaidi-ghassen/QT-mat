from PyQt5.uic import *
from PyQt5.QtWidgets import *
from numpy import *

def calc():
  mat_a = [
    [w.A1.text(), w.A2.text(), w.A3.text()],
    [w.A4.text(), w.A5.text(), w.A6.text()],
    [w.A7.text(), w.A8.text(), w.A9.text()]
  ]
  mat_b = [
    [w.B1.text(), w.B2.text(), w.B3.text()],
    [w.B4.text(), w.B5.text(), w.B6.text()],
    [w.B7.text(), w.B8.text(), w.B9.text()]
  ]

  res = array([[0]*3] * 3)
  for i in range(3): # Col Matrice B
    for j in range(3): # l Matrice B
      val = 0
      for k in range(3):
        val = val + int(mat_a[j][k]) * int(mat_b[k][i])
      res[j][i] = val

  table = w.res
  table.setRowCount(3)
  table.setColumnCount(3)
  for i in range(3):
    for j in range(3):
       table.setItem(i, j, QTableWidgetItem(str(res[i][j])))

app = QApplication([])
w = loadUi("interface.ui")
w.show()
w.BTN.clicked.connect(calc)
app.exec_()
