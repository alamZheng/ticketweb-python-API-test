import requests
import unittest
import re
from parameterized import parameterized

def interfaceTest(api_host,check_point="",request_method="GET",request_data="", s=None,domains="1"\
    ,orgs="145162", eventfees="3705284"):
    headers = {'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',\
    'X-Requested-With' : 'XMLHttpRequest',\
    'Connection' : 'keep-alive',\
    'Referer' : 'http://' + api_host,\
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'}


    if request_method == 'GET':
        status = "cannot get any response"
        resp = status
        try:
            url = 'http://'+api_host+"/fees/domains/"+domains+"/orgs/"+orgs+"/auditreports"
            print("\n"+url)
            r = requests.get(url, headers = headers, timeout=1)
            status = r.status_code
            resp = status
            resp = r.text
        except Exception as e:
            # raise e
            pass
    
    if status == 200:
        # print(200)
        if re.search(check_point, str(resp)):
            return("passed")
    else:
        return(status)

class TestGetFeeAuditing(unittest.TestCase):
    stg1_host = "clientapi.tktwb.twstg1.websys.tmcs:8080"
    qa1_host = "app3.tktwb.twqa1.websys.tmcs:8080"

    def test_01_getFeeAuditing_QA1(self):
        # qa1URL="app3.tktwb.twqa1.websys.tmcs:8080"
        result = interfaceTest(self.qa1_host,check_point="Success")
        self.assertEqual("passed", result)

    @parameterized.expand([
        ["ca_domain", "2"],
        ["ie_domain", "4"],
        ["uk_domain", "5"],
        ["au_domain", "6"],
        ["nz_domain", "7"],
        ])
    def test_02_getFeeAuditing_QA1_AllDomain(self,name,domain):
        # qa1URL="app3.tktwb.twqa1.websys.tmcs:8080"
        # domains = ["1","2","4","5","6","7"]
        # for i in domains:
        try:
            result = interfaceTest(self.qa1_host,check_point="Success",domains=domain)
            self.assertEqual("passed", result)
        except Exception as e:
            print("\nassert fail ------------------domain "+i+" is error")

    def test_03_getFeeAuditing_Stg1(self):
        # stg1URL="clientapi.tktwb.twstg1.websys.tmcs:8080"
        result = interfaceTest(self.stg1_host,check_point="Success",orgs='238663')
        self.assertEqual("passed", result)

    @parameterized.expand([
        ["us_domain", "1","238663"],
        ["ca_domain", "2","231863"],
        ["ie_domain", "4","231873"],
        ["uk_domain", "5","231883"],
        ["au_domain", "6","231893"],
        ["nz_domain", "7","231903"],
        ])
    def test_04_getFeeReport_STG1_AllDomainEvents(self,name,domain,org):
        result = interfaceTest(self.stg1_host,check_point="",domains=domain,orgs=org)
        self.assertEqual("passed", result)

if __name__ == '__main__':
    unittest.main()