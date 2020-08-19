from aip import AipFace
import numpy as np
import cv2
import base64
import time
import gc


class CapCustomer(object):
    """CapCustomer Class"""
    def __init__(self):
        super(CapCustomer, self).__init__()
        self.customer_id = 0
        self.group_id = 0
        self.state = "Not In Store"
        self.type = "default"

    def get_customer_id(self):
        return self.customer_id

    def get_group_id(self):
        return self.group_id

    def get_cus_state(self):
        return self.state

    def get_cus_FaceID(self):
        FaceID = int(self.customer_id)
        return FaceID

    def get_cus_type(self):
        return self.type

    def __del__(self):
        return


def image_to_base64(image):
    image_code = base64.b64encode(cv2.imencode('.jpg', image)[1]).decode()
    return image_code


def capture_video():
    capture = cv2.VideoCapture(0)
    i = 0
    while True:
        ret, image = capture.read()
        #cv2.imshow("test", image)
        i = i+1
        #print(i)
        if cv2.waitKey(10) == 27 or i==10:

            i = 0
            return image
            break


def add_customer(image, groupIdList):
    # Activate BaiduAI
    APP_ID = '21866956'
    API_KEY = '3GpEYKemawrtV8FW9wNUmi7h'
    SECRET_KEY = 'qhGp0f4ijc4cYIC9RFfWTGeDaM6GQZGB'
    client = AipFace(APP_ID, API_KEY, SECRET_KEY)

    user_id = str(int(time.time()))
    options = {}
    options["user_info"] = user_id
    options["liveness_control"] = "NORMAL"
    client.addUser(image,"BASE64", groupIdList, user_id, options)
    gc.collect()
    return user_id


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


def search_customer(image):
    # Activate BaiduAI
    APP_ID = '21866956'
    API_KEY = '3GpEYKemawrtV8FW9wNUmi7h'
    SECRET_KEY = 'qhGp0f4ijc4cYIC9RFfWTGeDaM6GQZGB'
    client = AipFace(APP_ID, API_KEY, SECRET_KEY)

    # Video Capture
    imageType = "BASE64"
    groupIdList = "Customer"
    detect_result = detect_face(image)
    if detect_result['error_code'] == 0:
        face_probability = detect_result['result']['face_list'][0]['face_probability']
        if face_probability >= 0.8:
            customer_info = client.search(image, imageType, groupIdList)
            customer = CapCustomer()
            if customer_info['error_code'] == 0:
                face_score = customer_info['result']['user_list'][0]['score']

            # Get Customer Info.
            if face_score > 80:
                print("Registered Customer")
                customer.customer_id = customer_info['result']['user_list'][0]['user_info']
                customer.group_id = customer_info['result']['user_list'][0]['group_id']
                customer.type = "Registered Customer"
                customer.state = "In Store"
                gc.collect()
                return customer

            elif (customer_info['error_code'] == 0 and face_score <= 80) or customer_info['error_code'] == 222207:
                groupId = "WalkInCustomer"
                customer_info = client.search(image, imageType, groupId)
                if customer_info['error_code'] == 0:
                    face_score = customer_info['result']['user_list'][0]['score']

                if customer_info['error_code'] == 0 and face_score > 80:
                    print("Walk-in Customer")
                    customer.customer_id = customer_info['result']['user_list'][0]['user_info']
                    customer.group_id = customer_info['result']['user_list'][0]['group_id']
                    customer.type = "Walk-in Customer"
                    customer.state = "In Store"
                    return customer

                elif (customer_info['error_code'] == 0 and face_score <= 80) or customer_info['error_code'] == 222207:
                    print(customer_info['error_msg'])
                    detect_result = detect_face(image)
                    if detect_result['error_code'] == 0:
                        face_probability = detect_result['result']['face_list'][0]['face_probability']
                        if face_probability >= 0.8:
                            customer.customer_id = add_customer(image, groupId)
                            customer.group_id = groupId
                            cv2.waitKey(10)
                            customer.type = "New Customer"
                            customer.state = "In Store"
                            return customer
                    else:
                        print("No face detected")
                        return customer

            else:
                print(customer_info['error_code'])
                print(customer_info['error_msg'])
                return customer
    else:
        print(detect_result['error_msg'])
        customer = CapCustomer()
        return customer


def get_capcus_FaceID():
    image = capture_video()
    image_base64 = image_to_base64(image)
    customer = search_customer(image_base64)
    FaceID = CapCustomer.get_cus_FaceID(customer)
    del customer
    gc.collect()
    return FaceID



