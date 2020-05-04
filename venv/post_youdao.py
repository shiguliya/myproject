import requests
url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
    return '15874584542121'


def get_sign():
    return 'c5a48d9dbfcfd12fca25371c0624b210'


def get_ts():
    import time
    t = time.time()
    ts = str(int(round(t * 1000)))
    return ts


form_date={
    'i':'我和你都是中国人',
    'form':'AUTO',
    'to':'A',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt': get_salt(),
    'sign': get_sign(),
    'ts': get_ts(),
    'bv':'aba2eb413aab2b3c6b790cc4b2ce2dc8',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_REALTlME',
}
response=requests.post(url,form_date)
print(response.text)