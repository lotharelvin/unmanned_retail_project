import requests
import cv2
import base64
from urllib import request
from urllib import parse
import json


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


def capture_commodity():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    image = image_to_base64(frame)
    cv2.imshow('test',frame)
    cap.release()
    cv2.release(10)
    return image


def recogn_commodity(image_path):
    request_url_header = 'https://aip.baidubce.com/rpc/2.0/ai_custom_retail/v1/detection/firstkc_test'

    #image_path = 'D:/test/20200821_220819.jpg'
    image = cv2.imread(image_path)
    image_base64 = image_to_base64(image)
    params = {"image": image_base64}
    params = json.dumps(params)
    params = params.encode('utf-8')
    access_token = get_access_token()

    request_url = request_url_header + "?access_token=" + access_token
    req = request.Request(url=request_url, data=params)
    req.add_header('Content-Type', 'application/json')
    #response = request.urlopen(req)
    content = request.urlopen(req).read()
    #if content:
    #    print(content)
    return content


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

#for debug
def get_cart(image_path):
    content = recogn_commodity(image_path)
    cart = get_temp_cart(content)
    return cart
