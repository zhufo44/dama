import requests,re
from time import sleep

'''
易码短信平台  http://www.51ym.me/User/Default.aspx
账号: zhufo44  密码：123456as
itemid  每一个项目的编号，在平台搜索
'''

#项目编号--京东金融
itemid = 16359
ymtoken = '00899695b25c917c557a6277122427141720568a4601'

#获取手机号--只返回手机号
def getphone():
    url = 'http://api.fxhyd.cn/UserInterface.aspx?action=getmobile&token={}&itemid={}&excludeno=170.171.180'.format(ymtoken,itemid)
    res = requests.get(url).content.decode('utf8')
    phone = res.replace('success|','').strip()
    return phone

#获取验证码--1，返回'fail'表示验证码获取失败,2，正确返回，具体验证码需要具体提取
def getyanzhen(phone):
    url = 'http://api.fxhyd.cn/UserInterface.aspx?action=getsms&token={}&itemid={}&mobile={}&release=1'.format(ymtoken,itemid,phone)
    count = 0
    while True:
        sleep(5)
        yanzhen = requests.get(url).content.decode('utf8','ignore')
        print('验证信息',yanzhen)
        if count>15:
            print('接受不到短信')
            return 'fail'
        if yanzhen == '3001':
            print('再等等，还没收到短信')
            count+=1
            continue
        if re.findall(r'验证码',yanzhen):
            break
        if yanzhen == '2007':
            print('号码失效，已被释放')
            return 'fail'
    return yanzhen
