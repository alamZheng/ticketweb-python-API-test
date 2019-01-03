import unittest
import requests
import re
import json
import random
from parameterized import parameterized

def interfaceTest(api_host,request_method="PUT",request_data='',check_point='', s=None,\
                userId="alam@livenation.com",\
                domains = "1",orgs="145162", eventfees="3705284",groupEvents="123123",\
                feeLevel = "event"):
    headers = {
    'Content-Type' : 'application/json',\
    'X-Requested-With' : 'XMLHttpRequest',\
    'Connection' : 'keep-alive',\
    'Accept-Language':'en,zh-CN;q=0.9,zh;q=0.8,en-US;q=0.7',\
    'Host' : api_host,\
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/49.0.2623.110 Safari/537.36'}

    if feeLevel == "event":
        Url ="http://"+api_host+"/fees/domains/"+domains+"/orgs/"+orgs+"/eventfees/"+eventfees+"?userId="+userId+""
    elif feeLevel == "groupEvent":
        Url ="http://"+api_host+"/fees/domains/"+domains+"/orgs/"+orgs+"/eventgroupfees/"+groupEvents+"?userId="+userId+""
    elif feeLevel == "org":
        Url ="http://"+api_host+"/fees/domains/"+domains+"/orgfees/"+orgs+"?userId="+userId+""
    elif feeLevel == "domain":
        Url ="http://"+api_host+"/fees/domainfees/"+domains+"?userId="+userId+""
    else:
        print("feeLevel is incorrect!")

    if request_method == 'PUT':
        status = "cannot get any response"
        resp = status
        try:
            print('\n'+Url)
            print(request_data)
            r = requests.put(Url, data=request_data, headers = headers,timeout=5)
            status = r.status_code
            # print("status_code ==========="+str(status))
            resp = r.text
        except Exception as e:
            pass
        # print(resp)
        # return status
    
    if status == 200:
        # print(200)
        if re.search(check_point, str(resp)):
            return("Success")
    else:
        return(status)

class TestSaveFee(unittest.TestCase):
    stg1_host = "clientapi.tktwb.twstg1.websys.tmcs:8080"
    qa1_host = "app3.tktwb.twqa1.websys.tmcs:8080"

    def test_01_Save_API_QA1(self):
        # qa1URL="app3.tktwb.twqa1.websys.tmcs:8080"

        payload = '[{\
            "feeTypeId": '+str(random.randint(1,10))+',\
            "tiers": [\
                {\
                    "lowertier": null,\
                    "uppertier": null,\
                    "selleramount": '+str(random.randint(0,9999)/100)+',\
                    "sellerlowerbound": null,\
                    "sellerupperbound": null,\
                    "buyeramount": '+str(random.randint(0,9999)/100)+',\
                    "buyerlowerbound": null,\
                    "buyerupperbound": null,\
                    "units": '+str(random.randint(100,101))+'\
                }]}]'
        # print(payload)
        userId ="alam"+str(random.randint(0,999))+"@ticketweb.com"
        result = interfaceTest(self.qa1_host,request_data=payload,check_point='Success',userId=userId)
        # print(result)
        self.assertEqual("Success", result)

    def test_02_Save_API_STG1(self):
        # qa1URL="clientapi.tktwb.twstg1.websys.tmcs:8080"

        payload = '[{\
            "feeTypeId": '+str(random.randint(1,10))+',\
            "tiers": [\
                {\
                    "lowertier": null,\
                    "uppertier": null,\
                    "selleramount": '+str(random.randint(0,9999)/100)+',\
                    "sellerlowerbound": null,\
                    "sellerupperbound": null,\
                    "buyeramount": '+str(random.randint(0,9999)/100)+',\
                    "buyerlowerbound": null,\
                    "buyerupperbound": null,\
                    "units": '+str(random.randint(100,101))+'\
                }]}]'
        # print(payload)
        userId ="alam"+str(random.randint(0,999))+"@ticketweb.com"
        result = interfaceTest(self.stg1_host,request_data=payload,check_point='Success',userId=userId,orgs='238663',eventfees='7747685')
        # print(result)
        self.assertEqual("Success", result)

    @parameterized.expand([
        ["us_domain", "1","238663"],
        ["ca_domain", "2","231863"],
        ["ie_domain", "4","231873"],
        # ["uk_domain", "5","231883"],
        # ["au_domain", "6","231893"],
        # ["nz_domain", "7","231903"],
        ])
    def test_03_Save_API_STG1_AllDomainOrgs(self,name,domain,org):
        payload = '[{\
            "feeTypeId": 17,\
            "tiers": [\
                {\
                    "lowertier": null,\
                    "uppertier": null,\
                    "selleramount": '+str(random.randint(0,9999)/100)+',\
                    "sellerlowerbound": null,\
                    "sellerupperbound": null,\
                    "buyeramount": '+str(random.randint(0,9999)/100)+',\
                    "buyerlowerbound": null,\
                    "buyerupperbound": null,\
                    "units": "100"\
                }]}]'
        userId ="alam"+str(random.randint(0,999))+"@ticketweb.com"
        result = interfaceTest(self.stg1_host,request_data=payload,check_point='Success',feeLevel='org',domains=domain,userId=userId,orgs=org)
        self.assertEqual("Success", result)

    @parameterized.expand([
        ["us_domain", "1","238663","29709"],
        ["ca_domain", "2","231863","29712"],
        ["ie_domain", "4","231873","29710"],
        # ["uk_domain", "5","231883","29711"],
        # ["au_domain", "6","231893","29714"],
        # ["nz_domain", "7","231903","29713"],
        ])
    def test_04_Save_API_STG1_AllDomainGroupEvent(self,name,domain,org,groupEvent):
        payload = '[{\
            "feeTypeId": 5,\
            "tiers": [\
                {\
                    "lowertier": null,\
                    "uppertier": null,\
                    "selleramount": '+str(random.randint(0,9999)/100)+',\
                    "sellerlowerbound": null,\
                    "sellerupperbound": null,\
                    "buyeramount": '+str(random.randint(0,9999)/100)+',\
                    "buyerlowerbound": null,\
                    "buyerupperbound": null,\
                    "units": "100"\
                }]}]'
        userId ="alam"+str(random.randint(0,999))+"@ticketweb.com"
        result = interfaceTest(self.stg1_host,request_data=payload,check_point='Success',feeLevel='groupEvent',\
            domains=domain,userId=userId,orgs=org,groupEvents=groupEvent)
        self.assertEqual("Success", result)

if __name__ == '__main__':
    unittest.main()