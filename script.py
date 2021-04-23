# coding: utf-8
import uiautomator2 as u2
from datetime import datetime
import time, random, os


def double_click():
    i = 0
    i += 1
    delay = random.uniform(0.1, 0.5)
    time.sleep(delay)
    randomX = str(random.randint(-15, 15) + 1015)
    randomY = str(random.randint(-20, 20) + 1730)
    cmd = 'adb shell input tap ' + randomX + ' ' + randomY
    os.popen(cmd)
    logger('已点赞 {}次 ！点击坐标为{}{}'.format(i,randomX,randomX))


def adb_swipe_b2t(n, time_count, name):
    x1 = round(350 + random.uniform(-5, 5), 2)
    y1 = round(1580 + random.uniform(-6, 6), 2)
    x2 = round(350 + random.uniform(-8, 8), 2)
    y2 = round(900 + random.uniform(-7, 7), 2)
    step_ = round(200 + random.randint(-9, 9), 2)
    time_sleep = random.uniform(6, 8)
    os.system("adb shell input swipe {} {} {} {} {}".format(x1, y1, x2, y2, step_))
    logger('正在看{}第{}个视频！看{}秒！总共观看{}分钟'.format(name, n, time_sleep, round(time_count / 60, 2)))
    time.sleep(time_sleep)
    return time_sleep


def adb_swipe_r2l(n,time_count,name):
    x1 = round(912+random.uniform(-5,5),2)
    y1 = round(990+random.uniform(-6,6),2)
    x2 = round(128+random.uniform(-8,8),2)
    y2 = round(800+random.uniform(-7,7),2)
    step_ = round(200+random.randint(-9,9),2)
    time_sleep = random.uniform(6,8)
    os.system("adb shell input swipe {} {} {} {} {}".format(x1,y1,x2,y2,step_))
    logger('正在看{}第{}个视频！看{}秒！总共观看{}分钟'.format(name,n,time_sleep,round(time_count/60,2)))
    time.sleep(time_sleep)
    return time_sleep



def logger(msg):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(current_time, msg)


def check_time(name,first_time,now_time):
    if name == 'weishi':
        if (now_time - first_time).seconds <= 2700:
            return True
        else:
            return False
    elif name == 'douyin':
        if (now_time-first_time).seconds <= 2700:
            return True
        else:
            return False
    elif name == 'toutiao':
        if (now_time-first_time).seconds <= 2700:
            return True
        else:
            return False
    elif name == 'kuaishou':
        return True
def ramdom_dpuble_click():
    random_num = random.randint(1,20)
    if random_num == 1 or random_num == 20:
        double_click()
        

first_time = datetime.now()
now_time = datetime.now()
n = 1
time_count = 1
d = u2.connect()
os.system('adb shell settings put system screen_brightness {}'.format(1))

#微视
def weishi():
    d.app_stop("com.tencent.weishi")
    d.app_start("com.tencent.weishi")
    time.sleep(8)
    first_time = datetime.now()
    now_time = datetime.now()
    n = 1
    time_count = 1

    while check_time('weishi',first_time,now_time):
        ramdom_dpuble_click()
        time_sleep = adb_swipe_b2t(n, time_count, '微视')
        now_time = datetime.now()
        n = n+1
        time_count = time_count +time_sleep

#抖音

def douyin():
    d.app_stop("com.tencent.weishi")
    d.app_stop("com.ss.android.ugc.aweme.lite")
    d.app_start("com.ss.android.ugc.aweme.lite")
    time.sleep(8)
    first_time = datetime.now()
    now_time = datetime.now()
    n = 1
    time_count = 1
    while check_time('douyin',first_time,now_time):
        ramdom_dpuble_click()
        time_sleep = adb_swipe_b2t(n, time_count, '抖音')
        now_time = datetime.now()
        n = n+1
        time_count = time_count +time_sleep

    d.app_stop("com.ss.android.ugc.aweme.lite")


#今日头条
def toutiao():
    d.app_stop("com.ss.android.ugc.aweme.lite")
    d.app_stop("com.ss.android.article.lite")
    d.app_start("com.ss.android.article.lite")
    time.sleep(8)
    first_time = datetime.now()
    now_time = datetime.now()
    n = 1
    time_count = 1
    d.click(479.0, 2250.0)  # 点击，抢购按钮
    time.sleep(2)
    d.click(99.0, 1559.0)  # 点击，抢购按钮
    time.sleep(2)
    d.click(99.0, 1559.0)  # 点击，抢购按钮
    while check_time('toutiao',first_time,now_time):
        time_sleep = adb_swipe_r2l(n, time_count, '今日头条')
        ramdom_dpuble_click()
        now_time = datetime.now()
        n = n+1
        time_count = time_count +time_sleep

#快手
def kuaishou():
    d.app_stop("com.ss.android.article.lite")
    d.app_stop("com.kuaishou.nebula")
    d.app_start("com.kuaishou.nebula")
    time.sleep(8)
    first_time = datetime.now()
    now_time = datetime.now()
    n = 1
    time_count = 1
    while check_time('kuaishou',first_time,now_time):
        ramdom_dpuble_click()
        time_sleep = adb_swipe_b2t(n, time_count, '快手')
        now_time = datetime.now()
        n = n+1
        time_count = time_count +time_sleep

    d.app_stop("com.kuaishou.nebula")

weishi()
douyin()
toutiao()
kuaishou()
