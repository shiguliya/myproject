import random
import requests
import time
import json
import hashlib

class Youdao():
    def __init__(self,content):
        self.content=content
        self.url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.ts=self.get_ts()
        self.salt=self.get_salt()
        self.sign=self.get_sign()

    def get_salt(self):
        return self.ts + str(random.randint(0, 10))

    def get_md5(self,value):
        m = hashlib.md5()
        m.update(value.encode("utf-8"))
        return m.hexdigest()

    def get_sign(self):
        s = "fanyideskweb" + self.content + self.salt + "Nw(nmmbP%A-r6U3EUn]Aj"
        return self.get_md5(s)

    def get_ts(self):
        t = time.time()
        return str(int(round(t * 1000)))

    def yield_form_date(self):
        return {
            'i': self.content,
            'form': 'AUTO',
            'to': 'A',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': self.salt,
            'sign': self.sign,
            'ts': self.ts,
            'bv': 'b286f0a34340b928819a6f64492585e8',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME',
        }

    def yield_headers(self):
        return {
            'Cookie': 'OUTFOX_SEARCH_USER_ID=965353655@10.108.160.102;OUTFOX_SEARCH_USER_ID_NCOO=302512989.4509335;JSESSIONID=aaalS99rL0Ih2figoEOhx;___rl__test__cookies=1588743363757',
            'Referer': 'http://fanyi.youdao.com',
            'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/81.0.4044.129Safari/537.36',
        }

    def fanyi(self):
        response = requests.post(self.url, data=self.yield_form_date(), headers=self.yield_headers())
        content=json.loads(response.text)
        return content['translateResult'][0][0]['tgt']

if __name__ == '__main__':
    while(True):
        try:
            i=input("please input : ")
            youdao=Youdao(i)
            print("fanyi result : ",youdao.fanyi())
        except:
            pass