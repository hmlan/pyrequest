import requests
import hashlib
import unittest
class Jwt(unittest.TestCase):
   def setUp(self):
       md5 = hashlib.md5()
       phone = "13981401923"
       password = "123456"
       url = "http://172.18.0.50/common/merchant_shop_user_login"
       md5.update(password.encode(encoding="utf-8"))
       password_md5 = md5.hexdigest().upper()
       body_raw = {"phone": phone, "password": password_md5, "telephoneCode": "+86"}
       r = requests.post(url, json=body_raw)
       self.jwt = r.json()['data']['jwt']
       print(self.jwt)
       