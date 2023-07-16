import math


def add_one(number):
	number = number + 1
	return number
x = 2 
x = add_one(x)
print(x)

############Pytago###############s
a = 0 
def add_one(number):
	number = number + 1
	return number

x = input("Nhập giá trị của x: ")
x = add_one(int(x))
print(x)

y = input("Nhập giá trị của y: ")
y = add_one(int(y))
print(y)

a = math.sqrt(x*x + y*y)
a = round(a,2)
print("Canh huyen = " + str(a))

############Pytago###############
def add_one(a, b):
	s = math.sqrt(a*a + b*b)
	s = round(s,2)
	return s

x = input("Nhập giá trị của x: ")
x = int(x)
y = input("Nhập giá trị của y: ")
y = int(y)
ch = add_one(x,y)
print("Canh huyen =: " + str(ch))

