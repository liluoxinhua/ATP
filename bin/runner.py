# --*-- coding:utf-8 --*--
import os
import unittest

import time
from lib.log import atp_log
from cases.testtvsports import testtvsports
from cases.testExlogin import testExlogin
from cases.testGetinfo import testGetinfo
from BeautifulReport import BeautifulReport as bf
if __name__=='__main__':
    #将测试用例集成到suite中
    suite=unittest.TestSuite()
    # suite.addTest(unittest.makeSuite(testExlogin))
    suite.addTest(unittest.makeSuite(testGetinfo))
    #使用beautifulReport运行测试用例
    run=bf(suite)
    ospath=os.getcwd()
    reportpath=os.path.join(ospath,'Report')
    if not os.path.exists(reportpath):
        os.mkdir(reportpath)
    print(reportpath)
    now=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    reporttitle=now+'.html'
    run.report(filename=reporttitle,description='testone',log_path=reportpath)
    atp_log.info('success_count%s'% run.success_count)
    atp_log.info('failure_count%s' % run.failure_count)
    print (run.success_count)
    print (run.failure_count)
