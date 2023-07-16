# import datetime
# import time

# def hien_thi_gio():
#     gio_hien_tai = datetime.datetime.now()
#     gio = gio_hien_tai.strftime("%H:%M:%S")
#     print("Bây giờ là:", gio)

# def hen_gio():
#     gio_hen = input("Nhập giờ (HH:MM:SS): ")
#     while True:
#         gio_hien_tai = datetime.datetime.now()
#         gio = gio_hien_tai.strftime("%H:%M:%S")
#         if gio == gio_hen:
#             print("Đã đến giờ!")
#             break

# def bam_gio():
#     thoi_gian = int(input("Nhập số giây: "))
#     time.sleep(thoi_gian)
#     print("Đã bấm giờ xong!")

# while True:
#     print("---- ĐỒNG HỒ ----")
#     print("1. Hiển thị giờ hiện tại")
#     print("2. Hẹn giờ")
#     print("3. Bấm giờ")
#     print("0. Thoát")
#     lua_chon = int(input("Nhập lựa chọn của bạn: "))

#     if lua_chon == 1:
#         hien_thi_gio()
#     elif lua_chon == 2:
#         hen_gio()
#     elif lua_chon == 3:
#         bam_gio()
#     elif lua_chon == 0:
#         print("Kết thúc chương trình.")
#         break
#     else:
#         print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

import tkinter as tk
import time

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

# Tạo cửa sổ giao diện
window = tk.Tk()
window.title("Đồng hồ")

# Tạo nhãn cho đồng hồ
clock_label = tk.Label(window, font=("Arial", 80), fg="black", bg="white")
clock_label.pack(padx=50, pady=50)

# Cập nhật đồng hồ ban đầu
update_clock()

# Khởi chạy giao diện
window.mainloop()