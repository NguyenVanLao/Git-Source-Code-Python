class Student:
	def __init__(self,name,age,ID,match_score,lit_score):
		self.name = name
		self.age = age
		self.ID = ID
		self.match_score = match_score
		self.lit_score = lit_score
		self.teacher = "Dung lai"
	def average_score(self):
		self.ave_score = (self.match_score + self.lit_score)/2
		return self.ave_score
	def print_info(self):
		ave_score = str(self.average_score())
		print("Your information:")
		print("Your name is: " + self.name + "\n" "MSSV: " + self.ID)
		print("Studetn name is " + self.name + " study with " + self.teacher + " have average score " + ave_score)
students = []
s1 = Student("Lao",22,"22H1050036",5,7)
s2 = Student("Jane",19,"19H1050036",9,7)
s3 = Student("Peter",20,"20H1050036",5,4)

# s1.name = "Lao"
# s1.age = 22
# s1.ID = "19H1050036"
# s1.match_score = 9
# s1.lit_score = 7 	

students.append(s1)
students.append(s2)
students.append(s3)

for i in range(len(students)):
	students[i].print_info()
	