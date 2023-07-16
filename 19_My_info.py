import smtplib
import getpass
CURRENT_YEAR = 2023
METER_TO_FEET = 3.281
########################################################
firstname = input("Your fisrtname: ")
lastname = input("Your lastname: ")
year_born = input("When you were born: ")
school_name = input("What name is your University: ")
start_year = input("Year of enroll: ")
height_meter = input("Your height (meter): ")
iden = input("Your ID number: ")
classname = input("My class name is: ")
gender_input = input("Are you male (Yes/No): ")

start_year = int(start_year)
year_born = int(year_born) #overwrite, \n: newline character
age = CURRENT_YEAR - year_born
K_course = CURRENT_YEAR - start_year	

height_meter = float(height_meter)
height_feet = height_meter*METER_TO_FEET
height_feet = round(height_feet,1)

print("\n +++++++++")
print("Hello!" + firstname + "\a" +"\n" + "Your name is " + firstname + " " + lastname) 
print("I recevied your information:\n You study at {0} and This is {1} - year student. \n Good for you".format(school_name,str(K_course)))
print(" My class name is: {0}".format(classname))
print(" Your identification number is {0} ".format(iden))
print(" You are {0} years old".format(str(age)) )
print(" You is {0} feet tall".format(str(height_feet)))

# ########################################################
# #Email
# email = input("Your email: ")
# pwd = input("Password: ")
# address = input("Sent to: ")
# msg = input("My infor: ")

# #Send mail
# client = smtplib.SMTP("smtp.gmail.com", 587) #Depart SMTP
# client.starttls()
# client.login(email, pwd)

# client.sendmail(email, address, msg)
# print("Massage send to " + address)
# client.quit() 

# input()
# ########################################################

is_male = None

if (gender_input == "Yes") or (gender_input == "Y") or (gender_input == "yes"):
	is_male = True
elif (gender_input == "No") or (gender_input == "N") or (gender_input == "no"):
	is_male = False
else: 
	is_male = None

if is_male == None:
	print("Invalid Answer")
elif is_male == True:
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
elif is_male == False:
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
else:
	print("Systen Error: Variable 'is_male' is not correct!")
