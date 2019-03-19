# --*-- coding:utf-8 --*--
import os,time
BASE_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
now=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
LOG_PATH=os.path.join(BASE_PATH,'logs',now+'.log')
LOG_LEVEL='debug'
CASE_PATH=os.path.join(BASE_PATH,'cases')   #用例存放路径
#邮箱配置
mail_host='smtp.qq.com'
mail_user='872677171@qq.com'
mail_password='fmmnadptslckbbgf'
to='872677171@qq.com'
