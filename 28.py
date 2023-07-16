
def main():
	hocsinh_A_Ten = "Nguyen Van A"
	hocsinh_A_Lop = "12A1"
	hocsinh_A_DTB = 9

	hocsinh_B_Ten = "Nguyen Van B"
	hocsinh_B_Lop = "12A2"
	hocsinh_B_DTB = 7
	
	infor_student(hocsinh_A_Ten, hocsinh_A_Lop,hocsinh_A_DTB)
	infor_student(hocsinh_B_Ten, hocsinh_B_Lop,hocsinh_B_DTB)

def infor_student(Ten, Lop, DTB):
	print("Name " + Ten)
	print("Lop " + Lop)
	print("DTB " + str(DTB))

main()	