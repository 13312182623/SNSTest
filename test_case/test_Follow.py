import unittest
import requests
from test_case import snsLogin

header = snsLogin
filename = "../data/userId.txt"
with open(filename) as file_object:
    contest = file_object.read().splitlines()
    print(contest)


class WeatherTest(unittest.TestCase):
    def setUp(self):
        self.addUrl = 'http://test.wanfangdata.com.cn/sns/addFolw'
        self.canUrl = 'http://test.wanfangdata.com.cn/sns/cancelFolw'

    def test_canFollow_normal_params(self):
        self.data = {'targetId': 'morefans'}
        r = requests.get(self.addUrl, params=self.data, cookies=header.user_normal.cookies)
        print(r.text)
        print(self.data)

    def test_canFollow_no_params(self):


    def test_addFollow_normal_params(self):
        self.data = {'targetId': 'morefans'}
        r = requests.get(self.addUrl, params=self.data, cookies=header.user_normal.cookies)
        print(r.text)
        print(self.data)

    def test_addFollow_more_params(self):
        for value in contest:
            self.data = {'targetId': value}
            r = requests.get(self.addUrl, params=self.data, cookies=header.user_normal.cookies)
            print(r.text)
            print(self.data)
