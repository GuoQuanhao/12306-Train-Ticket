# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MianWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time
from get_stations import *
import source_rc

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from query_request import *
from PyQt5.QtGui import *

class Ui_mainWindow(object):
    # setupUi由Qt Designer设计
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(960, 850)
        mainWindow.setMinimumSize(QtCore.QSize(480, 360))
        mainWindow.setMaximumSize(QtCore.QSize(960, 1080))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title_img = QtWidgets.QLabel(self.centralwidget)
        self.label_title_img.setGeometry(QtCore.QRect(0, 0, 960, 225))
        self.label_title_img.setStyleSheet("background-image: url(:/png/src/bg1.png);")
        self.label_title_img.setText("")
        self.label_title_img.setObjectName("label_title_img")
        self.widget_input = QtWidgets.QWidget(self.centralwidget)
        self.widget_input.setGeometry(QtCore.QRect(0, 225, 640, 80))
        self.widget_input.setStyleSheet("background-image: url(:/png/src/bg2.png);")
        self.widget_input.setObjectName("widget_input")
        self.label_departure = QtWidgets.QLabel(self.widget_input)
        self.label_departure.setGeometry(QtCore.QRect(0, 32, 60, 15))
        self.label_departure.setObjectName("label_departure")
        self.lineEdit_departure = QtWidgets.QLineEdit(self.widget_input)
        self.lineEdit_departure.setGeometry(QtCore.QRect(55, 30, 113, 21))
        self.lineEdit_departure.setText("")
        self.lineEdit_departure.setObjectName("lineEdit_departure")
        self.lineEdit_destination = QtWidgets.QLineEdit(self.widget_input)
        self.lineEdit_destination.setGeometry(QtCore.QRect(235, 30, 113, 21))
        self.lineEdit_destination.setText("")
        self.lineEdit_destination.setObjectName("lineEdit_destination")
        self.label_destination = QtWidgets.QLabel(self.widget_input)
        self.label_destination.setGeometry(QtCore.QRect(175, 32, 60, 15))
        self.label_destination.setObjectName("label_destination")
        self.lineEdit_date = QtWidgets.QLineEdit(self.widget_input)
        self.lineEdit_date.setGeometry(QtCore.QRect(430, 30, 113, 21))
        self.lineEdit_date.setObjectName("lineEdit_date")
        self.label_date = QtWidgets.QLabel(self.widget_input)
        self.label_date.setGeometry(QtCore.QRect(355, 32, 72, 15))
        self.label_date.setObjectName("label_date")
        self.pushButton_inquire = QtWidgets.QPushButton(self.widget_input)
        self.pushButton_inquire.setGeometry(QtCore.QRect(548, 26, 93, 28))
        self.pushButton_inquire.setObjectName("pushButton_inquire")
        self.label_departure.raise_()
        self.lineEdit_departure.raise_()
        self.lineEdit_destination.raise_()
        self.label_destination.raise_()
        self.label_date.raise_()
        self.pushButton_inquire.raise_()
        self.lineEdit_date.raise_()
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(640, 225, 320, 80))
        self.label_logo.setStyleSheet("background-image: url(:/png/src/logo.png);")
        self.label_logo.setText("")
        self.label_logo.setObjectName("label_logo")
        self.widget_train_class = QtWidgets.QWidget(self.centralwidget)
        self.widget_train_class.setGeometry(QtCore.QRect(0, 305, 960, 35))
        self.widget_train_class.setStyleSheet("background-image: url(:/png/src/bg3.png);")
        self.widget_train_class.setObjectName("widget_train_class")
        self.label_train_class = QtWidgets.QLabel(self.widget_train_class)
        self.label_train_class.setGeometry(QtCore.QRect(20, 10, 72, 15))
        self.label_train_class.setObjectName("label_train_class")
        self.checkBox_G = QtWidgets.QCheckBox(self.widget_train_class)
        self.checkBox_G.setGeometry(QtCore.QRect(120, 9, 91, 19))
        self.checkBox_G.setObjectName("checkBox_G")
        self.checkBox_D = QtWidgets.QCheckBox(self.widget_train_class)
        self.checkBox_D.setGeometry(QtCore.QRect(280, 9, 91, 19))
        self.checkBox_D.setObjectName("checkBox_D")
        self.checkBox_Z = QtWidgets.QCheckBox(self.widget_train_class)
        self.checkBox_Z.setGeometry(QtCore.QRect(440, 9, 91, 19))
        self.checkBox_Z.setObjectName("checkBox_Z")
        self.checkBox_T = QtWidgets.QCheckBox(self.widget_train_class)
        self.checkBox_T.setGeometry(QtCore.QRect(600, 9, 91, 19))
        self.checkBox_T.setObjectName("checkBox_T")
        self.checkBox_K = QtWidgets.QCheckBox(self.widget_train_class)
        self.checkBox_K.setGeometry(QtCore.QRect(760, 9, 91, 19))
        self.checkBox_K.setObjectName("checkBox_K")
        self.label_information = QtWidgets.QLabel(self.centralwidget)
        self.label_information.setGeometry(QtCore.QRect(0, 340, 960, 62))
        self.label_information.setStyleSheet("background-image: url(:/png/src/bg4.png);")
        self.label_information.setText("")
        self.label_information.setObjectName("label_information")
        self.tableView_information = QtWidgets.QTableView(self.centralwidget)
        self.tableView_information.setGeometry(QtCore.QRect(0, 402, 960, 448))
        self.tableView_information.setObjectName("tableView_information")

        self.model = QStandardItemModel()  # 创建存储数据的模式
        # 根据空间自动改变列宽度并且不可修改列宽度
        self.tableView_information.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 设置表头不可见
        self.tableView_information.horizontalHeader().setVisible(False)
        # 纵向表头不可见
        self.tableView_information.verticalHeader().setVisible(False)
        # 设置表格内容文字大小
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableView_information.setFont(font)
        # 设置表格内容不可编辑
        self.tableView_information.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 垂直滚动条始终开启
        self.tableView_information.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.widget_input.raise_()
        self.label_title_img.raise_()
        self.label_logo.raise_()
        self.widget_train_class.raise_()
        self.label_information.raise_()
        self.tableView_information.raise_()
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "12306官网查询"))
        self.label_departure.setText(_translate("mainWindow", "出发地："))
        self.label_destination.setText(_translate("mainWindow", "目的地："))
        self.label_date.setText(_translate("mainWindow", "出发日期："))
        self.pushButton_inquire.setText(_translate("mainWindow", "查询"))
        self.label_train_class.setText(_translate("mainWindow", "车次类型："))
        self.checkBox_G.setText(_translate("mainWindow", "G-高铁"))
        self.checkBox_D.setText(_translate("mainWindow", "D-动车"))
        self.checkBox_Z.setText(_translate("mainWindow", "Z-直达"))
        self.checkBox_T.setText(_translate("mainWindow", "T-特快"))
        self.checkBox_K.setText(_translate("mainWindow", "K-快车"))

        self.lineEdit_date.setText(get_time())  # 出发日显示当天日期
        self.pushButton_inquire.clicked.connect(self.on_click)  # 查询按钮指定单击事件的方法
        self.checkBox_G.stateChanged.connect(self.change_G)  # 高铁选中与取消事件
        self.checkBox_D.stateChanged.connect(self.change_D)  # 动车选中与取消事件
        self.checkBox_Z.stateChanged.connect(self.change_Z)  # 直达车选中与取消事件
        self.checkBox_T.stateChanged.connect(self.change_T)  # 特快车选中与取消事件
        self.checkBox_K.stateChanged.connect(self.change_K)  # 快车选中与取消事件

    # 将所有车次分类复选框取消勾选
    def checkBox_default(self):
        self.checkBox_G.setChecked(False)
        self.checkBox_D.setChecked(False)
        self.checkBox_Z.setChecked(False)
        self.checkBox_T.setChecked(False)
        self.checkBox_K.setChecked(False)

    # 查询按钮的单击事件
    def on_click(self):
        get_from = self.lineEdit_departure.text() # 获取出发地
        get_to = self.lineEdit_destination.text()  # 获取到达地
        get_date = self.lineEdit_date.text()  # 获取出发时间
        # 判断车站文件是否存在
        if isStations() == True:
            stations = eval(read())  # 读取所有车站并转换为dic类型
            # 判断所有参数是否为空，出发地、目的地、出发日期
            if get_from != "" and get_to != "" and get_date != "":
                # 判断输入的车站名称是否存在，以及时间格式是否正确
                if get_from in stations and get_to in stations and is_valid_date(get_date):
                    # 获取输入的日期是当前年初到现在一共过了多少天
                    inputYearDay = time.strptime(get_date, "%Y-%m-%d").tm_yday
                    # 获取系统当前日期是当前年初到现在一共过了多少天
                    yearToday = time.localtime(time.time()).tm_yday
                    # 计算时间差，也就是输入的日期减掉系统当前的日期
                    timeDifference = inputYearDay - yearToday
                    # 判断时间差为0时证明是查询当前的查票，
                    # 以及29天以后的车票。12306官方要求只能查询30天以内的车票
                    if timeDifference >= 0 and timeDifference <= 28:
                        from_station = stations[get_from]  # 在所有车站文件中找到对应的参数，出发地
                        to_station = stations[get_to]  # 目的地
                        data = query(get_date, from_station, to_station)  # 发送查询请求,并获取返回的信息
                        self.checkBox_default()
                        if len(data) != 0:  # 判断返回的数据是否为空
                            # 如果不是空的数据就将车票信息显示在表格中
                            self.displayTable(len(data), 16, data)
                        else:
                            self.messageDialog('警告', '没有返回的网络数据！')
                    else:
                        self.messageDialog('警告', '超出查询日期的范围内,'
                                                 '不可查询昨天的车票信息,以及29天以后的车票信息！')
                else:
                    self.messageDialog('警告', '输入的站名不存在,或日期格式不正确！')
            else:
                self.messageDialog('警告', '请填写车站名称！')
        else:
            self.messageDialog('警告', '未下载车站查询文件！')

    # 高铁复选框事件处理
    def change_G(self, state):
        # 选中将高铁信息添加到最后要显示的数据当中
        if state == QtCore.Qt.Checked:
            # 获取高铁信息
            g_vehicle()
            # 通过表格显示该车型数据
            self.displayTable(len(type_data), 16, type_data)
        else:
            # 取消选中状态将移除该数据
            r_g_vehicle()
            self.displayTable(len(type_data), 16, type_data)

    # 动车复选框事件处理
    def change_D(self, state):
        # 选中将动车信息添加到最后要显示的数据当中
        if state == QtCore.Qt.Checked:
            # 获取动车信息
            d_vehicle()
            # 通过表格显示该车型数据
            self.displayTable(len(type_data), 16, type_data)

        else:
            # 取消选中状态将移除该数据
            r_d_vehicle()
            self.displayTable(len(type_data), 16, type_data)

    # 直达复选框事件处理
    def change_Z(self, state):
        # 选中将直达车信息添加到最后要显示的数据当中
        if state == QtCore.Qt.Checked:
            # 获取直达车信息
            z_vehicle()
            self.displayTable(len(type_data), 16, type_data)
        else:
            # 取消选中状态将移除该数据
            r_z_vehicle()
            self.displayTable(len(type_data), 16, type_data)

    # 特快复选框事件处理
    def change_T(self, state):
        # 选中将特快车信息添加到最后要显示的数据当中
        if state == QtCore.Qt.Checked:
            # 获取特快车信息
            t_vehicle()
            self.displayTable(len(type_data), 16, type_data)
        else:
            # 取消选中状态将移除该数据
            r_t_vehicle()
            self.displayTable(len(type_data), 16, type_data)

    # 快速复选框事件处理
    def change_K(self, state):
        # 选中将快车信息添加到最后要显示的数据当中
        if state == QtCore.Qt.Checked:
            # 获取快速车信息
            k_vehicle()
            self.displayTable(len(type_data), 16, type_data)

        else:
            # 取消选中状态将移除该数据
            r_k_vehicle()
            self.displayTable(len(type_data), 16, type_data)

    # 显示消息提示框，参数title为提示框标题文字，message为提示信息
    def messageDialog(self, title, message):
        msg_box = QMessageBox(QMessageBox.Warning, title, message)
        msg_box.exec_()

    # 显示车次信息的表格
    # train参数为共有多少趟列车，该参数作为表格的行。
    # info参数为每趟列车的具体信息，例如有座、无座卧铺等。该参数作为表格的列
    def displayTable(self, train, info, data):
        self.model.clear()
        for row in range(train):
            for column in range(info):
                # 添加表格内容
                item = QStandardItem(data[row][column])
                # 向表格存储模式中添加表格具体信息
                self.model.setItem(row, column, item)
        # 设置表格存储数据的模式
        self.tableView_information.setModel(self.model)

# 获取系统当前时间并转换请求数据所需要的格式
def get_time():
    # 获得当前时间时间戳
    now = int(time.time())
    # 转换为其它日期格式,如:"%Y-%m-%d %H:%M:%S"
    timeStruct = time.localtime(now)
    strTime = time.strftime("%Y-%m-%d", timeStruct)
    return strTime


def is_valid_date(str):
    '''判断是否是一个有效的日期字符串'''
    try:
        time.strptime(str, "%Y-%m-%d")
        return True
    except:
        return False

# 定义显示函数
def show_MainWindow():
    app = QtWidgets.QApplication(sys.argv)  # 实例化QApplication类，作为GUI主程序入口
    MainWindow = QtWidgets.QMainWindow()  # 实例化QtWidgets.QMainWindow类，创建自带menu的窗体类型QMainWindow
    ui = Ui_mainWindow()  # 实例化UI类
    ui.setupUi(MainWindow)  # 设置窗体UI
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec_())
    # 当来自操作系统的分发事件指派调用窗口时，
    # 应用程序开启主循环（mainloop）过程，
    # 当窗口创建完成，需要结束主循环过程，
    # 这时候呼叫sys.exit（）方法来，结束主循环过程退出，
    # 并且释放内存。为什么用app.exec_()而不是app.exec()？
    # 因为exec是python系统默认关键字，为了以示区别，所以写成exec_


# 主程序入口
if __name__ == '__main__':
    if isStations() == False:
        getStation()
    show_MainWindow()