import unittest
import requests
import hashlib
class MerchantShopUserLoginTest(unittest.TestCase):
    """测试seller登录"""
    def setUp(self):
        self.url="http://172.18.0.50/common/merchant_shop_user_login"
        md5=hashlib.md5()
        password="123456"
        sign_bytes_utf8=password.encode('utf8')
        md5.update(sign_bytes_utf8)
        self.sign_md5=md5.hexdigest().upper()#把数据转成MD5格式,upper()把小写字母转换成大写字母,lower()把大写字母换成小写字母
        print(sign_bytes_utf8)
        print(self.sign_md5)
    def test_login_success(self):
        """登录成功"""
        body_raw={"phone":"13981401923","password":self.sign_md5,"telephoneCode":"+86"}
        r=requests.post(self.url,json=body_raw)
        result=r.json()
        print(self.sign_md5)
        self.assertEqual(result['code'],'200')
        self.assertEqual(result['msg'],"登录成功")
    def test_login_uername_not_exits(self):
        """用户名不存在"""
        body_raw={"phone":"13981401921","password":self.sign_md5,"telephoneCode":"+86"}
        r=requests.post(self.url,json=body_raw)
        result=r.json()
        self.assertEqual(result['code'],'400')
        self.assertEqual(result['msg'],"用户不存在")
    def test_login_password_error(self):
        """密码错误"""
        body_raw={"phone":"13981401923","password":"111111","telephoneCode":"+86"}
        r=requests.post(self.url,json=body_raw)
        result=r.json()
        self.assertEqual(result["code"],'400')
        self.assertEqual(result['msg'],"密码不正确")
    def test_login_uername_error(self):
         body_raw={"phone":"139","password":"11111","telephoneCode":"+64"}
         r=requests.post(self.url,json=body_raw)
         result=r.json()
         self.assertEqual(result['code'],'400')
         self.assertEqual(result['msg'],'用户不存在')
if __name__=="__name__":
    unittest.main()