import unittest
import requests
import hashlib
from db_fixture.jwt import Jwt
class UserLogout(Jwt):
    # def setUp(self):
    #     self.url="http://172.18.0.50/common/user/logout"
    #     login_url="http://172.18.0.50/common/merchant_shop_user_login"
    #     username="13981401923"
    #     password="123456"
    #     md5=hashlib.md5()
    #     md5.update(password.encode('utf8'))
    #     password_md5=md5.hexdigest().upper()
    #     body_raw={"phone":username,"password":password_md5,"telephoneCode":"+86"}
    #     print(password_md5)
    #     r=requests.post(login_url,json=body_raw)
    #     self.jwt=r.json()['data']['jwt']
    url = "http://172.18.0.50/common/user/logout"
    def test_logout_sucess(self):
        header={"Authorization":self.jwt,"Platform":'P_WECHAT',"Version":'2.7.0'}
        r=requests.get(self.url,headers=header)
        result=r.json()
        self.assertEqual(result['code'],'200')
        self.assertEqual(result['msg'],"注销成功")
if __name__=="__main__":
    unittest.main()
       