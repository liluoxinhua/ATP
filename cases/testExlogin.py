from cases.BaseTest import BaseTest
from lib.log import atp_log
import ddt
@ddt.ddt
class testExlogin(BaseTest):
    args=()
    @ddt.file_data('C:\\Users\\cherrylixh\\PycharmProjects\\ATP\\conf\\2.yaml')
    def testlogin(self,*args,**kwargs):
        res=BaseTest().requestTest(*args,**kwargs)
        print('testlogin_res:%s'%res.json())
        atp_log.info('testlogin:%s'% res.json())
