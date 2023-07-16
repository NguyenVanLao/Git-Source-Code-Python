#Input integer number (n) from keyboard and inspect: Is n prime number ?
#If n = 1, notify n isn't prime number
#If n is composite number, print n and analysis equivalent prime factor

#---------------------------------------------------------------------
def is_prime(number):
	if number < 2:
		return False
#Kiem tra gioi han tren de xet cac uoc cua number (2 => Can bac 2(number))
	for i in range(2, int(number**0.5) + 1):
		if number % i == 0:
			return False
	return True

number = int(input("Nhap so tu nhien n:"))

if is_prime(number):
	print(number, ": la so nguyen to")
else:
	print(number, ": khong la so nguyen to") 

#---------------------------------------------------------------------
n = int(input("Nhap so tu nhien n: "))
m = n
k = 2
numbers = []
while m > 1:
	while m%k != 0:
		k = k + 1
	numbers.append(k)
	m = m//k
count = len(numbers)
if count == 0:
	print(n, ": khong phai la so nguyen to")
elif count == 1:
	print(n,": la so nguyen to")
else:
	print(str(n) + ": la hop so")
	print(str(n) +" =", end = " ")
	for i in range(count):
		if i < count < -1:
			print(numbers[i],"x",end = "")
		else: 
			print(numbers[i])