#!/usr/bin/python
#coding=utf-8

# data={"张三":23,"李四":21,"王五":20}
# op = open(file="D:/pythonFile/python1.txt",mode="w")
# for key,value in data.items():
#     str1 = str(key) +":"+ str(value) +"\n"
#     op.write(str1)
# op.close()

# op1 = open(file="D:/pythonFile/python1.txt",mode="r")
# str2 = op1.read()
# print(str2)

# op=open(file="D:/pythonFile/python2.txt",mode="a+")
# i = 1
# while i>0:
#     str = input()
#     op.write(str)
#     if i.__eq__(str):
#         break
# op.close()

# import calendar
# cal = calendar.month(2020, 8)
# print ("以下输出2016年1月份的日历:")
# print (cal)


# import json
# data = {"张三":23,"李四":21,"王五":20}
# jsonStr = json.dumps(data,ensure_ascii=False)
# print(jsonStr)

#九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("{}x{}={}\t".format(j,i,i*j),end='')
    print()

#随机数
import random
print(random.randint(1,100))
print(random.randrange(1,100,10))

#
# #发送邮件
# import smtplib
# from email import encoders
# from email.header import Header
# from email.mime.text import MIMEText
# from email.utils import parseaddr,formataddr
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
#
# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr((Header(name, 'utf-8').encode(), addr))
# # from_addr = input('发件人： ')
# # password = input('Password: ')
# # to_addr = input('To: ')
# # smtp_server = input('SMTP server: ')
# msg = MIMEMultipart()
# msg['From'] = _format_addr('python学习<%s>' % "zhangwh@windit.com.cn")
# msg['To'] = _format_addr("管理员<%s>" % "to_addr")
# msg['Subject'] = Header("来自SMTP的问候...","utf-8").encode()
# # 邮件正文是MIMEText:
# msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
#
# # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
# with open('D:\line.png', 'rb') as f:
#     # 设置附件的MIME和文件名，这里是png类型:
#     mime = MIMEBase('image', 'png', filename='line.png')
#     # 加上必要的头信息:
#     mime.add_header('Content-Disposition', 'attachment', filename='test.png')
#     mime.add_header('Content-ID', '<0>')
#     mime.add_header('X-Attachment-Id', '0')
#     # 把附件的内容读进来:
#     mime.set_payload(f.read())
#     # 用Base64编码:
#     encoders.encode_base64(mime)
#     # 添加到MIMEMultipart:
#     msg.attach(mime)
#
#
# server = smtplib.SMTP('smtp.exmail.qq.com',25)
# server.set_debuglevel(1)
# server.login("info@windit.com.cn","Windit2010")
# server.sendmail('info@windit.com.cn','1277420858@qq.com',msg.as_string())
#
# server.quit()
