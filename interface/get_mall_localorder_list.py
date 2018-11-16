from db_fixture.jwt import Jwt
import requests
import unittest
class Get_Order_Localorder_List(Jwt):
    """获取订单列表"""
    url="http://172.18.0.50/mall/localOrder/4User"
    def test_get_list(self):
        header={"version":"v1.0.0","language":"zh-CN","Authorization":self.jwt}
        params={"start":0,"limit":5}
        print(self.url)
        r=requests.get(self.url,params=params,headers=header)
        result=r.json()
        self.assertEqual(result['code'],'200')

if __name__=="__main__":
    unittest.main()
    