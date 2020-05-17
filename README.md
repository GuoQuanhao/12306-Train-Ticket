# 12306-Train-Ticket
Get train ticket information via Python crawler
# 12306火车票爬取
## 特别说明
本次案例根据 《零基础学 Python》修改而来，在原案例中，由于书本原案例是 2018 年编写的代码，随着 12306 的迭代更新，就的爬取方式不在适用，**本次主要修改的是 query函数，修改了爬取方式，界面布局等**
## Pycharm 配置 Qt
### Pycharm 下载
Pycharm 点击[此处](https://www.jetbrains.com/pycharm/)进入下载官网
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020051713504730.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NTY3NDI3,size_16,color_FFFFFF,t_70)
Pycharm 提供[专业版](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows)（Professional）与[社区版](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC)（Community），社区版免费且开源，专业版具有 30 天试用期，需要付费购买，可以使用支付宝支付，我使用的是专业版 `pycharm-professional-2020.1.1`
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200517135517384.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NTY3NDI3,size_16,color_FFFFFF,t_70)
### Qt 安装与配置
通过如下命令安装

```powershell
!pip install PyQt5
```
**注：我是用的是 Anaconda 环境配置，下面的路径选择根据自己电脑路径修改**

配置三个扩展工具 External Tools，依次点击 File→Settings→External Tools，点击＋号，三个工具的配置输入如下：
**Qt Designer:用于绘制界面**
|属性| 参数 |
|--|--|
| Name | Qt Designer(自己取名字) |
| Description | Create Qt UI(描述信息，可以不写) |
| Program | E:\Anaconda3\Library\bin\designer.exe(根据自己Python环境填写路径) |
| Arguments | 无 |
| Working directory | E:\Anaconda3\Library\bin |
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200517140025297.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NTY3NDI3,size_16,color_FFFFFF,t_70#pic_center)
**PyUIC:将 UI 界面转换为 Python 可识别的代码**
|属性| 参数 |
|--|--|
| Name | PyUIC(自己取名字) |
| Description | UI to py file(描述信息，可以不写) |
| Program | E:\Anaconda3\envs\tensorflow1.x\python.exe(根据自己Python环境填写路径) |
| Arguments | -m PyQt5.uic.pyuic \$FileName\$ -o \$FileNameWithoutExtension\$.py|
| Working directory | \$FileDir\$ |
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200517140534152.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NTY3NDI3,size_16,color_FFFFFF,t_70#pic_center)
**qrc2py:将需要用到的资源文件转换成 Python 可识别文件（在设置 UI 时可以在 UI 转换成 py 文件后手动添加资源文件，但过程相较于繁琐，此处采取在编辑UI时直接添加资源文件）**
|属性| 参数 |
|--|--|
| Name | qrc2py(自己取名字) |
| Description | 无(描述信息，可以不写) |
| Program | E:\Anaconda3\envs\tensorflow1.x\Scripts\pyrcc5.exe(根据自己Python环境填写路径) |
| Arguments | \$FileName\$ -o \$FileNameWithoutExtension\$_rc.py|
| Working directory | \$FileDir\$ |
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200517140825705.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NTY3NDI3,size_16,color_FFFFFF,t_70#pic_center)
配置完成后如下
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200517140839548.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NTY3NDI3,size_16,color_FFFFFF,t_70#pic_center)
### 界面绘制
打开配置的扩展工具 Qt Designer
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200517141006663.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NTY3NDI3,size_16,color_FFFFFF,t_70)
绘制 UI 界面部分需要具备基本的 Qt 操作，左边是界面布局的一些按钮，控件等，右边是调节控件的参数例如命名，大小等，界面使用了添加资源文件，所以后面需要将生成的 qrc 文件转换，界面如何绘制不再赘述，界面如图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200517141344784.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NTY3NDI3,size_16,color_FFFFFF,t_70)
绘制完界面后，点击如下，将界面转换成 py 文件，UI 文件名与 py 文件名相同，都为 MianWindow
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020051714143035.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NTY3NDI3,size_16,color_FFFFFF,t_70)
转换 qrc 文件类似上面转换 UI 操作，转换后需要在 MianWindow.py 中加入：

```powershell
import source_rc
```
## 代码文件
主要的程序文件如下
### MianWindow.py
主程序
### query_request.py
解析程序
### get_stations.py
站点程序
## Pyinstaller 程序打包
### 直接运行
运行主程序如下
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200517142517387.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NTY3NDI3,size_16,color_FFFFFF,t_70)
### 打包运行
程序打包后运行出错参见参见[pygame 实现 flappybird 并打包成 exe 运行文件](https://blog.csdn.net/qq_39567427/article/details/104373140)与[使用 Pygame 创建五子棋游戏](https://blog.csdn.net/qq_39567427/article/details/104538053)解决方案
在命令行直接输入：

```powershell
pyinstaller -F -w -i logo.ico main.py
```
打包运行效果如下：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200517144114954.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NTY3NDI3,size_16,color_FFFFFF,t_70)
## （附）简单爬取操作
进入 [12306](https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc) 车票查询官网，输入北京到上海如下图所示
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200517143046781.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NTY3NDI3,size_16,color_FFFFFF,t_70)
按 F12，再按 F5  刷新(刷新后可能需要重新点击查询)，最终界面应如下，其中包含了大量信息，除了车次信息还有网页的图片文件信息等：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200517143229579.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NTY3NDI3,size_16,color_FFFFFF,t_70)
找到代表车次信息的信息条，名称大致为 query?leftTicketDTO.train_date=2020-05-17&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT（不同的时间可能不同）
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020051714342025.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NTY3NDI3,size_16,color_FFFFFF,t_70)
Headers 与 Response 选项卡就是我们需要的信息，Headers 里面包含了 Cookie 文件，消息头，User-Agent 等，Response  则是包含了车次信息，里面包含站点信息，时间，座位信息以及一些反爬的混淆信息，我们需要适用正则化，字符串处理方法等提取信息，具体操作参见 query_request.py
