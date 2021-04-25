# coding: utf-8
import uiautomator2 as u2
from datetime import datetime
import time, random, os

def like(i, name):
    i = i + 1
    if name == 'weishi':
        d.xpath(
            '//*[@resource-id="com.tencent.weishi:id/rzm"]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.FrameLayout[1]').click()
    elif name == 'douyin':
        d(resourceId="com.ss.android.ugc.aweme.lite:id/ahr").click()
    elif name == 'toutiao':
        d.xpath(
            '//*[@resource-id="com.bytedance.article.lite.plugin.huoshan:id/iv_like_video"]/android.widget.ImageView[1]').click()
    elif name == 'kuaishou':
        d.xpath(
            '//*[@resource-id="com.bytedance.article.lite.plugin.huoshan:id/iv_like_video"]/android.widget.ImageView[1]').click()
    else:
        None
    if name == 'weishi':
        name = '微视'
    elif name == 'douyin':
        name = '抖音'
    elif name == 'toutiao':
        name = '今日头条'
    elif name == 'kuaishou':
        name = '快手'
    else:
        None
    logger(f'已点赞 {name}{i}次 ！'.format(name, str(i)))
    return i

#上下滑动
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

#左右滑动
def adb_swipe_r2l(n, time_count, name):
    x1 = round(912 + random.uniform(-5, 5), 2)
    y1 = round(990 + random.uniform(-6, 6), 2)
    x2 = round(128 + random.uniform(-8, 8), 2)
    y2 = round(800 + random.uniform(-7, 7), 2)
    step_ = round(200 + random.randint(-9, 9), 2)
    time_sleep = random.uniform(6, 8)
    os.system("adb shell input swipe {} {} {} {} {}".format(x1, y1, x2, y2, step_))
    logger('正在看{}第{}个视频！看{}秒！总共观看{}分钟'.format(name, n, time_sleep, round(time_count / 60, 2)))
    time.sleep(time_sleep)
    return time_sleep

#打印
def logger(msg):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(current_time, msg)

#各软件时长
def check_time(name, first_time, now_time):
    if name == 'weishi':
        if (now_time - first_time).seconds <= 2700:
            return True
        else:
            return False
    elif name == 'douyin':
        if (now_time - first_time).seconds <= 2700:
            return True
        else:
            return False
    elif name == 'toutiao':
        if (now_time - first_time).seconds <= 2700:
            return True
        else:
            return False
    elif name == 'kuaishou':
        return True


#点击喜欢
def click_like(i, name):
    random_num = random.randint(1, 10)
    # random_num = 1
    if random_num == 1 or random_num == 10:
        try:
            i = like(i, name)
            return i
        except:
            return i


first_time = datetime.now()
now_time = datetime.now()
n = 1
time_count = 1
d = u2.connect()
os.system('adb shell settings put system screen_brightness {}'.format(10))


# 微视
def weishi():
    d.app_stop("com.tencent.weishi")
    d.app_start("com.tencent.weishi")
    time.sleep(8)
    first_time = datetime.now()
    now_time = datetime.now()
    n = 1
    i = 0
    time_count = 1
    name = 'weishi'
    while check_time(name, first_time, now_time):
        i = click_like(i, name)
        time_sleep = adb_swipe_b2t(n, time_count, '微视')
        now_time = datetime.now()
        n = n + 1
        time_count = time_count + time_sleep


# 抖音
def douyin():
    d.app_stop("com.tencent.weishi")
    d.app_stop("com.ss.android.ugc.aweme.lite")
    d.app_start("com.ss.android.ugc.aweme.lite")
    time.sleep(8)
    first_time = datetime.now()
    now_time = datetime.now()
    n = 1
    i = 0
    name = 'douyin'
    time_count = 1
    while check_time(name, first_time, now_time):
        i = click_like(i, name)
        time_sleep = adb_swipe_b2t(n, time_count, '抖音')
        now_time = datetime.now()
        n = n + 1
        time_count = time_count + time_sleep

    d.app_stop("com.ss.android.ugc.aweme.lite")


# 今日头条
def toutiao():
    d.app_stop("com.ss.android.ugc.aweme.lite")
    d.app_stop("com.ss.android.article.lite")
    d.app_start("com.ss.android.article.lite")
    time.sleep(8)
    first_time = datetime.now()
    now_time = datetime.now()
    n = 1
    i = 0
    name = 'toutiao'
    time_count = 1
    d.click(479.0, 2250.0) 
    time.sleep(2)
    d.click(99.0, 1559.0)
    time.sleep(2)
    d.click(99.0, 1559.0) 
    while check_time(name, first_time, now_time):
        time_sleep = adb_swipe_r2l(n, time_count, '今日头条')
        i = click_like(i, name)
        now_time = datetime.now()
        n = n + 1
        time_count = time_count + time_sleep


# 快手
def kuaishou():
    d.app_stop("com.ss.android.article.lite")
    d.app_stop("com.kuaishou.nebula")
    d.app_start("com.kuaishou.nebula")
    time.sleep(8)
    first_time = datetime.now()
    now_time = datetime.now()
    n = 1
    name = 'kuaishou'
    time_count = 1
    while check_time(name, first_time, now_time):
        i = click_like(i, name)
        time_sleep = adb_swipe_b2t(n, time_count, '快手')
        now_time = datetime.now()
        n = n + 1
        time_count = time_count + time_sleep

    d.app_stop("com.kuaishou.nebula")


weishi()
douyin()
toutiao()
kuaishou()
