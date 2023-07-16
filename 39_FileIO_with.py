# Write mode - write to a new file
with open("data.txt", "w") as file:
  file.write("Truong THPT Long Hoa\n")
  file.write("Lop 12A1")

  #Write mode - write to a new file
with open("data.txt", "w") as file:
  file.write("Nguyen Van Lao\n")
  file.write("22 years old\n")

# Append mode - write to an existing file
with open("data.txt", "a") as file:
  file.write("Transport University\n")
  file.write("Control and Automation Engineering\n")
  file.write("TD19CLC\n")
  file.write("19H1050036\n")

# Reading mode - Read a file
with open("data.txt", "r") as file:
  data = file.read()
  print(data)
