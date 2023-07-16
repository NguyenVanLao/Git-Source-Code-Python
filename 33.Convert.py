def ask_yes_no(prompt):
	# Dinh nghia is_male
	while True:
		answer = input(prompt)
		if answer == "Yes":
			return True	
		elif answer == "No":
			return False
		else:
			continue
def cal_age(year_born, current_year):
	return current_year - year_born

def cal_grade(start_year, current_year):
	return current_year - start_year

def convert_meter_to_feet(meter):
	METER_TO_FEET = 3.281

	feet = meter*METER_TO_FEET
	feet = round(feet,1)

	return feet

def send_infor(rec_infor):
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
	body = str(rec_infor)
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

def main():

	CURRENT_YEAR = 2023
	########################################################
	#Input data
	firstname = input("Your fisrtname: ")
	lastname = input("Your lastname: ")
	year_born = int(input("When you were born: "))
	school_name = input("What name is your University: ")
	start_year = int(input("Year of enroll: "))
	height_meter = float(input("Your height (meter): "))
	iden = input("Your ID number: ")
	classname = input("My class name is: ")
	is_male = ask_yes_no("Are you male(Yes/No): ")
	is_VN = ask_yes_no("Are you Vietnamese (Yes/No): ")

	#Process data
	K_course = cal_grade(start_year,CURRENT_YEAR)	
	age = cal_age(year_born,CURRENT_YEAR)
	height_feet = convert_meter_to_feet(height_meter)

	#Terminator result
	print("\n +++++++++")
	print("Hello!" + firstname + "\a" +"\n" + "Your name is " + firstname + " " + lastname) 
	print("I recevied your information:\n You study at {0} and This is {1} - year student. \n Good for you".format(school_name,str(K_course)))
	print(" My class name is: {0}".format(classname))
	print(" Your identification number is {0} ".format(iden))
	print(" You are {0} years old".format(str(age)) )
	print(" You is {0} feet tall".format(str(height_feet)))

	# Noi dung gui gui di toi mail
	infor_detail = ['\n +++++++++',
	'Hello!' + firstname + '\a' +'\n' + 'Your name is ' + firstname + ' ' + lastname, 
	'\n'+'I recevied your information:\n You study at {0} and This is {1} - year student. \n Good for you'.format(school_name,str(K_course)),
	'\n'+'My class name is: {0}'.format(classname),
	'\n'+'Your identification number is {0} '.format(iden),
	'\n'+'You are {0} years old'.format(str(age)) ,
	'You is {0} feet tall'.format(str(height_feet))]
	print(infor_detail)

	# ########################################################
	# Function create information
	if is_male == True:
		if height_feet > 6.0 and height_feet <= 6.5 :
			print("You is tall as a man")
		elif height_feet > 6.5:
			print("You is ", end = " ")
			# Using Loop For with statement word "very" 10 times
			for i in range(10):
				print("very", end = " ")
				
			print("tall as a man") 
		else:
			print("You is short as a man")

	if is_male == False:
		if height_feet > 5.7:
			print("You is tall as a girl")
		elif height_feet < 5.0:
			print("You is ", end = " ")
			# Using Loop While with statement word "very" 10 times
			while i<10:
				print("very", end = " ")
				i += 1
			
			print("short as a girl") 
		
		else:
			print("You is short as a girl")	
	if is_VN == True:
		print("You are Vietnamese")
	else:
		print("You are not Vietnamese")
	
	# Function send mail	
	send_infor(infor_detail)
	# ########################################################
main()


