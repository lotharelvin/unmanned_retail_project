# 模拟结算台商品识别 

Author：李国锵 likwokc@mail2.sysu.edu.cn

Version:  v1.0.2

#### 依赖库

由于baiduAI的在线人脸识别功能以及商品识别功能要通过URL请求，因此需要调用requests库；同时，baiduAI要求送进图片的格式是base64格式，因此我们需要base64库来进行图片格式转换。图像处理我们应用OpenCV库。

```
pip install pybase64
pip install requests
pip install python-opencv
pip install urllib
pip install baidu-aip
```

另外还需要安装pyqt5，由于anaconda的兼容性问题，安装pyqt5的版本必须在5.12.3以下，建议安装5.12.3。

**建议的安装方式：在官网上下载对应系统的whl安装包然后pip install [安装包名]**

#### How to use

- **目前仅支持屈臣氏饮用水280ml，维记鲜奶946ml，双薄荷黑人牙膏盒装，维达纸巾和宝矿力水特500ml的识别**
- **利用pyqt5搭建了一个简易GUI界面，使用流程：“打开摄像头”-->“开始识别”**
- **由于pyqt5中的按键回调函数（Button Callback Function）不能有返回值，我们用socket（TCP）编程来实现信息传输，因此服务端（server）需要开启一个信道来监听识别台发送的数据（目前已经利用两个电脑上验证了该思路的可行性）**
- **Python进行编程时，必须要bytes型数据（如果要发送的数据是中文则必须用utf-8来进行编码），因此我们将识别结果（列表List）打包成json数据格式来进行发送**

```python
#main.py
import defines

defines.start_qt()
(然后就会启动GUI界面)

```

#### Sample Output

```
["face_id": 1825371932; "cart": "黑人牙膏"]
```

#### 版本历史

| 版本   | 版本改动内容概要                                | 修改日期/成员    |
| ------ | :---------------------------------------------- | ---------------- |
| alpha  | 实现了手动送图的正确识别，并返回购物车列表      | 2020.8.20/李国锵 |
| v1.0.0 | 利用pyqt5构建了一个GUI界面                      | 2020.8.25/李国锵 |
| v1.0.1 | 利用socket（TCP）编程实现了server和client的通信 | 2020.9.1/李国锵  |
| v1.0.2 | 整合了人脸识别，基本实现了完整的结算流程        | 2020.9.4/李国锵  |

#### 后续工作

- 对错误输入的处理，如没有识别到任何商品
- 按键启动摄像头拍照送图

#### 环境

我自己的电脑环境是**Windows10 + Pycharm + OpenCV 3.4.2** ，不知道其它系统或IDE行8行，不行再改.

#### Reference

https://ai.baidu.com/ai-doc/FACE/ek37c1qiz