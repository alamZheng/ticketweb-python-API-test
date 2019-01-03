import requests
import unittest
import re
from parameterized import parameterized


def interfaceTest(api_host,\
					feeLevel,\
					check_point,\
					request_method="GET",\
					request_data="", \
					s=None,domain="1",\
					orgs="145162", eventfees="3705284",groupEventfees="88785",\
					feeType="8"):
	headers = {\
	'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',\
	'X-Requested-With' : 'XMLHttpRequest',\
	'Connection' : 'keep-alive',\
	'Referer' : 'http://' + api_host,\
	'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
	}

	if feeLevel == "domain":
		Url ="http://"+api_host+"/fees/domainfees/"+domain+"/"
	elif feeLevel == "org":
		Url = "http://"+api_host+"/fees/domains/"+domain+"/orgfees/"+orgs+"/"
	elif feeLevel == "event":
		Url = "http://"+api_host+"/fees/domains/"+domain+"/orgs/"+orgs+"/eventfees/"+eventfees+""
	elif feeLevel == "eventFeeType":
		Url = "http://"+api_host+"/fees/domains/"+domain+"/orgs/"+orgs+"/eventfees/"+eventfees+"?feeType="+feeType
	elif feeLevel =="groupEvent":
		Url = "http://"+api_host+"/fees/domains/"+domain+"/orgs/"+orgs+"/eventgroupfees/"+groupEventfees+""
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
			# print("\n"+Url)
			pass
			# raise e
	
	if status == 200:
		# print(200)
		if re.search(check_point, str(resp)):
			return("passed")
	else:
		return status

class TestGetFee(unittest.TestCase):
	qa1_host="app3.tktwb.twqa1.websys.tmcs:8080"
	stg1_host="clientapi.tktwb.twstg1.websys.tmcs:8080"

	@parameterized.expand([
		["Url_domain", "domain"],
		["Url_org", "org"],
		["Url_event", "event"],
		["Url_eventFeeType", "eventFeeType"],
		["Url_groupEventFeeType", "groupEvent"],
		])
	def test_01_getFee_QA1(self,name,feeLevel):
		# qa1_host="app3.tktwb.twqa1.websys.tmcs:8080"
		result = interfaceTest(self.qa1_host,feeLevel,check_point="Success")
		self.assertEqual("passed", result)

	@parameterized.expand([
		["ca_domain", "2"],
		["ie_domain", "4"],
		["uk_domain", "5"],
		["au_domain", "6"],
		["nz_domain", "7"],
		])
	def test_02_getFee_QA1_AllDomain(self,name,domain):
		# domains = ["1","2","a","4","5","6","b","7"]
		# for i in domains:
		result = interfaceTest(self.qa1_host,feeLevel="domain",check_point="perTicketRebate",domain=domain)
		self.assertEqual("passed", result)

	@parameterized.expand([
		["Url_domain", "domain"],
		["Url_org", "org"],
		["Url_event", "event"],
		["Url_eventFeeType", "eventFeeType"],
		["Url_groupEventFeeType", "groupEvent"],
		])
	def test_03_getFee_Stg1(self,name,feeLevel):
		
		result = interfaceTest(self.stg1_host,feeLevel,check_point="perTicketRebate",orgs='238663',eventfees='7747685',groupEventfees="29709")
		self.assertEqual("passed", result)

	@parameterized.expand([
		["ca_domain", "2"],
		["ie_domain", "4"],
		["uk_domain", "5"],
		["au_domain", "6"],
		["nz_domain", "7"],
		])
	def test_04_getFee_STG1_AllDomain(self,name,domain):
		result = interfaceTest(self.stg1_host,feeLevel="domain",check_point="Success",domain=domain)
		self.assertEqual("passed", result)

	@parameterized.expand([
		["us_domain", "238663"],
		["ca_domain", "231863"],
		["ie_domain", "231873"],
		["uk_domain", "231883"],
		["au_domain", "231893"],
		["nz_domain", "231903"],
		])
	def test_05_getFee_STG1_AllDomainOrgs(self,name,org):
		result = interfaceTest(self.stg1_host,feeLevel="org",check_point="perTicket",orgs=org)
		self.assertEqual("passed", result)

	@parameterized.expand([
		["us_domain", "238663","7742085"],
		["ca_domain", "231863","7745735"],
		["ie_domain", "231873","7649315"],
		["uk_domain", "231883","7649325"],
		["au_domain", "231893","7649285"],
		["nz_domain", "231903","7545665"],
		])
	def test_06_getFee_STG1_AllDomainEvents(self,name,org,event):
		result = interfaceTest(self.stg1_host,feeLevel="event",check_point="perTicket",orgs=org,eventfees=event)
		self.assertEqual("passed", result)

	@parameterized.expand([
		["us_domain", "238663","29709"],
		["ca_domain", "231863","29712"],
		["ie_domain", "231873","29710"],
		["uk_domain", "231883","29711"],
		["au_domain", "231893","29714"],
		["nz_domain", "231903","29713"],
		])
	def test_06_getFee_STG1_AllDomainGroupEvents(self,name,org,groupEvent):
		result = interfaceTest(self.stg1_host,feeLevel="groupEvent",check_point="perTicket",orgs=org,groupEventfees=groupEvent)
		self.assertEqual("passed", result)

if __name__ == '__main__':
	unittest.main()