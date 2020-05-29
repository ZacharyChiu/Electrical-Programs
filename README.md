# Electrical-Programs
> 本仓库记录我的树莓派项目。

# 目录
* [树莓派](#树莓派)  
    * [基本操作](#基本操作)  
        * [开始前的一些事](#开始前的一些事)  
        * [系统安装](#系统安装)  
    * [扩展](#扩展)  
        * [微雪电纸屏](#微雪电纸屏)  
        * [二哈识图](#二哈识图)  
* [Raspbian](#Raspbian)
* [项目](#项目)
    * [SmartClock](#SmartClock)

# 树莓派
[返回目录](#目录)
## 基本操作
### 开始前的一些事
* **注意事项**
1. 经常负载运行，SoC**发热**严重。最好配备散热片，风扇。
2. 4b**功耗**比3系大好几倍，若用电池供电，略显吃力。
3. 若希望通过**远程桌面**控制树莓派，需安装带桌面的镜像（with desktop）
### 系统安装
* **参考教程**  
[树莓派首次启动无屏幕解决方案 |CSDN](https://blog.csdn.net/weixin_43282511/article/details/90453295)  
[树莓派第一次配置+装系统+远程连接+WiFi连接 | CSDN](https://blog.csdn.net/qq_28821995/article/details/83185618)  
[树莓派RASPBIAN系统安装个人经验教训 | CSDN](https://blog.csdn.net/piaoyangguohai1/article/details/79596859)  
[树莓派上安装tensorflow | 360图书馆](http://www.360doc.com/content/19/0810/12/13145302_854037777.shtml)

* **Raspbian**
> Raspbian是专门针对树莓派而优化的Linux系统。  
* **安装**
> * **所需工具**  
> 1. SD卡格式化工具：`SDCardFormatter`  
> ![SD格式化工具](http://img4.imgtn.bdimg.com/it/u=2206007037,16898101&fm=15&gp=0.jpg)
> 2. 镜像烧录工具：`win32diskimager`  
> ![镜像烧录工具](http://img5.imgtn.bdimg.com/it/u=3214485409,2704380398&fm=26&gp=0.jpg)
> 3. SD卡  
> 4. IP搜索软件：Advanced IP Scanner  
> ![IP搜索软件](http://img4.imgtn.bdimg.com/it/u=1078071457,2542206237&fm=15&gp=0.jpg)  
> * **流程**
> 1. 获取镜像文件。（已上传至我的百度网盘）  
> 注意将镜像文件保存在全英文路径下。  
> 2. 使用格式化工具将SD卡格式化  
> 3. 烧写镜像  
> 跳出的弹窗中不要点击格式化（会烧录失败）  
> 4. 简单配置  
> 烧写完后，在boot分区，建立一个“内容空白”的txt文件，文件名字是 ssh，然后把后缀 .txt 删除。  
> 5. 安装系统 
> 插入SD卡，给树莓派接通电源。
> 观察树莓派指示灯判断树莓派是否工作正常。  
> 指示灯信号所代表的意思参考[树莓派LED指示灯状态的解释 | 树莓派实验室](https://shumeipai.nxez.com/2014/09/30/raspberry-pi-led-status-detail.html?variant=zh-cn)
> 6. 配置远程桌面  
> (1) 树莓派接鼠标、键盘、屏幕，连接wifi。  
>> 方法一：直接使用图形界面右上角的图标连接WiFi（与windows系统类似）  
>> ![连WiFi](http://img1.imgtn.bdimg.com/it/u=2232326196,3954081989&fm=26&gp=0.jpg)  
>  
>> 方法二：(没有屏幕)
>> * 开启PC的热点，设置热点名称（不要包含中文）和密码
>> * 将Raspbian系统镜像写入SD卡后，在SD卡的boot分区新建文件名为`wpa_supplicant.conf`的文件，文件中写入如下代码：  
```
country=GB
 
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
 
update_config=1
 
network={
 
    ssid="你的Wifi名称，注意大小写"
 
    psk="你的Wifi密码"
 
}
```
>> 上述文件即WiFi配置文件，使树莓派根据它来自动连接WiFi。  
>> * 在PC上弹出SD卡，把SD卡插到树莓派，上电。 
>> * 此时，树莓派会连接笔记本的热点，在笔记本上可以看到树莓派的IP地址。
>> * Win10系统，按“Win+R”调出“运行”程序，输入“mstsc”，回车后，打开了Win10的远程桌面。  
>> 随后输入树莓派的IP地址。  
>> 在登录到xrdp窗口中，默认选择的是Xorg（有的是sesman-Xvnc）  
>> 用户名：pi  
>> 密码：raspberry

## 扩展
### 微雪电纸屏
[返回目录](#目录)
> 4.3寸 串口电子墨水屏模块 800×600分辨率 黑白  
> 内置128MB NandFlash，字库和图片数据既可以存储于外部TF卡，也可导入到内部NandFlash  
> 型号 4.3inch e-Paper UART Module  
> ![微雪电纸屏](http://file.elecfans.com/web1/M00/AC/E7/pIYBAF3C01uAZR2qAADyaB2Wwz4369.jpg)
> ![背面](http://file.elecfans.com/web1/M00/AC/E7/pIYBAF3C01yASZO7AAIKgw1mKHM545.jpg)
> * **资料**  
> [微雪电子4.3寸电子纸墨水屏简介 | 电子说](http://www.elecfans.com/d/1106427.html)
### 二哈识图
[返回目录](#目录)
> * **一句话**  
> 人工智能摄像头传感器。 -- `¥329`
> * **简介**  
> 这款传感器据说是国内第一款使用K210处理器芯片的AI视觉传感器，来自于一家叫做DFRobot的公司，而且从介绍来看，集人脸识别、物体识别、物体追踪、颜色识别、巡线、二维码标签识别6大功能于一身。  
> [B站演示视频](https://www.bilibili.com/video/BV1di4y1t7KS) <-戳我  
> ![HuskyLens](https://bkimg.cdn.bcebos.com/pic/4d086e061d950a7b8a00f19d05d162d9f2d3c9b6?x-bce-process=image/watermark,g_7,image_d2F0ZXIvYmFpa2UxMTY=,xp_5,yp_5)  
> * **资料**  
> [HUSKYLENS人工智能摄像头是什么？详细介绍 | 豆瓣](https://www.douban.com/note/748920278/)

# Raspbian
Linux系统`Raspbian`的使用方法。
## 常用命令
### 文件管理
* **列出文件夹内容**:`ls`
* **创建文件夹**:`mkdir`
* **创建文件**：`touch`
## 应用程序
### nano
nano是一个字符终端的文本编辑器。  

## 参考资料
[详解linux中nano命令 | CSDN](https://blog.csdn.net/a4132447/article/details/95531532)
[Linux简单指令学习 | CSDN](https://blog.csdn.net/qyx635804080/article/details/87625422)
# 项目
## SmartClock
[返回目录](#目录)
### 功能  

显示时间 |倒计时| 闹钟 | 显示阴历
-----|-----|-----|-----
显示天气|显示室内温度|显示室内湿度|
  
## Siri+Raspberry
**资料**  
[超简单的私人语音助手:用Siri让你的树莓派做任何事 | 哔哩哔哩](https://www.bilibili.com/video/BV1x5411s7gE?t=5)
