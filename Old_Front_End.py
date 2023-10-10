from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QInputDialog, QPushButton, QMainWindow, QLabel, QFileDialog, QApplication, QVBoxLayout, QWidget
import pyqtgraph as pg
from pyqtgraph import PlotWidget
import numpy as np 
import sys
from pyqtgraph import PlotWidget
import pyautogui
from PIL import ImageGrab
import time
import wfdb

class Ui_MainWindow(object):
    


    Snapshots_Count = 0
    def take_snapshot(self):
        #Shortcut to take screenshot
        pyautogui.hotkey("win", "shift", "s")
        #wait till user takes screenshot
        time.sleep(6)
        snapshot = ImageGrab.grabclipboard()    
		# Save the image to Snapshots folder
        snapshot.save(f'Snapshots/image{self.Snapshots_Count}.png', 'PNG')  

    #Browsing Signals Function 
    def Browse_Signals(self):
        File_Path, _ = QFileDialog.getOpenFileName(self.Load_Button, "Browse Signal", "D:\Education\Digital Signal Processing\Tasks\Task 1\Signal-Viewer\Signals", "All Files (*)")
        self.Open_Signal(File_Path)

    #
    def Open_Signal(self,File_Path):
        if File_Path:
         File_Extension = File_Path[-3:]
         X_Axis_Data = None
         Y_Axis_Data = None
        
         if File_Extension == "dat" or File_Extension == "hea" or File_Extension == "atr" :
             Record = wfdb.rdrecord(File_Path[:-4])
             Y_Axis_Data = Record.p_signal[:,0]
             X_Axis_Data = np.arange(len(Y_Axis_Data))

        if Y_Axis_Data is not None:
            self.Start_Plotting(X_Axis_Data, Y_Axis_Data)


             

   




    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1088, 805)
        MainWindow.setStyleSheet("background-color: #1e1e2f;\n" "color:white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(380, 0, 381, 51))
        self.textBrowser.setStyleSheet("border:none;")
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 1061, 481))
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.graphicsView = PlotWidget(self.groupBox)
        self.graphicsView.setGeometry(QtCore.QRect(10, 30, 1031, 151))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = PlotWidget(self.groupBox)
        self.graphicsView_2.setGeometry(QtCore.QRect(10, 250, 1031, 151))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 200, 61, 31))
        self.pushButton.setStyleSheet("background-color:#3366ff;\n" "background-image: \"Assets/zoomin.png\";")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/zoomin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 200, 61, 31))
        self.pushButton_2.setStyleSheet("background-color:#3366ff;")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Assets/zoom-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(510, 430, 101, 31))
        self.pushButton_6.setStyleSheet("background-color:#3366ff;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox)
        self.horizontalSlider.setGeometry(QtCore.QRect(770, 220, 201, 21))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumber.setGeometry(QtCore.QRect(980, 210, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.groupBox)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(770, 440, 201, 21))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumber_2.setGeometry(QtCore.QRect(980, 440, 64, 23))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(820, 200, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(820, 420, 111, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 430, 61, 31))
        self.pushButton_4.setStyleSheet("background-color:#3366ff;\n" "background-image: \"Assets/zoomin.png\";")
        self.pushButton_4.setText("")
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(80, 430, 61, 31))
        self.pushButton_5.setStyleSheet("background-color:#3366ff;")
        self.pushButton_5.setText("")
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(400, 430, 101, 31))
        self.pushButton_7.setStyleSheet("background-color:#3366ff;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_8.setGeometry(QtCore.QRect(390, 200, 101, 31))
        self.pushButton_8.setStyleSheet("background-color:#3366ff;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_9.setGeometry(QtCore.QRect(500, 200, 101, 31))
        self.pushButton_9.setStyleSheet("background-color:#3366ff;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.groupBox)
        self.horizontalScrollBar.setEnabled(False)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(160, 210, 221, 16))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.horizontalScrollBar_2 = QtWidgets.QScrollBar(self.groupBox)
        self.horizontalScrollBar_2.setEnabled(False)
        self.horizontalScrollBar_2.setGeometry(QtCore.QRect(160, 440, 221, 16))
        self.horizontalScrollBar_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_2.setObjectName("horizontalScrollBar_2")
        self.Graph_One_Snapshot_Button = QtWidgets.QPushButton(self.groupBox, clicked=lambda: self.take_snapshot())
        self.Graph_One_Snapshot_Button.setGeometry(QtCore.QRect(610, 200, 101, 31))
        self.Graph_One_Snapshot_Button.setStyleSheet("background-color:#3366ff;")
        self.Graph_One_Snapshot_Button.setObjectName("Graph_One_Snapshot_Button")
        self.Graph_Two_Snapshot_Button = QtWidgets.QPushButton(self.groupBox, clicked=lambda: self.take_snapshot())
        self.Graph_Two_Snapshot_Button.setGeometry(QtCore.QRect(620, 430, 101, 31))
        self.Graph_Two_Snapshot_Button.setStyleSheet("background-color:#3366ff;")
        self.Graph_Two_Snapshot_Button.setObjectName("Graph_Two_Snapshot_Button")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 540, 1061, 211))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 110, 101, 31))
        self.pushButton_11.setStyleSheet("background-color:#3366ff;")
        self.pushButton_11.setObjectName("pushButton_11")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_3.setGeometry(QtCore.QRect(320, 50, 101, 31))
        self.comboBox_3.setStyleSheet("background-color:#3366ff;")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_13.setGeometry(QtCore.QRect(440, 50, 101, 31))
        self.pushButton_13.setStyleSheet("background-color:#3366ff;")
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(420, 20, 111, 16))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(830, 20, 111, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton_19 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_19.setGeometry(QtCore.QRect(320, 100, 101, 31))
        self.pushButton_19.setStyleSheet("background-color:#3366ff;")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_28 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_28.setGeometry(QtCore.QRect(440, 100, 101, 31))
        self.pushButton_28.setStyleSheet("background-color:#3366ff;")
        self.pushButton_28.setObjectName("pushButton_28")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(470, 160, 81, 20))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_34 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_34.setGeometry(QtCore.QRect(880, 100, 101, 31))
        self.pushButton_34.setStyleSheet("background-color:#3366ff;")
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_35.setGeometry(QtCore.QRect(880, 50, 101, 31))
        self.pushButton_35.setStyleSheet("background-color:#3366ff;")
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_36 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_36.setGeometry(QtCore.QRect(760, 100, 101, 31))
        self.pushButton_36.setStyleSheet("background-color:#3366ff;")
        self.pushButton_36.setObjectName("pushButton_36")
        self.comboBox_9 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_9.setGeometry(QtCore.QRect(760, 50, 101, 31))
        self.comboBox_9.setStyleSheet("background-color:#3366ff;")
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_3.setGeometry(QtCore.QRect(910, 160, 81, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_12.setGeometry(QtCore.QRect(130, 110, 101, 31))
        self.pushButton_12.setStyleSheet("background-color:#3366ff;")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_20 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_20.setGeometry(QtCore.QRect(320, 150, 101, 31))
        self.pushButton_20.setStyleSheet("background-color:#3366ff;")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_21.setGeometry(QtCore.QRect(760, 150, 101, 31))
        self.pushButton_21.setStyleSheet("background-color:#3366ff;")
        self.pushButton_21.setObjectName("pushButton_21")
        self.Load_Button = QtWidgets.QPushButton(self.groupBox_2)
        self.Load_Button.setGeometry(QtCore.QRect(10, 50, 221, 31))
        self.Load_Button.setStyleSheet("background-color:#3366ff;")
        self.Load_Button.setObjectName("pushButton_16")
        self.Load_Button.clicked.connect(self.Browse_Signals)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1088, 26))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_Signal = QtWidgets.QAction(MainWindow)
        self.actionLoad_Signal.setObjectName("actionLoad_Signal")
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.horizontalSlider.valueChanged['int'].connect(self.lcdNumber.display) # type: ignore
        self.horizontalSlider_2.valueChanged['int'].connect(self.lcdNumber_2.display) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Live Signal Viewer</span></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "Channels"))
        self.pushButton_6.setText(_translate("MainWindow", "Rewind"))
        self.label.setText(_translate("MainWindow", "Cine Speed"))
        self.label_2.setText(_translate("MainWindow", "Cine Speed"))
        self.pushButton_7.setText(_translate("MainWindow", "Play"))
        self.pushButton_8.setText(_translate("MainWindow", "Play"))
        self.pushButton_9.setText(_translate("MainWindow", "Rewind"))
        self.Graph_One_Snapshot_Button.setText(_translate("MainWindow", "Snapshot"))
        self.Graph_Two_Snapshot_Button.setText(_translate("MainWindow", "Snapshot"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Controls"))
        self.pushButton_11.setText(_translate("MainWindow", "Link Graphs"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Channel 1"))
        self.pushButton_13.setText(_translate("MainWindow", "Edit Label"))
        self.label_3.setText(_translate("MainWindow", "Graph 1"))
        self.label_5.setText(_translate("MainWindow", "Graph 2"))
        self.pushButton_19.setText(_translate("MainWindow", "Select Color"))
        self.pushButton_28.setText(_translate("MainWindow", "Move"))
        self.checkBox.setText(_translate("MainWindow", "Hide"))
        self.pushButton_34.setText(_translate("MainWindow", "Move"))
        self.pushButton_35.setText(_translate("MainWindow", "Edit Label"))
        self.pushButton_36.setText(_translate("MainWindow", "Select Color"))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "Channel 1"))
        self.checkBox_3.setText(_translate("MainWindow", "Hide"))
        self.pushButton_12.setText(_translate("MainWindow", "Export"))
        self.pushButton_20.setText(_translate("MainWindow", "Add Channel"))
        self.pushButton_21.setText(_translate("MainWindow", "Add Channel"))
        self.Load_Button.setText(_translate("MainWindow", "Load Signal"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionLoad_Signal.setText(_translate("MainWindow", "Load Signal"))

            



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())