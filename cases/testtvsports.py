# --*-- coding: utf-8 --*--
from cases.BaseTest import BaseTest
import ddt
@ddt.ddt
class testtvsports(BaseTest):
    args=()
    @ddt.file_data('C:\\Users\\cherrylixh\\PycharmProjects\\ATP\\conf\\1.yaml')
    def test_one(self,*args,**kwargs):
        BaseTest().requestTest(*args,**kwargs)

