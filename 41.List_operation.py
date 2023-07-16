	#LIST: remove, insert, index, colors[], 
	#      pop(), try(except),append(), len(), count(),
	#      
colors = ["Green", "Red", "Blue","Lao","Green", 11]
print(colors)
#-----------------------------------
# #Remove from list
if "Red" in colors: #Validation: kiem tra code hoat dong
	colors.remove("Red")
else:
	print("Not exist")	
print(colors)
#-----------------------------------
#Remove from list
try:
	colors.remove("Red")
except:
	print("Not exist")
print(colors)

# #Remove last element
colors.pop() #Delete stack in above
print(colors)

#-----------------------------------
#Insert color in list
colors.insert(0,"Black")
print(colors)
colors.insert(11,"Nguyen")
print(colors)
colors.insert(12,"Laof")
print(colors.index("Laof"))

# #-----------------------------------
# #Find index of the first "Green" in list
try:
	print(colors.index("Green"))
except:
	print("Not exist")

#-----------------------------------
#Find index of "Green" in list
green_index = []
for i in range(len(colors)):
	if colors[i] == "Green":
		green_index.append(i)
print("The word 'Green' occurs at the following index: ", end = "")
#Ghi de khong xuong dong khi su dung print(green_index)
print(green_index)

#Find number of occurance of "green"
print("Mau xanh la trong list co: ",colors.count("Green"))

#-----------------------------------
#Arrange in list
a = [0,6,8,4,2]
a.sort()
print("Sort example: ", end = "")
print(a)

# Change the first element to "Lao Nguyen"
a[0] = "Lao NGUYEN"


#Sau đây là mã hoàn chỉnh để loại bỏ các phần tử giống nhau trong danh sách và lưu kết quả vào danh sách mới:

python
Copy code
my_list = [1, 2, 3, 4, 2, 5, 1, 6, 7, 8, 6]
unique_list = set(my_list)
result_list = list(unique_list)

print(result_list)
#Kết quả của đoạn mã trên sẽ là danh sách mới chứa các phần tử duy nhất: [1, 2, 3, 4, 5, 6, 7, 8]. Các phần tử giống nhau đã được loại bỏ.