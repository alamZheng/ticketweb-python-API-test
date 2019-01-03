import unittest
import requests
import re


def interfaceTest(api_host,check_point,request_method="GET",request_data="", s=None):
	headers = {'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',\
	'X-Requested-With' : 'XMLHttpRequest',\
	'Connection' : 'keep-alive',\
	'Referer' : 'http://' + api_host,\
	'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'}


	if request_method == 'GET':
		status = "cannot get any response"
		resp = status
		try:
			r = requests.get('http://'+api_host+"/fees/health", headers = headers,timeout=1)
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

class TestFeeHealth(unittest.TestCase):

	def test_01_FeeHealth_QA1(self):
		qa1URL="app3.tktwb.twqa1.websys.tmcs:8080"
		result = interfaceTest(qa1URL,check_point="UP")
		self.assertEqual("passed", result)

	def test_02_FeeHealth_Stg1(self):
		stg1URL="clientapi.tktwb.twstg1.websys.tmcs:8080"
		result = interfaceTest(stg1URL,check_point="UP")
		self.assertEqual("passed", result)


if __name__ == '__main__':
	unittest.main()