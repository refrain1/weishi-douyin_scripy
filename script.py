# coding: utf-8
import uiautomator2 as u2
from datetime import datetime 
import time,random,os

first_time=datetime.now()
now_time = datetime.now()
n = 1
time_count = 1


def adb_swipe(n,time_count,name):
    x1 = round(350+random.uniform(-5,5),2)
    y1 = round(1580+random.uniform(-6,6),2)
    x2 = round(350+random.uniform(-8,8),2)
    y2 = round(900+random.uniform(-7,7),2)
    step_ = round(200+random.randint(-9,9),2)
    time_sleep = round(random.uniform(6,8))
    os.system("adb shell input swipe {} {} {} {} {}".format(x1,y1,x2,y2,step_))
    print('正在看{}第{}个视频！看{}秒！总共观看{}分钟'.format(name,n,time_sleep,round(time_count/60,2)))
    time.sleep(time_sleep)
    return time_sleep

def logger(msg):
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(current_time, msg)

def check_time(name):
    if name == 'weishi':
        if (now_time-first_time).seconds <= 2700:
            return True
        else:
            return False
    elif name == 'douyin':
        return True
        # if (now_time-first_time).seconds <= 20:
        #     return True
        # else:
        #     return False
d = u2.connect()
d.app_stop("com.tencent.weishi")
d.app_start("com.tencent.weishi")
time.sleep(8)
while check_time('weishi'):
    time_sleep = adb_swipe(n,time_count,'微视')
    now_time = datetime.now()

first_time=datetime.now()
now_time = datetime.now()

d.app_stop("com.tencent.weishi")
d.app_start("com.ss.android.ugc.aweme.lite")
time.sleep(8)
n = 1
time_count = 1
while check_time('douyin'):
    time_sleep = adb_swipe(n,time_count,'抖音')
    now_time = datetime.now()
    
d.app_stop("com.ss.android.ugc.aweme.lite")
