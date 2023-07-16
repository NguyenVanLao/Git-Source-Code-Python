# Create a program that asks an user to enter an integer
# Write to a file named "data.txt" all integers from the previous integer to 0 on each line
# Read the file "data.txt" and print to the terminal all lines and its corresponding integer

in_number = int(input("Nhap so nguyen vao: "))

with open("data.txt", "w") as file:
	for i in range(in_number):
		file.write(str(in_number - i) + "\n")

numbers = []
with open("data.txt", "r") as file:
	numbers = file.read().split() 

for i in range(len(numbers)):
	print("Line " + str(i+1) + ": ", numbers[i])