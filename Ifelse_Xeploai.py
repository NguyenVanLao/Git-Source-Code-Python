Grate = input("Nhap diem hoc sinh: ")
Grate = float(Grate)
Taskgrate = input("Nhap diem ren luyen: ") 
Taskgrate = int(Taskgrate)
if Grate >= 8.0:
	print("Ban dat danh hieu hsg")
	if Taskgrate > 85:
		print("Ban du dieu kien xet HB loai gioi")
	elif Taskgrate > 65:
		print("Ban dat hoc bong loai kha")
	else:	
		print("Khong dat HB Gioi")
elif Grate >= 6.5 and Grate < 8.0: 
	print("Ban dat danh hieu hsk")
	if Taskgrate > 65:
		print("Ban du dieu kien xet HB loai kha")
	else:
		print("Khong du dieu kien xet HB")
else: 
	print("Hoc sinh tb. Ban co gang hon nhe!\nBan hay tiep tuc ren luyen nua nhe!")
    
