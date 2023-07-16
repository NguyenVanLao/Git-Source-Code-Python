# import cv2
# import numpy as np
# def sharpen_image(image_path, output_path):
#     # Đọc ảnh đầu vào
#     image = cv2.imread(image_path)
#
#     # Tạo kernel sắc nét
#     kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
#
#     # Áp dụng bộ lọc sắc nét
#     sharpened_image = cv2.filter2D(image, -1, kernel)
#
#     # Ghi ảnh đã được nét lại ra file
#     cv2.imwrite(output_path, sharpened_image)
#
#
# # Đường dẫn tới ảnh đầu vào và đầu ra
# input_image_path = 'E:/Py_Doc/Others/NetAnh/input/image2.jpg'
# output_image_path = 'E:/Py_Doc/Others/NetAnh/output/image2.jpg'
#
# # Gọi hàm xử lý nét lại ảnh
# sharpen_image(input_image_path, output_image_path)

import cv2


def smooth_image(image_path, output_path):
    # Đọc ảnh đầu vào
    image = cv2.imread(image_path)

    # Áp dụng bộ lọc Gaussian
    smoothed_image = cv2.GaussianBlur(image, (5, 5), 0)

    # Ghi ảnh đã được làm mượt ra file
    cv2.imwrite(output_path, smoothed_image)


# Đường dẫn tới ảnh đầu vào và đầu ra
input_image_path = 'E:/Py_Doc/Others/NetAnh/output/image3.jpg'
output_image_path = 'E:/Py_Doc/Others/NetAnh/output/image33.jpg'

# Gọi hàm làm mượt ảnh
smooth_image(input_image_path, output_image_path)