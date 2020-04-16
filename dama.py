import requests,time,json
import hashlib

def CalcSign(pd_id, passwd, timestamp):
    md5     = hashlib.md5()
    md5.update((timestamp + passwd).encode())
    csign   = md5.hexdigest()
    md5     = hashlib.md5()
    md5.update((pd_id + timestamp + csign).encode())
    csign   = md5.hexdigest()
    return csign

'''
	打码平台--斐斐打码   http://www.fateadm.com/user_home.php
	账号：1126760657@qq.com   密码：123456as
    img: 验证码图片bit流数据
	imgtype: 验证码类型--具体到平台去找对应数字代码
	pd_id: 账号id--打码平台可见
	pd_key: 账号key--打码平台可见
    返回timeout或者正确验证码
'''
imgtype = '20400'
def get_captcha(img):
    tm = str(int(time.time()))
    pd_id = '107527'
    pd_key = 'YyfEg6qpXKegJajUPDKJJ1bvrIzQG9Tq'
    sign = CalcSign(pd_id,pd_key,tm)
    header = {
        'User-Agent': 'Mozilla/5.0',
    }
    param = {
        "user_id": pd_id,
        "timestamp": tm,
        "sign": sign,
        "predict_type": imgtype,
        "up_type": "mt"
    }
    files = {
        'img_data':('img_data',img)
    }
    url = 'http://pred.fateadm.com/api/capreg'
    #timeout 延迟过长，验证码会出现过期情况
    try:
        res = requests.post(url,data=param,files=files,headers=header,timeout=30).json()
        print(res)
        code = json.loads(res['RspData'])['result']
    except Exception as e:
        print('验证平台出错',e)
        return 'timeout'
    return code


