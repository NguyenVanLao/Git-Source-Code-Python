def total_apple_price(apple_weight, APPLE_PRICE):
	return apple_weight*APPLE_PRICE

def total_return_money(total_apple, money_customer):
	if money_customer < total_apple:
		return -1 # Tra ve mot truong hop dac biet 
	else:
		return money_customer - total_apple

def type_currency(total):
	count_500 = int(total/500)
	total = total - 500*count_500
	if count_500 != 0:
		print("Currency of 500k:  " + str(count_500))

	count_200 = int(total/200)
	total = total - 200*count_200
	if count_200 != 0:
		print("Currency of 200k:  " + str(count_200))

	count_100 = int(total/100)
	total = total - 100*count_100
	if count_100 != 0:
		print("Currency of 100k:  " + str(count_100))

	count_50 = int(total/50)
	total = total - 50*count_50
	if count_50 != 0:
		print("Currency of 50k:   " + str(count_50))

	count_20 = int(total/20)
	total = total - 20*count_20
	if count_20 != 0:
		print("Currency of 20k:   " + str(count_20))

	count_10 = int(total/10)
	total = total - 10*count_10
	if count_10 != 0:
		print("Currency of 10k:   " + str(count_10))

	count_5 = int(total/5)
	total = total - 5*count_5
	if count_5 != 0:
		print("Currency of 5k:    " + str(count_5))

	count_2 = int(total/2)
	total = total - 2*count_2
	if count_2 != 0:
		print("Currency of 2k:    " + str(count_2))

	count_1 = int(total)
	total = total - 1
	if count_1 != 0:	
		print("Currency of 1k:    " + str(count_1))

def main():
	APPLE_PRICE = 20 # kVND
	apple_weight = input("Write kg of apples: ")
	money_customer = input("Money is received by customer: ")

	apple_weight = float(apple_weight)
	money_customer = float(money_customer)

	total_apple = total_apple_price(apple_weight, APPLE_PRICE)
	return_money = total_return_money(total_apple, money_customer)

	print("Total of money customer cash: " + str(total_apple))

	if return_money == -1:
		print("Money is not enough to cash from customer")
	else:
		print("You need to return to customer: " + str(int(return_money)) + "000 VND")
		type_currency(return_money)

main()











