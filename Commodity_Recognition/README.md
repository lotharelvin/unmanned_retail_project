# 模拟结算台商品识别 

Author：KCLi2000 likwokc@mail2.sysu.edu.cn

Version:  v0.0.alpha

#### 依赖库

由于baiduAI的在线人脸识别功能要通过URL请求，因此需要调用requests库；同时，baiduAI要求送进图片的格式是base64格式，因此我们需要base64，numpy库来进行图片格式转换。

```
pip install pybase64
pip install requests
pip install python-opencv
pip install urllib
```

#### How to use

- **目前仅支持屈臣氏饮用水280ml，维记鲜奶946ml和宝矿力水特500ml的识别**
- **目前暂时还没有利用摄像头模块，主要是百度AI恰烂钱，调用量有限制。我调试必须保证返回值正常**

```python
#test.py
import defines

image_path = '校验图片路径'
cart = defines.get_cart(image_path)

```

#### Sample Output

```
cart = ['蒸馏水_屈臣氏_280ml', '蒸馏水_屈臣氏_280ml', '蒸馏水_屈臣氏_280ml', '鲜奶_维记_946ml', '宝矿力水特_宝矿力水特_500ml']
```

#### 版本历史

| 版本       | 版本改动内容概要                           |
| ---------- | :----------------------------------------- |
| v0.0.alpha | 实现了手动送图的正确识别，并返回购物车列表 |

#### 后续工作

- 对错误输入的处理，如没有识别到任何商品
- 按键启动摄像头拍照送图

#### 环境

我自己的电脑环境是**Windows10 + Pycharm**，不知道其它系统或IDE行8行，不行再改.

#### Reference

https://ai.baidu.com/ai-doc/FACE/ek37c1qiz