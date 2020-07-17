#coding=utf-8
import os
#获取当前文件所在目录的父目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#获取存放页面元素定位表达式文件的绝对路径
pageElementLocatorPath = parentDirPath+r"/config/PageElementLocator.ini"
#获取数据文件存放的绝对路径
dataFilePath = parentDirPath+r"/testData/测试数据.xlsx"

#测试数据.xlsx中登陆账号tab每列对应的数字序号
acount_username = 2
acount_password = 3
login_isExecute = 4
login_testResult = 5
login_time = 6

#测试数据.xlsx中新增医师tab每列对应的数字序号
doctor_name = 2
doctor_IdNumber = 3
doctor_Number = 4
doctor_phoneNumber = 5
doctor_email = 6
doctor_remarks = 7
adddoctor_isExecute = 8
adddoctor_testResult = 9
adddoctor_time = 10





if __name__=="__main__":
    print(pageElementLocatorPath)
    print(dataFilePath)
    print(parentDirPath)
