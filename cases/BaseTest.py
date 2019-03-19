
import unittest
import requests
from urllib import parse
from lib.log import atp_log
class BaseTest(unittest.TestCase):
    def __init__(self,methosName='runTest'):
        super(BaseTest,self).__init__(methosName)
    @classmethod
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        pass
    #ddt自动读取文件，并获取内容传给下面的函数，循环调用
    def requestTest(self,*args,**kwargs):
        detail=kwargs.get('detail','no detail')
        self._testMethodDoc=detail
        host=kwargs.get('host')
        url=kwargs.get('url')
        url=parse.urljoin(host,url)
        method=kwargs.get('method','get')
        data=kwargs.get('data',{})
        header=kwargs.get('header',{})
        cookie=kwargs.get('Cookie'.lower(),{})
        #args是data中需要传入的参数key值，由于kwargs中已经更新了手动加入的参数，现在需要把这个参数放在data字典中，cookie是单独放在header中不能放在body中
        if(len(args)>0):
            for c in args:
                atp_log.info('c:%s'%c)
                if c.lower()=='cookie':
                    continue
                #将需要手动传入的数据放在data，key值是传入时的args，value值放在已更新的kwargs对应的key中
                data[c]=kwargs[c]
        atp_log.info('data:%s' % data)
        check=kwargs.get('check')
        method=method.lower()
        try:
            #根据method判断需要执行哪个命令
            if method=='get':
                res=requests.get(url,params=data,cookies=cookie,headers=header)
            else:
                res=requests.post(url,data,cookies=cookie,headers=header)
            req = res.text
            atp_log.info('responde:%s'%req)
            return res
        except Exception as e:
            atp_log.error('requestTest: %s' %e)
            print ('请求接口出错')
            req=e
            #断言，yaml中checklist是否包含在返回的结果中
        for c in check:
            self.assertIn(c,req,msg='预期结果不符，预期结果%s，实际结果%s'%(c,req))