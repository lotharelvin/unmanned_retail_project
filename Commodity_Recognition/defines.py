from aip import AipFace
import sys
import gc
import cv2
import requests
import json
import base64
from urllib import request
from urllib import parse

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

import socket

#Face_ID = ''

#groupIdList = ''

class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)

        self.timer_camera = QtCore.QTimer()  # 初始化定时器
        self.cap = cv2.VideoCapture(3)  # 初始化摄像头
        #self.cap1 = cv2.VideoCapture(1)
        self.CAM_NUM = 0
        self.set_ui()
        self.slot_init()
        self.__flag_work = 0
        self.x = 0
        self.count = 0

    def set_ui(self):
        self.__layout_main = QtWidgets.QHBoxLayout()  # 采用QHBoxLayout类，按照从左到右的顺序来添加控件
        self.__layout_fun_button = QtWidgets.QHBoxLayout()
        self.__layout_data_show = QtWidgets.QVBoxLayout()  # QVBoxLayout类垂直地摆放小部件


        self.button_open_camera = QtWidgets.QPushButton(u'打开相机')
        self.button_close = QtWidgets.QPushButton(u'退出')
        self.button_capture = QtWidgets.QPushButton(u'识别商品')
        #self.button_face_recog = QtWidgets.QPushButton(u'识别身份')

        self.textBrowser = QtWidgets.QTextBrowser(self)
        #self.textBrowser.setGeometry(QtCore.QRect(200, 150, 181, 291))
        self.textBrowser.setObjectName("textBrowser")
        # button颜色修改
        button_color = [self.button_open_camera, self.button_close, self.button_capture]
        for i in range(3):
            button_color[i].setStyleSheet("QPushButton{color:black}"
                                           "QPushButton:hover{color:red}"
                                           "QPushButton{background-color:rgb(78,255,255)}"
                                           "QpushButton{border:2px}"
                                           "QPushButton{border_radius:10px}"
                                           "QPushButton{padding:2px 4px}")

        self.button_open_camera.setMinimumHeight(50)
        self.button_close.setMinimumHeight(50)
        self.button_capture.setMinimumHeight(50)
        #self.button_face_recog.setMinimumHeight(50)
        #self.button_face_recog.setMinimumWidth(100)
        self.textBrowser.setMinimumWidth(300)
        self.textBrowser.setMaximumHeight(300)

        # move()方法是移动窗口在屏幕上的位置到x = 500，y = 500的位置上
        self.move(500, 500)

        # 信息显示
        self.label_show_camera = QtWidgets.QLabel()
        #self.label_show_result = QtWidgets.QLabel()
        self.label_move = QtWidgets.QLabel()
        self.label_move.setFixedSize(100, 100)

        self.label_show_camera.setFixedSize(641, 481)
        self.label_show_camera.setAutoFillBackground(False)
        #self.label_show_result.setFixedSize(200, 100)

        self.__layout_fun_button.addWidget(self.button_open_camera)
        self.__layout_fun_button.addWidget(self.button_close)
        self.__layout_fun_button.addWidget(self.label_move)

        self.__layout_main.addLayout(self.__layout_fun_button)
        self.__layout_main.addWidget(self.label_show_camera)

        self.setLayout(self.__layout_main)
        self.label_move.raise_()
        self.setWindowTitle(u'摄像头')

        '''
        # 设置背景颜色
        palette1 = QPalette()
        palette1.setBrush(self.backgroundRole(),QBrush(QPixmap('background.jpg')))
        self.setPalette(palette1)
        '''

    def slot_init(self):  # 建立通信连接
        self.button_open_camera.clicked.connect(self.button_open_camera_click)
        self.timer_camera.timeout.connect(self.show_camera)
        self.button_close.clicked.connect(self.close)

    def button_open_camera_click(self):
        if self.timer_camera.isActive() == False:
            flag = self.cap.open(self.CAM_NUM)
            if flag == False:
                msg = QtWidgets.QMessageBox.Warning(self, u'Warning', u'请检测相机与电脑是否连接正确',
                                                    buttons=QtWidgets.QMessageBox.Ok,
                                                    defaultButton=QtWidgets.QMessageBox.Ok)
                # if msg==QtGui.QMessageBox.Cancel:
                #                     pass
            else:
                self.timer_camera.start(30)
                self.button_open_camera.setText(u'关闭相机')
                self.__layout_fun_button.addWidget(self.button_capture)
                #self.__layout_fun_button.addWidget(self.button_face_recog)
                self.__layout_fun_button.addWidget(self.textBrowser)
                self.button_capture.clicked.connect(lambda: self.commodity_recog(self.cap))
                #self.button_face_recog.clicked.connect(lambda: self.face_recog(self.cap))
            # self.timer_camera.start(30)
            # self.button_open_camera.setText(u'关闭相机')
            # self.__layout_fun_button.addWidget(self.button_capture)
            # self.__layout_fun_button.addWidget(self.button_face_recog)
            # self.__layout_fun_button.addWidget(self.textBrowser)
            # self.button_capture.clicked.connect(lambda: self.commodity_recog(self.cap))
            # #self.button_face_recog.clicked.connect(lambda: self.face_recog(self.cap))
        else:
            self.timer_camera.stop()
            self.cap.release()
            self.label_show_camera.clear()
            self.textBrowser.setText('')
            self.button_capture.setParent(None)
            self.textBrowser.setParent(None)
            self.__layout_data_show.removeWidget(self.textBrowser)
            self.__layout_fun_button.removeWidget(self.button_capture)
            #sip.delete(self.button_capture)
            self.button_open_camera.setText(u'打开相机')


    def printf(self, mes):
        self.textBrowser.append(mes)  # 在指定的区域显示提示信息
        self.cursot = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursot.End)

    def show_camera(self):
        flag, self.image = self.cap.read()
        show = cv2.resize(self.image, (640, 480))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.label_show_camera.setPixmap(QtGui.QPixmap.fromImage(showImage))

    # def commodity_recog(self, cap):
    #     ret, frame = cap.read()
    #     cv2.imshow('test', frame)
    #     cv2.waitKey(10000)

    def face_recog(self, cap):
        #self.textBrowser.setText('')
        APP_ID = '21866956'
        API_KEY = '3GpEYKemawrtV8FW9wNUmi7h'
        SECRET_KEY = 'qhGp0f4ijc4cYIC9RFfWTGeDaM6GQZGB'
        client = AipFace(APP_ID, API_KEY, SECRET_KEY)

        imageType = "BASE64"
        groupIdList = "Customer"

        ret, frame = cap.read()
        #cv2.imshow('test', frame)
        image = image_to_base64(frame)
        customer_info = client.search(image, imageType, groupIdList)
        self.printf('客户信息')
        #self.printf(' ')
        face_threshold = 70
        if customer_info['error_code'] == 0:
            face_score = customer_info['result']['user_list'][0]['score']

        if face_score > face_threshold:
                self.printf('Registered Customer')
                self.printf(customer_info['result']['user_list'][0]['user_info'])
                return int(customer_info['result']['user_list'][0]['user_info'])
        elif (customer_info['error_code'] == 0 and face_score <= face_threshold) or customer_info['error_code'] == 222207:
            groupIdList = 'WalkInCustomer'
            customer_info = client.search(image, imageType, groupIdList)
            if customer_info['error_code'] == 0:
                face_score = customer_info['result']['user_list'][0]['score']
                if face_score > face_threshold:
                    self.printf('Walk-in Customer')
                    self.printf(customer_info['result']['user_list'][0]['user_info'])
                    return int(customer_info['result']['user_list'][0]['user_info'])
                else:
                    self.printf('Recognition Failed! Please Try Again')
                    return 0
            else:
                self.printf('Recognition Failed! Please Try Again')
                return 0
        else:
            self.printf('Recognition Failed! Please Try Again')
            return 0

    def commodity_recog(self, cap):
        self.textBrowser.setText('')
        cap1 = cv2.VideoCapture(4)
        Face_ID = self.face_recog(cap1)
        self.printf('')
        self.printf('待付款商品：')
        access_token = get_access_token()
        #self.printf(access_token)
        request_url_header = 'https://aip.baidubce.com/rpc/2.0/ai_custom_retail/v1/detection/firstkc_test'

        ret, frame = cap.read()
        # image_path = 'D:/test/20200821_220819.jpg'
        # image = cv2.imread(image_path)
        cv2.imshow('test', frame)
        image_base64 = image_to_base64(frame)

        params = {"image": image_base64}
        params = json.dumps(params)
        params = params.encode('utf-8')

        request_url = request_url_header + "?access_token=" + access_token
        req = request.Request(url=request_url, data=params)
        req.add_header('Content-Type', 'application/json')
        #response = request.urlopen(req)
        content = request.urlopen(req).read()
        if content:
            print(eval(content))
        cart = get_temp_cart(content)
        data = {'Face_ID': Face_ID, 'Cart': cart}
        data_client(data)

        commodity_num = len(cart)
        count = 0
        while count < commodity_num:
            self.printf(cart[count])
            count = count + 1

    def closeEvent(self, event):
        ok = QtWidgets.QPushButton()
        cancel = QtWidgets.QPushButton()
        msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, u'关闭', u'是否关闭！')
        msg.addButton(ok, QtWidgets.QMessageBox.ActionRole)
        msg.addButton(cancel, QtWidgets.QMessageBox.RejectRole)
        ok.setText(u'确定')
        cancel.setText(u'取消')
        if msg.exec_() == QtWidgets.QMessageBox.RejectRole:
            event.ignore()
        else:
            if self.cap.isOpened():
                self.cap.release()
            if self.timer_camera.isActive():
                self.timer_camera.stop()
            event.accept()


def get_access_token():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=aZZaDTaKHbgKbVoQFlrniQDB&client_secret=vBnziymZom2sLDkT1UbZDRKrQ7o9f27z'
    response = requests.get(host)
    if response:
        #print(response.json()["access_token"])
        return response.json()["access_token"]
    return 0


def image_to_base64(image):
    image_code = base64.b64encode(cv2.imencode('.jpg', image)[1]).decode()
    return image_code


def detect_face(image):
    # Activate BaiduAI
    APP_ID = '21866956'
    API_KEY = '3GpEYKemawrtV8FW9wNUmi7h'
    SECRET_KEY = 'qhGp0f4ijc4cYIC9RFfWTGeDaM6GQZGB'
    client = AipFace(APP_ID, API_KEY, SECRET_KEY)

    options = {}
    options['max_face_num'] = 1
    options['liveness_control'] = "HIGH"

    res = client.detect(image, "BASE64", options)
    gc.collect()
    return res


def get_temp_cart(content):
    content_eval = eval(content)
    result = content_eval['results']
    commodity_num = len(result)
    cart = []
    count = 0
    while count < commodity_num:
        commodity = result[count]['name']
        cart.append(commodity)
        count = count + 1
    return cart


def data_client(data):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 4396))
    print('success')
    json_string = bytes(json.dumps(data), encoding='utf-8')
    client.send(json_string)
    print('send')
    # s.sendto(json_string, address)
    # s.shutdown(socket.SHUT_RDWR)
    client.shutdown(socket.SHUT_RDWR)


def start_qt():
    App = QApplication(sys.argv)
    win = Ui_MainWindow()
    win.show()
    sys.exit(App.exec_())

