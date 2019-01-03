#coding:utf-8
from locust import HttpLocust, TaskSet, task

domains =[1,2,3,5,6,7]

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        # self.login()
        print("start test")

    # def login(self):
    #     self.client.post("/login", {"username":"ellen_key", "password":"education"})

    @task(1)
    def index(self):
        # self.client.get("/")
        for i in domains:
            with self.client.get(str(i)+"/orgs/12402/eventfees/8315425", catch_response=True) as response:
                if response.status_code != 200 :
                    response.failure("Got wrong response")

    # @task(1)
    # def profile(self):
    #     for i in domains:
    #         self.client.get("1/orgs/12402/eventfees/8315425/reports")

    @task(1)
    def profile(self):
        for i in domains:
            self.client.get(str(i)+"/orgfees/12402")
        self.client.get(str(i)+"/orgerror/12402")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host='http://clientapi2.tktwb.twprod2.websys.tmcs:8080/fees/domains/'
    min_wait = 0
    max_wait = 0