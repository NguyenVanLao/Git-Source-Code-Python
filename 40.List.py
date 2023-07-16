colors = ["Green", "Red", "Blue"]

colors.append("Lao") #Them du lieu vao cuoi list

print(colors)
print(len(colors)) #So luong du lieu trong list

for i in range(len(colors)):
	print(colors[i])

last_index = len(colors)-1
print(colors[-1])