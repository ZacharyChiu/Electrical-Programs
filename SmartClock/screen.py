# coding: utf-8
# 智能时钟程序
# 创建者：Zachary
# 测试环境：Win10
# coding: utf-8
# 若运行失败，尝试安装‘lxml’库
import pygame
from pygame.locals import *
import datetime
import time
import requests
from urllib import request
from bs4 import BeautifulSoup
import sys 
from ctypes import windll 
import os
def show_time():
    cur_time = datetime.datetime.now()	# 数据类型为：datetime
    time = str(cur_time).split('.')[0]
    return time
def show_weather(city):
    url = 'https://tianqi.moji.com/weather/china/jiangsu/' + city
    htmlData = request.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(htmlData, 'lxml')
    # print(soup.prettify())
    weather = soup.find('div',attrs={'class':"wea_weather clearfix"})
    T = weather.find('em').get_text()
    W = weather.find('b').get_text()
    weather = '宜兴 '+T+'℃ '+W
    return weather


# 打印数字
def resizeimg(oimg,height):
    size = oimg.get_rect()
    w = size[2]
    h = size[3]
    # print(w,h)
    width = int(height / h * w)
    return pygame.transform.smoothscale(oimg, (width, height))
pygame.init()
# os.environ['SDL_VIDEO_CENTERED'] = '1' #居中显示
screen = pygame.display.set_mode((400,190),NOFRAME)
pygame.display.set_caption("Smart Clock")
font = pygame.font.Font('C:\\Windows\\Fonts\\msyh.ttc', 36)
weatherlogo1 = pygame.image.load('img\\雷阵雨.jpg')

# 窗口最前端显示
SetWindowPos = windll.user32.SetWindowPos
x,y = 0,0 # 窗口显示坐标
SetWindowPos(pygame.display.get_wm_info()['window'], -1, x, y, 0, 0, 0x0001)

# print( pygame.display.Info() )

while True:
    
    #监听退出事件
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    screen.fill((5,33,63))
    
    # 生成文字
    date = font.render(show_time().split(' ')[0], True, (255,255,255))
    time = font.render(show_time().split(' ')[1], True, (255,255,255))
    weather_text = show_weather('yixing')
    weathertype = weather_text.split('℃')[1]
    weather = font.render(weather_text, True, (255,255,255))
    
    timew = time.get_rect()[2]
    timeh = time.get_rect()[3]
    weatherlogo1 = pygame.transform.smoothscale(weatherlogo1, (timeh+10, timeh+10))
    # print(time.get_rect())
    
    
    
    screen.blit(date, (90,0))
    screen.blit(time, (90,50))
    screen.blit(weather, (90,100))
    screen.blit(weatherlogo1, (90+timew+25,50))
    
    pygame.display.update()
