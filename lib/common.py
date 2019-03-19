# --*-- coding:utf-8 --*--
import xlrd,requests
from xlutils import copy
from lib.log import atp_log
class OpCase():
    def get_cases(self,filepath):
        cases=[] #保存用例
        print ('filepath%s' % filepath)
        if filepath.endswith('.xls') or filepath.endswith('xlsx'):
            try:
                book=xlrd.open_workbook(filepath)    #打开文件
                sheet=book.sheet_by_index(0)         #获取第一个sheet表
                nrows=sheet.nrows                    #获取表格行数
                for i in range(1,nrows):             #从第2行循环读取用例
                    row_data=sheet.row_values(i)       #获取每行的数据，返回一个list
                    cases.append(row_data[4:9])         #获取4-9列的数据放入cases：url，methos，data，check
                atp_log.info('共有%s条用例' % len(cases))
                self.filepath=filepath
                print ('cases:%s'%cases)
            except Exception as e:
                atp_log.error('文件打开失败：%s' % e)
        else:
            atp_log.error('用例格式不合法，需要xls或xksx：%s' % filepath)
        return cases
    def my_requests(self,url,data,method):
        method=method.upper()     #统一请求方法大写
        data=self.data_to_dic(data)
        try:
            if method=='GET':
                res=requests.get(url,params=data).text
            elif method=='POST':
                res=requests.post(url,data).text
            else:
                atp_log.warning('请求方式暂不支持')
                res='请求方式不支持'
        except Exception as e:
            atp_log.error('接口不通url %s\n 错误信息：%s' %e)
            res='接口不通'
        return res

    def data_to_dic(self, data):
        print ('data_to_dic %s'% data)
        if data:
            data=data.split(',')
            res={}
            for d in data:
                k,v=d.split('=')
                res[k]=v
            print (res)
            return res

    def check(self,res,check):
        for c in check.split(','):
            if c not in res:
                atp_log.error('失败,预期结果：%s，实际结果：%s' %(c,res))
                return 'fail'
        return 'secessced'

    def write_to_excel(self,cases_res):
        book=xlrd.open_workbook(self.filepath)
        newbook=copy.copy(book)
        sheet=newbook.get_sheet(0)
        row=1
        for case_res in cases_res:
            sheet.write(row,9,case_res[0]) #第9列是实际结果
            sheet.write(row,10,case_res[1]) #第10列是测试结果
            row+=1
        newbook.save(self.filepath.replace('xlsx','xls'))





