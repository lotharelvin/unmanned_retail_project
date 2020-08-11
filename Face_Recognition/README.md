# 人脸识别 

Author：KCLi2000 likwokc@mail2.sysu.edu.cn

Version: v1.0.1

#### 依赖库

由于baiduAI的在线人脸识别功能要通过URL请求，因此需要调用requests库；同时，baiduAI要求送进图片的格式是base64格式，因此我们需要base64，numpy库来进行图片格式转换。

```
pip install base64
pip install requests
pip install numpy
```

另外，还需要安装OpenCV库来进行摄像头调用和图片获取，网上教程带带的多

#### 怎么注册客户脸部信息

- 注册成为会员客户

  - 扫描小程序二维码

    ![小程序二维码]()

  - 或者登录网址 https://ai.baidu.com/facekit/page/form/1FE58A340DA24D378378C5F8106E79AD

- 注册成为Walk-in客户

  - 直接站在入口摄像机前面就行

#### How to use

```python
import defines

image = defines.capture_customer()
groupIdList = "Customer" 
customer = defines.search_customer(image, groupIdList)
customer_id = defines.CapCustomer.get_customer_id(customer)

if customer.customer_id != 0:
    FaceID = defines.CapCustomer.get_cus_FaceID(customer)

```

#### Sample Output

```
Registered Customer
18028606235(登记手机号)Customer
(or) 
Walk-in Customer
123468732545281(时间戳)WalkInCustomer
(or) 
Registered As Walk-in Customer, Please Try Again
(or) 
222202 
face pic not found
```

#### 环境

我自己的电脑环境是Windows10 + Pycharm，不知道其它系统或IDE行8行，不行再改

#### Reference
https://ai.baidu.com/ai-doc/FACE/ek37c1qiz