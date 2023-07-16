import dlib

# Đường dẫn đến tập dữ liệu huấn luyện
training_data_path = 'E:/Picture/Input/to/training_data.xml'

# Khởi tạo đối tượng trainer
options = dlib.shape_predictor_training_options()

# Thiết lập các tham số huấn luyện
options.cascade_depth = 10
options.num_trees_per_cascade_level = 500
options.nu = 0.1
options.oversampling_amount = 20
options.feature_pool_size = 400
options.num_test_splits = 50

# Bắt đầu quá trình huấn luyện
predictor = dlib.train_shape_predictor(training_data_path,'E:/Picture/Output/to/shape_predictor_68_face_landmarks.dat', options)

# Lưu file shape_predictor_68_face_landmarks.dat
output_file = 'E:/Picture/Output/to/shape_predictor_68_face_landmarks.dat'
predictor.save(output_file)

#------------------------------------------------------
# import os
# import dlib
#
# # Lấy đường dẫn tới thư mục chứa file shape_predictor_68_face_landmarks.dat
# folder_path = 'E:/Picture'
#
# # Tạo đường dẫn đầy đủ tới file shape_predictor_68_face_landmarks.dat
# file_path = os.path.join(folder_path, 'shape_predictor_68_face_landmarks.dat')
#
# # Kiểm tra xem file có tồn tại không
# if not os.path.isfile(file_path):
#     print(f"Không tìm thấy file shape_predictor_68_face_landmarks.dat trong thư mục {folder_path}")
#     exit()
#
# # Tạo mô hình nhận dạng khuôn mặt
# face_recognizer = dlib.face_recognition_model_v1(file_path)

#------------------------------------------------------
# import os
#
# file_path = 'E:/Picture/shape_predictor_68_face_landmarks.dat'
# if os.path.exists(file_path):
#     print("File tồn tại")
# else:
#     print("File không tồn tại")

#------------------------------------------------------
# import cv2
# import dlib
#
# # Load pre-trained face detection model
# face_detector = dlib.get_frontal_face_detector()
#
# # Loaf pre-trained face recognition model
# face_recognizer = dlib.face_recognition_model_v1('E:/anh/to/shape_predictor_68_face_landmarks.dat')
#
# # Initialize video capture
# video_capture = cv2.VideoCapture(0)
#
# # Capture initail frame
# ret, frame = video_capture.read()
#
# # Detect faces in the initial frame
# faces = face_detector(frame)
#
# #Select the first face (assuming only one person is in the frame)
# if len(faces) > 0:
#     face = faces[0]
#     landmarks = face_recognizer(frame,face)
#
# # Main loop
# while True:
#     # Read frame from video capture
#     ret, frame = video_capture.read()
#
#     # Detect faces in the frame
#     faces = face_detector(frame)
#
#     # Select the first face (assuming only one person is in the frame)
#     if len(faces) > 0:
#         face = faces[0]
#         landmarks = face_recognizer(frame, face)
#
#         # Perform optical modifications based on the face landmarks
#         # Modify the frane according to the desired optical changes
#
#     # Display the modified frame
#     cv2.imshow('video',frame)
#
#     # Break lood if 'w' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('w'):
#         break
#
# # Release video capture and close windows
# video_capture.release()
# cv2.destroyAllWindows()