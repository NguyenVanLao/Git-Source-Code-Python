# Write mode - write to a new file
file = open("data.txt", "w")
file.write("Truong THPT Long Hoa\n")
file.write("Lop 12A1")
file.close()

  #Write mode - write to a new file
file = open("data.txt", "w")
file.write("Nguyen Van Lao\n")
file.write("22 years old\n")
file.close()

# Append mode - write to an existing file
file = open("data.txt", "a")
file.write("Transport University\n")
file.write("Control and Automation Engineering\n")
file.write("TD19CLC\n")
file.write("19H1050036\n")
file.close()

# Reading mode - Read a file
file = open("data.txt", "r")
data = file.read()
print(data)
file.close()