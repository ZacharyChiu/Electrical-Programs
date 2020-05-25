# Electrical-Programs
> 本仓库记录我的电子相关项目。

# 目录
[树莓派](#树莓派)  
[扩展](#扩展)

## 树莓派
### 基本操作
#### 开始前的一些事
- **注意事项**
1. 经常负载运行，SoC发热严重。最好配备散热片，风扇。
2. 4b功耗比3系大好几倍，若用电池供电，略显吃力。
3. 若希望通过远程桌面控制树莓派，需安装带桌面的镜像（with desktop）
#### 系统安装
- **参考教程**  
[树莓派RASPBIAN系统安装个人经验教训 | CSDN](https://blog.csdn.net/piaoyangguohai1/article/details/79596859
)  
[树莓派上安装tensorflow | 360图书馆](http://www.360doc.com/content/19/0810/12/13145302_854037777.shtml)

- **Raspbian**
> Raspbian是专门针对树莓派而优化的Linux系统。  
- **安装**
> - **所需工具**  
> 1. SD卡格式化工具：`SDCardFormatter`
> 2. 镜像烧录工具：`win32diskimager`
> 3. SD卡
> - **流程**
> 1. 获取镜像文件。（已上传至我的百度网盘）  
> 注意将镜像文件保存在全英文路径下。  
> 2. 使用格式化工具将SD卡格式化  
> 3. 烧写镜像  
> 跳出的弹窗中不要点击格式化（会烧录失败）  
> 4. 简单配置  
> 烧写完后，在boot分区，建立一个“内容空白”的txt文件，文件名字是 ssh，然后把后缀 .txt 删除。
### 扩展
#### 微雪4.3寸电纸屏
> 4.3寸 串口电子墨水屏模块 800×600分辨率 黑白  
> 内置128MB NandFlash，字库和图片数据既可以存储于外部TF卡，也可导入到内部NandFlash  
> 型号 4.3inch e-Paper UART Module  
> ![微雪电纸屏](http://file.elecfans.com/web1/M00/AC/E7/pIYBAF3C01uAZR2qAADyaB2Wwz4369.jpg)
> ![背面](http://file.elecfans.com/web1/M00/AC/E7/pIYBAF3C01yASZO7AAIKgw1mKHM545.jpg)
> - **资料**  
> [微雪电子4.3寸电子纸墨水屏简介 | 电子说](http://www.elecfans.com/d/1106427.html)
#### 二哈识图（HuskyLens）
> - **一句话**  
> 人工智能摄像头传感器。 -- `¥329`
> - **简介**  
> 这款传感器据说是国内第一款使用K210处理器芯片的AI视觉传感器，来自于一家叫做DFRobot的公司，而且从介绍来看，集人脸识别、物体识别、物体追踪、颜色识别、巡线、二维码标签识别6大功能于一身。  
> [B站演示视频](https://www.bilibili.com/video/BV1di4y1t7KS) <-戳我  
> ![HuskyLens](https://bkimg.cdn.bcebos.com/pic/4d086e061d950a7b8a00f19d05d162d9f2d3c9b6?x-bce-process=image/watermark,g_7,image_d2F0ZXIvYmFpa2UxMTY=,xp_5,yp_5)  
> - **资料**  
> [HUSKYLENS人工智能摄像头是什么？详细介绍 | 豆瓣](https://www.douban.com/note/748920278/)


