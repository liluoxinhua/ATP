import ddt
import requests
import yaml

from lib.log import atp_log
from cases.testExlogin import testExlogin

def gettoken():
    filepath = r'C:\\Users\\cherrylixh\\PycharmProjects\\ATP\\conf\\2.yaml'
    f = open(filepath)
    res = yaml.load(f)
    req = res[0]
    host = req['host']
    url = req['url']
    data = req['data']
    try:
        rew = requests.get(host + url, params=data)
        token = rew.json()['result']['token']
        atp_log.info('gettoken:%s'%token)
        return token
    except Exception  as e:
        atp_log.error('获取token失败')


