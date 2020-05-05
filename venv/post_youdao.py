import random
import requests
import time


# url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
# content="我和你"

class Youdao():
    def __init__(self,content):
        self.content=content
        self.url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.ts=self.get_ts()
        self.salt=self.get_salt()
        self.sign=self.get_sign()

    def get_salt(self):
        s=str(random.randint(0,10))
        t=self.ts
    # print("random =",s)
    # print("ts= ",t)
    # print("salt= ",t+s)
        return t+s
    # return '15874584542121'


    def get_md5(self,value):
        import hashlib
        m = hashlib.md5()
        m.update(value.encode("utf-8"))
        return m.hexdigest()

    def get_sign(self):
        i=self.salt
        e=self.content
        s="fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj"
        return self.get_md5(s)
    # return 'c5a48d9dbfcfd12fca25371c0624b210'


    def get_ts(self):
        t = time.time()
        ts = str(int(round(t * 1000)))
        print("ts=",ts)
        return ts


    # def get_content(self):
    #     return content

    def yield_form_date(self):
        form_date={
            'i':self.content,
            'form':'AUTO',
            'to':'A',
            'smartresult':'dict',
            'client':'fanyideskweb',
            'salt': self.salt,
            'sign': self.sign,
            'ts': self.ts,
            'bv':'aba2eb413aab2b3c6b790cc4b2ce2dc8',
            'doctype':'json',
            'version':'2.1',
            'keyfrom':'fanyi.web',
            'action':'FY_BY_REALTlME',
        }
        return form_date



    def get_headers(self):
        headers={
            'Cookie':'OUTFOX_SEARCH_USER_ID=9653OUTFOX_SEARCH_USER_ID=965353655@10.108.160.102;OUTFOX_SEARCH_USER_ID_NCOO=302512989.4509335;JSESSIONID=aaa6asR8Jfo-scyEVTIhx;___rl__test__cookies=1588646834892',
            'Referer':'http://fanyi.youdao.com/',
            'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/81.0.4044.129Safari/537.36',
        }
        return headers
    #
    # class Youdao():
    #     def __init__(self):
    #     self.get_ts()
    #     self.salt=self.get_salt()
    #     self.salt=self.get_sign()
    #
    #
    # def get_form_date():
    #     return form_date


def fanyi(self):
    response = requests.post(self.url, data=self.yield_form_date(), headers=self.get_headers())
    return response.text()


if __name__ == '__main__':
    # print(form_date)
    # print(get_headers())
    # print(response.text)
    youdao=Youdao('我们')
    print(youdao.fanyi())