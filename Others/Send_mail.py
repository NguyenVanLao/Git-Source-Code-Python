# Successed #

import smtplib
import getpass

#Setup mail
email = 'laolaipython@gmail.com'
password = 'nxfkqdfsaocwrxic'
email_sent = 'vanlao0512@gmail.com'

#Function gui mail
session = smtplib.SMTP('smtp.gmail.com',587)
session.starttls() #enable security
session.login(email,password)

#Tao noi dung mail
mail_content = '''Subject: Hello! This is automation mail for you 
#Noi dung nhap vao day ...
Con meo yeu dau cua anh!
ok!
'''
session.sendmail(email, email_sent, mail_content)
