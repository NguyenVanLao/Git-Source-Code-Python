# #Local variable
# def main():
# 	arch_A = "Loai Gioi"
# 	arch_B = "Loai Kha"

# 	hocsinh_A(arch_A)
# 	hocsinh_B(arch_B)

# def hocsinh_A(rankk):
# 	print("Ten: Nguyen Van A")
# 	print("Lop: 12A1")
# 	print("Diem TB Nam: 8.9")
# 	print("Xep loai: " + rankk)

# def hocsinh_B(rankk):
# 	print("Ten: Nguyen Van B")	
# 	print("Lop: 12A2")
# 	print("Diem TB Nam: 7.9")
# 	print("Xep loai: " + rankk)

# main()

#Global variable
def main():
	hocsinh_A()
	hocsinh_B()
def hocsinh_A():
	print("Ten: Nguyen Van A")
	print("Lop: 12A1")
	print("Diem TB Nam: 8.9")
	print("Xep loai: " + arch_A)

def hocsinh_B():
	print("Ten: Nguyen Van B")	
	print("Lop: 12A2")
	print("Diem TB Nam: 7.9")

arch_A = "Loai Gioi"

main()	