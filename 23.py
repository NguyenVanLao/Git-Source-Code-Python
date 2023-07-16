def print_number(max_number):
	for i in range(max_number):
		print(i)

print_number(5)

# ========Similar======== #
def print_number(max_number):
	for i in range(max_number):
		print(i)

number = 5
print_number(number)

# ***************************** #

def name_number(max_number):
	s_denominator = 0
	for i in range(max_number):
		if i == 1:
			continue
		if i % 2 == 0:
			continue

		print(i)
		s_denominator += 1/i
	s = 1/s_denominator
	s = round(s,2)
	print("S = " + str(s))
number = input(" Max number: ")
name_number(int(number))
