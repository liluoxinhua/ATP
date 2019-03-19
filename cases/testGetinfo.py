# --*-- coding: utf-8 --*--
import urllib

from cases.BaseTest import BaseTest
from cases.testExlogin import testExlogin
import cases.commonMt as cm
from lib.log import atp_log
import ddt
import requests
from urllib import parse
@ddt.ddt
class testGetinfo(BaseTest):
    #获取token
    token=cm.gettoken()
    token = parse.unquote(token)
    #将获取到token作为参数，传入到data中
    wargs={'token':token}
    #获取自定义data的key值
    args=wargs.keys()
    @ddt.file_data('C:\\Users\\cherrylixh\\PycharmProjects\\ATP\\conf\\3.yaml')
    def testInfo(self, *args, **kwargs):
        #传入参数列表
        args=self.args
        #将手动需要传入的参数更新到参数字典中
        kwargs.update(self.wargs)
        BaseTest().requestTest(*args,**kwargs)
