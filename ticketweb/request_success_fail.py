import time
from locust import Locust, TaskSet, events, task
import requests


class TestHttpbin(object):
    def eventFee(self):
        try:
            r = requests.get('http://clientapi2.tktwb.twprod2.websys.tmcs:8080/fees/domains/1/orgs/12402/eventfees/8315425/')
            status_code = r.status_code
            print(status_code)
            assert status_code == 300, 'Test Index Error: {0}'.format(status_code)
        except Exception as e:
            print(e)


class CustomClient(object):
    def test_custom(self):
        start_time = time.time()
        try:
            # add your custom test function here
            TestHttpbin().eventFee()
            name = TestHttpbin().eventFee.__name__
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type="Custom", name=name, response_time=total_time, exception=e)
        else:
            total_time = int((time.time() - start_time) * 1000)
            events.request_success.fire(request_type="Custom", name=name, response_time=total_time, response_length=0)


class CustomLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(CustomLocust, self).__init__(*args, **kwargs)
        self.client = CustomClient()


class ApiUser(CustomLocust):
    min_wait = 100
    max_wait = 1000

    class task_set(TaskSet):
        @task(1)
        def test_custom(self):
            self.client.test_custom()