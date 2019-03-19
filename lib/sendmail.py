# --*-- coding:utf-8 --*--
import yagmail
from conf import setting
from lib import log
def sendmail(title,content,attrs=None):
    try:
        m=yagmail.SMTP(host=setting.mail_host,user=setting.mail_user,password=setting.mail_password,smtp_ssl=True)
        m.send(to=setting.to,
               subject=title,
               contents=content,
               attachments=attrs)
    except Exception as e:
        log.atp_log.error('邮件发送失败')
        