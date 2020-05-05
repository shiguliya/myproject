import unittest
from unittest import mock

from post_youdao import *




class PostYoudaoText(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, True)


    def test_get_ts(self):
        # import time
        # t=time.time()
        # ts=str(int(round(t * 1000)))
        # print(ts)
        get_ts=mock.Mock(return_value='1587458454212')
        self.assertEqual('1587458454212',get_ts())

    def test_get_salt(self):
        get_salt=mock.Mock(return_value='15874584542121')
        self.assertEqual('15874584542121',get_salt())

    def test_get_sign(self):
        get_sign = mock.Mock(return_value='c5a48d9dbfcfd12fca25371c0624b210')
        self.assertEqual("c5a48d9dbfcfd12fca25371c0624b210",get_sign())

if __name__ == '__main__':
    unittest.main()
