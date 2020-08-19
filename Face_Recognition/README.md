# 人脸识别 

Author：KCLi2000 likwokc@mail2.sysu.edu.cn

Version: v1.1.3

#### 依赖库

由于baiduAI的在线人脸识别功能要通过URL请求，因此需要调用requests库；同时，baiduAI要求送进图片的格式是base64格式，因此我们需要base64，numpy库来进行图片格式转换。

```
pip install pybase64
pip install requests
pip install python-opencv
pip install baidu-aip
(sudo) python setup.py install
```

另外，还需要安装OpenCV库来进行摄像头调用和图片获取，网上教程带带的多

#### 怎么注册客户脸部信息

- 注册成为会员客户（Registered Customer）

  - 扫描小程序二维码

    ![小程序二维码](https://github.com/lotharelvin/unmanned_retail_project/blob/master/Face_Recognition/QR_Code.png)

  - 或者登录网址 https://ai.baidu.com/facekit/page/form/1FE58A340DA24D378378C5F8106E79AD

- 注册成为Walk-in客户

  - 直接站在入口摄像机前面就行

#### How to use

```python
#test.py
import defines

FaceID = defines.get_cus_FaceID()
print(FaceID)
#-----

cd Face_Recognition
pip install baidu-aip
sudo python setup.py intall
./test.py

```

#### Sample Output

```
---已通过小程序注册
Registered Customer
18028606235(登记手机号)Customer <-- FaceID
(or) ---之前已在现场注册
Walk-in Customer
123468732545281(时间戳)WalkInCustomer <-- FaceID
(or) ---第一次在现场注册
match face not found
123468732545281(时间戳)WalkInCustomer <-- FaceID
(or) ---没有捕捉到人脸
222202 
face pic not found
0 <-- FaceID (当FaceID输出为0时，可以忽略)
```

#### 版本历史

| 版本   | 版本改动内容概要                                             |
| ------ | :----------------------------------------------------------- |
| v1.0.0 | 实现了在现有人脸库中进行人脸识别的功能                       |
| v1.1.0 | 增加了对Walk-in客户的现场注册并识别功能，优化了FaceID的输出接口 |
| v1.1.1 | 针对无门禁进入场景，优化了对Walk-in客户注册识别的功能        |
| v1.1.2 | 解决了一个有关匹配率低也返回匹配成功的bug                    |
| v1.1.3 | 解决了一个摄像头bug并将FaceID类型修改为int                   |

#### 环境

我自己的电脑环境是**Windows10 + Pycharm**，不知道其它系统或IDE行8行，不行再改.

**实测ubuntu18.04+python2.7也行**

#### Reference
https://ai.baidu.com/ai-doc/FACE/ek37c1qiz
