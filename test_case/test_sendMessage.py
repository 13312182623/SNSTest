# coding=utf-8
import requests
import unittest
from test_case import snsLogin

header = snsLogin


class SendMessageTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://test.wanfangdata.com.cn/sns/sendMsg'

    def test_message_cad(self):
        self.data = {"message": "cad", "messagesText": "cad"}
        message_result = requests.post(self.url, self.data, cookies=header.user_normal.cookies)
        result = message_result.json()
        self.assertEqual(result['successText'], "发送成功")
        self.assertEqual(result['status'], 200)

    def test_message_no_cookies(self):
        self.data = {"message": "cad", "messagesText": "cad"}
        message_result = requests.post(self.url, self.data)
        self.assertEqual(message_result.json()['status'], 401)
        self.assertEqual(message_result.json()['errMsg'], '没有检测到登录用户，请登录后重试')

    def test_message_no_params(self):
        self.data = {"message": "", "messagesText": ""}
        message_result = requests.post(self.url, self.data, cookies=header.user_normal.cookies)
        self.assertEqual(message_result.json()['status'], 400)
        self.assertEqual(message_result.json()['errMsg'], "发送失败")

    def test_message_sensitive_params(self):
        self.data = {"message": "法轮功", "messagesText": "法轮功"}
        message_result = requests.post(self.url, self.data, cookies=header.user_normal.cookies)
        self.assertEqual(message_result.json()['status'], 501)
        self.assertEqual(message_result.json()['errMsg'], '消息内容疑似有敏感信息')

    def test_message_user_noJurisdiction(self):
        self.data = {"message": "cad", "messagesText": "cad"}
        message_result = requests.post(self.url, self.data, cookies=header.user_noJurisdiction.cookies)
        self.assertEqual(message_result.json()['status'], 402)
        self.assertEqual(message_result.json()['errMsg'], '您没有操作权限')
