import requests
import unittest
import re
from parameterized import parameterized

def interfaceTest(api_host,check_point,request_method="GET",request_data="", s=None,domains="1"\
	,orgs="145162", eventfees="3705284",feeLevel="event",groupEventfees="29709"):
	headers = {'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',\
	'X-Requested-With' : 'XMLHttpRequest',\
	'Connection' : 'keep-alive',\
	'Referer' : 'http://' + api_host,\
	'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'}

	if feeLevel == "event":
		Url ='http://'+api_host+"/fees/domains/"+domains+"/orgs/"+orgs+"/eventfees/"+eventfees+"/reports"
	elif feeLevel == "groupEvent":
		Url ='http://'+api_host+"/fees/domains/"+domains+"/orgs/"+orgs+"/eventgroupfees/"+groupEventfees+"/reports"
	else:
		print("feeLevel is incorrect!")

	if request_method == 'GET':
		status = "cannot get any response"
		resp = status
		try:
			print("\n"+Url)
			r = requests.get(Url, headers = headers,timeout=1)
			status = r.status_code
			# print(status)
			resp = r.text
			# print(resp)
		except Exception as e:
			pass
	
	if status == 200:
		# print(200)
		if re.search(check_point, str(resp)):
			return("passed")
	else:
		return(status)

class TestGetFeeReport(unittest.TestCase):
	stg1_host="clientapi.tktwb.twstg1.websys.tmcs:8080"
	qa1_host="app3.tktwb.twqa1.websys.tmcs:8080"

	def test_01_getFeeReport_QA1(self):
		# qa1URL="app3.tktwb.twqa1.websys.tmcs:8080"
		result = interfaceTest(self.qa1_host,check_point="sectionName")
		self.assertEqual("passed", result)

	@parameterized.expand([
		["ca_domain", "2"],
		["ie_domain", "4"],
		["uk_domain", "5"],
		["au_domain", "6"],
		["nz_domain", "7"],
		])
	def test_02_getFeeReport_QA1_AllDomain(self,name,domain):
		# qa1URL="app3.tktwb.twqa1.websys.tmcs:8080"
		# domains = ["1","2","4","5","6","7"]
		# for i in domains:
		try:
			result = interfaceTest(self.qa1_host,check_point="sectionName",domains=domain)
			self.assertEqual("passed", result)
		except Exception as e:
			print("\nassert fail ------------------domain "+i+" is error")

	def test_03_getFeeReport_Stg1(self):
		# stg1URL="clientapi.tktwb.twstg1.websys.tmcs:8080"
		result = interfaceTest(self.stg1_host,check_point="sectionName",orgs='238663',eventfees='7747685')
		self.assertEqual("passed", result)

	@parameterized.expand([
		["us_domain", "1","238663","7742085"],
		["ca_domain", "2","231863","7745735"],
		["ie_domain", "4","231873","7649315"],
		["uk_domain", "5","231883","7649325"],
		["au_domain", "6","231893","7649285"],
		["nz_domain", "7","231903","7545665"],
		])
	def test_04_getFeeReport_STG1_AllDomainEvents(self,name,domain,org,event):
		result = interfaceTest(self.stg1_host,feeLevel="event",check_point="sectionList",domains=domain,orgs=org,eventfees=event)
		self.assertEqual("passed", result)

	@parameterized.expand([
		["us_domain", "1","238663","29709"],
		["ca_domain", "2","231863","29712"],
		["ie_domain", "4","231873","29710"],
		["uk_domain", "5","231883","29711"],
		["au_domain", "6","231893","29714"],
		["nz_domain", "7","231903","29713"],
		])
	def test_05_getFeeReport_STG1_AllDomainGroupEvents(self,name,domain,org,groupEvent):
		result = interfaceTest(self.stg1_host,feeLevel="groupEvent",check_point="sectionList",domains=domain,orgs=org,groupEventfees=groupEvent)
		self.assertEqual("passed", result)

if __name__ == '__main__':
	unittest.main()