# coding=utf-8
import requests
import xlrd
import urllib.request
import http.cookiejar

url = "http://my.test.wanfangdata.com.cn/auth/user/grredirectlogin.do"

data_normal = {"username": "test1", "password": "ffffff"}
user_normal = requests.Session()
r = user_normal.post(url, data=data_normal, headers={})

data_noJurisdiction = {"username": "test_sns1", "password": "ffffff"}
user_noJurisdiction = requests.Session()
r = user_noJurisdiction.post(url, data=data_noJurisdiction, headers={})
