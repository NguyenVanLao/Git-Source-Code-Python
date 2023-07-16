import smtplib
import getpass

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

#Thiet lap thong tin nguoi gui 
from_address = "laolaipython@gmail.com"
password = "nxfkqdfsaocwrxic"

#Thiet lap thong tin email nguoi nhan
to_address = "vanlao0512@gmail.com"
subject = "Hello! This is automation mail for you"

#Xay dung email
msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = subject

#Them noi dung email
body = "This is the body of the email"
msg.attach(MIMEText(body, 'plain'))

#Them anh vao email neu can
with open("lao.jpg", "rb") as f:
	img_data = f.read()
image = MIMEImage(img_data, name = "lao.jpg")
msg.attach(image)

#Gui mail
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(from_address, password)
text = msg.as_string()
server.sendmail(from_address, to_address, text)
server.quit()