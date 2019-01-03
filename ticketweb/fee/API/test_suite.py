# -*- coding: utf-8 -*-

import unittest
from test_feeHealth import TestFeeHealth
# import HTMLTestRunner
import HTMLTestReportEN

if __name__ == '__main__':
	suite = unittest.TestSuite()
	print("test_suit starting-----")
	suite.addTests(unittest.TestLoader().loadTestsFromName('test_feeHealth.TestFeeHealth'))
	suite.addTests(unittest.TestLoader().loadTestsFromName('test_getFee.TestGetFee'))
	suite.addTests(unittest.TestLoader().loadTestsFromName('test_getFeeReport.TestGetFeeReport'))
	suite.addTests(unittest.TestLoader().loadTestsFromName('test_saveFeeAPI.TestSaveFee'))
	suite.addTests(unittest.TestLoader().loadTestsFromName('test_getFeeAuditing.TestGetFeeAuditing'))
	runner = unittest.TextTestRunner(verbosity=2)
	# runner.run(suite)
	
	
	#report path
	file_path = "D:\\python\\ticketweb\\fee\\resultEN.html"
	file_result= open(file_path, 'wb')
	print("test_result_path -----"+file_path)

	#test report
	# runner = HTMLTestRunner.HTMLTestRunner(stream = file_result, \
											# title = u"T4 Fee Report"\
											# description = u"test case")

	runner = HTMLTestReportEN.HTMLTestRunner(\
		stream=file_result,\
		title='{ Test Report }',\
		description='Test report detail',\
		tester='Alam'\
		)
	print("test_suit running-----")
	#run case
	runner.run(suite)
	file_result.close()
	print("\ntest_suit end -----")