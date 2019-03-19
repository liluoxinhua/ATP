# --*-- coding:utf-8 --*--
import os,sys
BASE_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,BASE_PATH)

from lib.common import OpCase
from conf import setting
from lib.sendmail import sendmail
class CaseRun():
    def run(self):
        op=OpCase()
        res_list=[]          #用来存放实际结果和测试结果，写入excel
        for t in os.listdir(setting.CASE_PATH):
            abs_path=os.path.join(setting.CASE_PATH,t)
            case_list=op.get_cases(abs_path)
            fail_count=0
            pass_count=0
            for case in case_list:
                print ('case:%s' %case)
                host,url,method,data,check=case
                res=op.my_requests(host+url,data,method)
                status=op.check(res,check)
                print(status,res)
                res_list.append([res,status])
                if status=='fail':
                    fail_count+=1
                else:
                    pass_count+=1
                op.write_to_excel(res_list)
                msg='本次共运行%s条用例，失败%s,成功%s'%(len(res_list),fail_count,pass_count)
                sendmail('测试结果',msg,abs_path)

print (os.listdir(setting.CASE_PATH))
print (BASE_PATH)
CaseRun().run()