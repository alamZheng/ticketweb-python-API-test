import requests
import logging
import re

'''
def interfaceTest1(num, api_purpose, api_host, request_method,request_data, check_point,s=None):
	headers = {'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',\
	'X-Requested-With' : 'XMLHttpRequest',\
	'Connection' : 'keep-alive',\
	'Referer' : 'http://' + api_host,\
	'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'}

	if s == None:
		s = requests.session()

	if request_method == 'POST':
		if request_url != '/login' :
	r = s.post(url='http://'+api_host+request_url, data = json.loads(request_data), headers = headers)         #由于此处数据没有经过加密，所以需要把Json格式字符串解码转换成**Python对象**
	elif request_url == '/login' :
		s = requests.session()
		r = s.post(url='http://'+api_host+request_url, data = request_data, headers = headers)          #由于登录密码不能明文传输，采用MD5加密，在之前的代码中已经进行过json.loads()转换，所以此处不需要解码
	else:
		logging.warning(num + ' ' + api_purpose + '  HTTP请求方法错误，请确认[Request Method]字段是否正确！！！')
		s = None
		return 400, r, s
		status = r.status_code
	resp = r.text
		print(resp)

		if status == 200 :
			if re.search(check_point, str(r.text)):
				logging.info(num + ' ' + api_purpose + ' success，' + str(status) + ', ' + str(r.text))
				return status, resp, s
			else:
				logging.warning(num + ' ' + api_purpose + ' fail , [' + str(status) + '], ' + str(r.text))
				return 200, resp , None
		else:
			logging.warning(num + ' ' + api_purpose + '  fail , [' + str(status) + '],' + str(r.text))
			# return status, resp.decode('utf-8'), None
'''

def interfaceTest(num, api_purpose, api_host, request_method,request_data, check_point,s=None):
	headers = {'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',\
	'X-Requested-With' : 'XMLHttpRequest',\
	'Connection' : 'keep-alive',\
	'Referer' : 'http://' + api_host,\
	'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'}


	if request_method == 'GET':
		r = requests.get('http://'+api_host+"/fees/domains/1/orgs/142142/eventfees/3704144?feeType=8", headers = headers)
		status = r.status_code
		# print(status)
		resp = r.text
		# print(resp)
	
	if status == 200:
		# print(200)
		if re.search(check_point, str(resp)):
			print("chek passed")

if __name__ == '__main__':

	qa1URL="app3.tktwb.twqa1.websys.tmcs:8080"
	stg1URL="clientapi.tktwb.twstg1.websys.tmcs:8080"
	urls = [qa1URL,stg1URL]

	for i in (urls):
		interfaceTest("1","get fee",i,"GET","","perTicketRebate")