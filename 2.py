# -*- encoding=utf8 -*-
__author__ = "liu123"

from airtest.core.api import *

import os

auto_setup(__file__)

#获取当前路径
path = os.getcwd()

#定义存放文件名
files = 'user.txt'

#判断存放账号密码文件是否存在
if not os.path.exists(files):
        file = open(path + '//' + files,'w')
        file.write(f'{input("请输入用户名：")}:{input("请输入密码：")}')

#取出存放的账号和密码    
user_dic =open(path + '//' + files , 'r')
for i in user_dic:
    username,password = i.split(':')

#点击米游社
touch(Template(r"tpl1711640152385.png", record_pos=(0.344, 0.021), resolution=(1280, 720)))

sleep(5.0)

#判断是否有青少年弹窗提醒
if exists(Template(r"tpl1711641868370.png", record_pos=(0.006, 0.293), resolution=(720, 1280))):
    touch(Template(r"tpl1711641877785.png", record_pos=(0.0, 0.287), resolution=(720, 1280)))

#判断是否为第一次登陆，同意一系列弹窗协议
if exists(Template(r"tpl1711639914642.png", record_pos=(0.146, 0.299), resolution=(720, 1280))):
        touch(Template(r"tpl1711639914642.png", record_pos=(0.146, 0.299), resolution=(720, 1280)))
        touch(Template(r"tpl1711639918809.png", record_pos=(0.029, 0.789), resolution=(720, 1280)))
        touch(Template(r"tpl1711639923338.png", record_pos=(0.104, 0.287), resolution=(720, 1280)))
        
#点击我的
touch(Template(r"tpl1711639930123.png", record_pos=(0.386, 0.839), resolution=(720, 1280)))


sleep(3.0)

#判断是否需要登陆
if exists(Template(r"tpl1711640246694.png", record_pos=(-0.29, -0.643), resolution=(720, 1280))):
        touch(Template(r"tpl1711640246694.png", record_pos=(-0.29, -0.643), resolution=(720, 1280)))
        sleep(3.0)
        touch(Template(r"tpl1711639948440.png", record_pos=(-0.06, 0.221), resolution=(720, 1280)))
        touch(Template(r"tpl1711639951359.png", record_pos=(-0.111, -0.199), resolution=(720, 1280)))
        text(username)
        touch(Template(r"tpl1711639987784.png", record_pos=(-0.239, -0.074), resolution=(720, 1280)))
        text("password")
        touch(Template(r"tpl1711640342003.png", record_pos=(-0.425, 0.025), resolution=(720, 1280)))
        touch(Template(r"tpl1711640353253.png", record_pos=(0.022, 0.167), resolution=(720, 1280)))
else:
        touch(Template(r"tpl1711640974363.png", record_pos=(-0.386, 0.839), resolution=(720, 1280)))
        
sleep(1.0)
        
#点击签到
touch(Template(r"tpl1711641449135.png", record_pos=(-0.197, -0.657), resolution=(720, 1280)))

sleep(10.0)

#判断当并领取当天签到奖励
if exists(Template(r"tpl1711642531392.png", threshold=0.9, record_pos=(-0.037, -0.204), resolution=(720, 1280))):
        touch(Template(r"tpl1711642672477.png", record_pos=(-0.103, -0.2), resolution=(720, 1280)))
else:
    touch(Template(r"tpl1711642750611.png", record_pos=(0.011, 0.372), resolution=(720, 1280)))
    sleep(1.0)

    if exists(Template(r"tpl1711642531392.png", threshold=0.9, record_pos=(-0.037, -0.204), resolution=(720, 1280))):
            touch(Template(r"tpl1711642672477.png", record_pos=(-0.103, -0.2), resolution=(720, 1280)))
    else:
        swipe(Template(r"tpl1711642861416.png", record_pos=(0.004, 0.732), resolution=(720, 1280)), vector=[0.0008, -0.8014])
        sleep(1.0)

        if exists(Template(r"tpl1711642531392.png", threshold=0.9, record_pos=(-0.037, -0.204), resolution=(720, 1280))):
                touch(Template(r"tpl1711642672477.png", record_pos=(-0.103, -0.2), resolution=(720, 1280)))
        else:
            touch(Template(r"tpl1711642938189.png", record_pos=(0.003, 0.836), resolution=(720, 1280)))
            sleep(1.0)

                
touch(Template(r"tpl1711641502534.png", record_pos=(-0.435, -0.776), resolution=(720, 1280)))

sleep(3.0)

keyevent("3")


