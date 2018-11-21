from locust import HttpLocust,TaskSet,task
# #定义用户行为
class UserBehavior(TaskSet):
    @task
    def baidu_page(self):
        self.client.get("/")
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000
    print("返回正常")
# f=open("F:\python\guests.txt",'w')
# for i in range(1,100):
#     str_i=str(i)
#     realname="jack"+str_i
#     phone='13800110000'+str_i
#     email="jack"+str_i+"@mail.com"
#     sql='INSERT INTO sign_guest(realname,phone,email,sign,create_time,event_id) VALUES ("'+realname+'","'+phone+'","'+email+'",0,"2018-11-19 17:59:00",1);'
#     f.write(sql)
#     f.write("\n")
# f.close()
#web性能测试
# class UserBehavior(TaskSet):
#     def on_start(self):
#         """on_start is called when a locust start before any task is scheduled"""
#         self.login()
#     def login(self):
#         self.client.post("/login_action",{"username":"admin","password":"admin123456"})
#     @task(2)
#     def event_manage(self):
#         self.client.get("/guest_manage/")
#     @task(2)
#     def guest_manage(self):
#         self.client.get("/guest_manage/")
#     @task(1)
#     def search_phone(self):
#         self.client.get("/search_phone/",params={"phone":'13800112541'})
# class WebsiteUser(HttpLocust):
#     task_set =UserBehavior
#     min_wait = 3000
#     max_wait = 6000
