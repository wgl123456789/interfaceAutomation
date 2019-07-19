import smtplib
from email.mime.multipart import MIMEMultipart  # 混合MIME格式，支持上传附件
from email.header import Header  # 用于使用中文邮件主题
from email.mime.text import MIMEText



def send_email(report_file):
    # smtpserver = 'smtp.163.com'  # smtp服务
    # sender = 'gupaotest@163.com'  # 用户名
    # pwd = 'qqszzaa123456'  # 密码
    # receiver = '[1039571336@qq.com]'
    # subject = Header('接口测试报告', 'utf-8')
    # msg = MIMEText(open(report_file, encoding='utf-8').read(), 'html', 'utf-8')  # 内容，格式，编码
    # msg['From'] = sender
    # msg['To'] = receiver
    # msg['Subject'] = subject
    # # 发送邮件
    # try:
    #     smtp = smtplib.SMTP()
    #     smtp.connect(smtpserver)
    #     smtp.login(sender, pwd)
    # except:
    #     smtp = smtplib.SMTP_SSL(smtpserver, 465)
    #     smtp.sendmail(sender, receiver, msg.as_string())
    # finally:
    #     smtp.quit()

    smtpserver = 'smtp.163.com'  # smtp服务
    sender = 'gupaotest@163.com'  # 用户名
    pwd = 'qqszzaa123456'  # 密码
    receiver = '1039571336@qq.com'

    #file_path = r'D:\腾讯课堂\interfaceAutomation\interface\report\report.html'

    with open(report_file, 'rb') as fp:
        mail_body = fp.read()  # 读取邮件内容

    msg = MIMEMultipart()
    msg['From'] = sender
    # msg["To"]=receiver
    msg["To"] = ",".join(receiver)
    msg['Subject'] = "接口测试报告"
    # 正文
    body = MIMEText(mail_body, "html", "utf-8")
    msg.attach(body)
    # 附件
    att = MIMEText(mail_body, "html", "utf-8")
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename="test_result.html"'
    msg.attach(att)
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)  # 建立连接
        smtp.login(sender, pwd)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, 465)
        smtp.login(sender, pwd)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
