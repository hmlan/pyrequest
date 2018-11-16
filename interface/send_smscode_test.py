import unittest
import requests
class SendSmscode(unittest.TestCase):
    """测试发送验证码"""
    def setUp(self):
        self.url="http://172.18.0.50/common/smsCode"
    def test_send_smscode_a_first(self):
        """第一次发验证码"""
        body_raw={"phone":"13981401923","telephoneCode":"+86","type":"T_CHANGE_PWD"}
        #r=requests.post(self.url,data=data)
        r=requests.post(self.url,json=body_raw)
        self.result=r.json()
        self.assertEqual(self.result['code'],'200')
        self.assertEqual(self.result['msg'],"验证码已发送")
    def test_send_smscode_b_second(self):
        """第二次发验证码"""
        body_raw={"phone":"13981401923","telephoneCode":"+86","type":"T_CHANGE_PWD"}
        r=requests.post(self.url,json=body_raw)
        self.result=r.json()
        self.assertEqual(self.result['code'],'200')
        self.assertEqual(self.result['msg'],"验证码已发送")
    def test_send_smscode_c_third(self):
        """第三次发验证码"""
        body_raw = {"phone": "13981401923", "telephoneCode": "+86", "type": "T_CHANGE_PWD"}
        r = requests.post(self.url, json=body_raw)
        self.result = r.json()
        self.assertEqual(self.result['code'], '400')
        self.assertEqual(self.result['msg'], "5分钟内只能发送两次")
if __name__ == '__main__':
        unittest.main()
