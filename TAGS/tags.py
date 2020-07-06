# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zachary

import os

def listdir(*names):
    if len(names) == 0:
        return ""
    else:
        allList = []
        for name in names:
            fileAndDirString = os.popen('ls '+name).read()
            # print(fileAndDirString)
            fileAndDirStringDo = fileAndDirString.split("\n")
            # print('##list:')
            for f in fileAndDirStringDo:
                if '.' in f:
                    allList.append(f.split(' ')[-1])
                    # print(f)
    return allList

def help():
    print('='*50)
    print('$ all：全文件夹读取')
    print('$ at：（all tags）统计当前配置的全部标签')
    print('$ +：交集模式\n$ /：并集模式')
    print('$ -：排除模式')
    print('$ new：给缓存文件夹所有文件名开头添加一个标签')
    print('$ cut：删除文件名中的特定标签')
    print('$ fcut：修建文件本名')
    print('$ replace(该命令已失效)：替换缓存文件夹文件名中某个标签。格式：旧标签.新标签')
    print('$ get: 将缓存文件夹中的快捷方式提取为文件')
    print('$ same：图片查重')
    print('$ c：清空缓存文件夹\n$ op：打开源文件夹')
    print('$ call：清空所有缓存文件夹')
    print('$ opc：打开缓存文件夹')
    print('$ code：打开源码\n$ p：打开源码文件夹')
    print('$ tag：获取标签信息文件\n$ tree：打开标签树')
    print('$ info：显示源文件夹信息')
    print('$ @：(Account Tag)统计符合条件的图片数量')
    print('$ pi：显示分类分布饼状图')
    print('$ d-：提取已经画过的图片')
    print('$ cg：更改源目录和缓存目录')
    print('$ sq：筛选图片朝向。o方形、m横屏、l竖屏')
    print('='*50)
# os.system('mkdir test')
# os.system('cp [-s] a.jpg test/')

def clear_cash(path):
    flist = listdir(path)
    for f in flist:
        if f != '':
            print('removing:#'+f+'#')
            os.system('rm '+path+'/'+f)
# clear_cash('test')

def clean(l):
    img = ['JPG','jpg','GIF','gif','jpeg','PNG','png','webp','jfif']
    new = []
    for i in l:
        if i != '':
            if '.' in i:
                type = i.split('.')[-1]
            else:
                type = ''
            if type in img:
                new.append(i)
    return new

def addtag(tags,v_path):
    Tags = tags.split('.')
    f_list = clean(listdir('..'))
    c_list = []
    for tag in Tags:	#一个一个目标标签来
        for file_name in f_list:
            file_tag = file_name.split('.')
            if tag in file_tag:
                c_list.append(file_name)
        f_list = c_list[:]
        c_list = []
    # for i in f_list:
        # print(i)
    # print('*'*50)
    print('\n')
    if f_list:
        for t in range(len(f_list)):
            oldfname = '/'.join(os.getcwd().split('/')[:-1]) + '/' + f_list[t]
            percent = int(((t+1)/len(f_list)*100)/5)
            perc = 'X'*percent+'O'*(20-percent)
            print('\rLoading>>'+perc+'<<',end='')
            newfpath = os.getcwd() + '/' + v_path + '/'
            os.system('cp '+oldfname+' '+newfpath)
    print('\n')
addtag('anqr','cash/cash0')
# print(os.getcwd())
