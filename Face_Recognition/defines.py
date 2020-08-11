from aip import AipFace
import numpy as np
import cv2
import base64


class CapCustomer(object):
    """CapCustomer Class"""
    def __init__(self):
        super(CapCustomer,self).__init__()
        self.user_id = 0;
        self.group_id = 0;
        self.state = "Not In Store"

    def get_user_id(self):
        return self.user_id

    def get_group_id(self):
        return self.group_id

    def get_cus_state(self):
        return self.state


def image_to_base64(image):
    image_code = base64.b64encode(cv2.imencode('.jpg', image)[1]).decode()
    return image_code


def capture_customer():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    image = image_to_base64(frame)
    #cv2.imshow('test', frame)
    cv2.waitKey(10)
    return image


def search_customer(image, groupIdList):
    # Activate BaiduAI
    APP_ID = '21866956'
    API_KEY = '3GpEYKemawrtV8FW9wNUmi7h'
    SECRET_KEY = 'qhGp0f4ijc4cYIC9RFfWTGeDaM6GQZGB'
    client = AipFace(APP_ID, API_KEY, SECRET_KEY)

    # Video Capture
    imageType = "BASE64"
    customer_info = client.search(image, imageType, groupIdList);
    customer = CapCustomer()

    # Get Customer Info.
    if customer_info['error_code'] != 0:
        print(customer_info['error_msg'])
        return customer
    else:
        customer.user_id = customer_info['result']['user_list'][0]['user_id']
        customer.group_id = customer_info['result']['user_list'][0]['group_id']
        customer.state = "In Store"
        return customer




