import unittest
import requests
from test_case import sns_login

header = sns_login
filename = "../data/userId.txt"
with open(filename) as file_object:
    contest = file_object.read().splitlines()
    print(contest)


class WeatherTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://test.wanfangdata.com.cn/sns/cancelFolw'

    def test_weather_beijing(self):
        for value in contest:
            self.data = {'targetId': value}
            r = requests.get(self.url, params=self.data, cookies=header.user_normal.cookies)
            print(r.text)
            print(self.data)
