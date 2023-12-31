# -*- coding: utf-8 -*-
import numpy as np
# Form implementation generated from reading ui file '03.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import pyqtgraph as pg

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1469, 1026)
        # pg.setConfigOption('background', 'black')  # 将 PyqtGraph 的背景色设置为白色
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = PlotWidget(self.tab)
        # self.label_5.setBackground('w')
        self.label_5.getAxis('left').setPen(pg.mkPen(color='white', width=2))
        self.label_5.getAxis('bottom').setPen(pg.mkPen(color='white', width=2))
        self.label_5.showGrid(x=True, y=True)
        self.label_5.setObjectName("plot_5")
        self.plot5_x = np.arange(100, 200)
        self.plot5_y1 = np.zeros(100)
        self.plot5_curve1 = self.label_5.plot(x=self.plot5_x, y=self.plot5_y1, pen=pg.mkPen(color='blue', width=3),
                                              name='angle')
        # 创建图例对象并将曲线添加到图例中，同时设置图例位置
        self.legend = self.label_5.addLegend()
        self.legend.addItem(self.plot5_curve1, name='angle')

        self.gridLayout_2.addWidget(self.label_5, 2, 1, 1, 1)
        self.label_4 = PlotWidget(self.tab)
        # self.label_4.setBackground('w')
        self.label_4.getAxis('left').setPen(pg.mkPen(color='white', width=2))
        self.label_4.getAxis('bottom').setPen(pg.mkPen(color='white', width=2))
        self.label_4.showGrid(x=True, y=True)
        self.label_4.setObjectName("plot_4")
        self.plot4_x = np.arange(100, 200)
        self.plot4_y1 = np.zeros(100)
        self.plot4_y2 = np.zeros(100)
        self.plot4_y2[:] = 0.15  # 阈值 0.15
        self.plot4_curve1 = self.label_4.plot(x=self.plot4_x, y=self.plot4_y1, pen=pg.mkPen(color='green', width=3),
                                        name='smile')
        self.plot4_curve2 = self.label_4.plot(x=self.plot4_x, y=self.plot4_y2, pen=pg.mkPen(color='red', style=QtCore.Qt.DashLine, width=3),
                                              name='阈值')
        # 创建图例对象并将曲线添加到图例中，同时设置图例位置
        self.legend = self.label_4.addLegend()
        self.legend.addItem(self.plot4_curve1, name='smile')
        self.legend.addItem(self.plot4_curve2, name='阈值')

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_3 = PlotWidget(self.tab)
        # self.label_3.setBackground('w')
        self.label_3.getAxis('left').setPen(pg.mkPen(color='white', width=2))
        self.label_3.getAxis('bottom').setPen(pg.mkPen(color='white', width=2))
        self.label_3.showGrid(x=True, y=True)
        self.label_3.setObjectName("plot_3")
        self.plot3_x = np.arange(100, 200)
        self.plot3_y1 = np.zeros(100)
        self.plot3_y2 = np.zeros(100)
        # 创建曲线对象并设置name参数
        self.plot3_curve1 = self.label_3.plot(x=self.plot3_x, y=self.plot3_y1, pen=pg.mkPen(color='purple', width=3),
                                              name='mouth_h')
        self.plot3_curve2 = self.label_3.plot(x=self.plot3_x, y=self.plot3_y2, pen=pg.mkPen(color='pink', width=3),
                                              name='mouth_w')

        # 创建图例对象并将曲线添加到图例中，同时设置图例位置
        self.legend = self.label_3.addLegend()
        self.legend.addItem(self.plot3_curve1, name='mouth_h')
        self.legend.addItem(self.plot3_curve2, name='mouth_w')

        self.gridLayout_2.addWidget(self.label_3, 1, 1, 1, 1)
        self.label_2 = PlotWidget(self.tab)
        # self.label_2.setBackground('w')
        self.label_2.getAxis('left').setPen(pg.mkPen(color='white', width=2))
        self.label_2.getAxis('bottom').setPen(pg.mkPen(color='white', width=2))
        self.label_2.showGrid(x=True, y=True)
        self.label_2.setObjectName("plot_1")
        self.plot1_x = np.arange(100, 200)
        self.plot1_y1 = np.zeros(100)
        self.plot1_y2 = np.zeros(100)
        # 创建曲线对象并设置name参数
        self.plot1_curve1 = self.label_2.plot(x=self.plot1_x, y=self.plot1_y1, pen=pg.mkPen(color='red', width=2),
                                        name='左眼')
        self.plot1_curve2 = self.label_2.plot(x=self.plot1_x, y=self.plot1_y2, pen=pg.mkPen(color='yellow', width=2),
                                        name='右眼')

        # 创建图例对象并将曲线添加到图例中，同时设置图例位置
        self.legend = self.label_2.addLegend()
        self.legend.addItem(self.plot1_curve1, name='左眼')
        self.legend.addItem(self.plot1_curve2, name='右眼')


        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setScaledContents(True)
        self.label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        # self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 2, 1)
        self.tabWidget.addTab(self.tab, "")


        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_6 = PlotWidget(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = PlotWidget(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 1, 1, 1)
        self.label_10 = PlotWidget(self.tab_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 2, 1, 1)
        self.label_8 = PlotWidget(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_9 = PlotWidget(self.tab_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 1, 1, 1, 1)
        self.label_11 = PlotWidget(self.tab_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 1, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1269, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setTitle(_translate("MainWindow", "head_pose"))
        self.label_4.setTitle(_translate("MainWindow", "smile"))
        self.label_3.setTitle(_translate("MainWindow", "mouth"))
        self.label_2.setTitle(_translate("MainWindow", "eyes"))
        self.label.setText(_translate("MainWindow", "摄像头"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "第一页"))
        self.label_6.setTitle(_translate("MainWindow", "TextLabel"))
        self.label_7.setTitle(_translate("MainWindow", "TextLabel"))
        self.label_10.setTitle(_translate("MainWindow", "TextLabel"))
        self.label_8.setTitle(_translate("MainWindow", "TextLabel"))
        self.label_9.setTitle(_translate("MainWindow", "TextLabel"))
        self.label_11.setTitle(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "第二页"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "第三页"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.menu_2.setTitle(_translate("MainWindow", "开始"))
        self.menu_3.setTitle(_translate("MainWindow", "关于我"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     # ui.camera()
#     MainWindow.show()
#     sys.exit(app.exec_())
