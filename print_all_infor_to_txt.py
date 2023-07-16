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
def cal_age(year_born):
	import datetime

	now = datetime.datetime.now()
	formatted_time = now.strftime("%Y")

	CURRENT_YEAR = int(formatted_time)
	return CURRENT_YEAR - year_born

def cal_grade(start_year):
	import datetime

	now = datetime.datetime.now()
	formatted_time = now.strftime("%Y")

	CURRENT_YEAR = int(formatted_time)
	return CURRENT_YEAR - start_year

def convert_meter_to_feet(meter):
	METER_TO_FEET = 3.281
	feet = meter*METER_TO_FEET 	
	feet = round(feet,1)
	return feet

def print_height_feet(is_male, height_feet, is_VN):
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

def print_peronal_info(firstname, lastname, school_name, K_course, classname, iden, age, is_VN, is_male, height_feet):
		#Terminator result
	print("\n +++++++++")
	print("Hello!" + firstname + "\a" +"\n" + "Your name is " + firstname + " " + lastname) 
	print("I recevied your information:\n You study at {0} and This is {1} - year student. \n Good for you".format(school_name,str(K_course)))
	print(" My class name is: {0}".format(classname))
	print(" Your identification number is {0} ".format(iden))
	print(" You are {0} years old".format(str(age)) )
	print(" You is {0} feet tall".format(str(height_feet)))
	print_height_feet(is_male, height_feet, is_VN)

def ask_personal_info():
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
	return firstname, lastname, year_born, school_name, start_year, height_meter, iden, classname, is_male, is_VN

def main():
	#Process data
	firstname, lastname, year_born, school_name, start_year, height_meter, iden, classname, is_male, is_VN = ask_personal_info()
	K_course = cal_grade(start_year)	
	age = cal_age(year_born)
	height_feet = convert_meter_to_feet(height_meter)
	print_peronal_info(firstname, lastname, school_name, K_course, classname, iden, age, is_VN, is_male, height_feet) 

main()

