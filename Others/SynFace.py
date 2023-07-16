import cv2
import dlib

# Load pre-trained face detection model
face_detector = dlib.get_frontal_face_detector()

# Load pre-trained face recognition model
face_recognizer = dlib.face_recognition_model_v1('E:/anh/to/shape_predictor_68_face_landmarks.dat')

# Initialize video capture
video_capture = cv2.VideoCapture(0)

# Capture initial frame
ret, frame = video_capture.read()

# Detect faces in the initial frame
faces = face_detector(frame)

    # Select the first face (assuming only one person is in the frame)
if len(faces) > 0:
    face = faces[0]
    landmarks = face_recognizer(frame, face)

# Main loop
while True:
    # Read frame from video capture
    ret, frame = video_capture.read()

    # Detect faces in the frame
    faces = face_detector(frame)

    # Select the first face (assuming only one person is in the frame)
    if len(faces) > 0:
        face = faces[0]
        landmarks = face_recognizer(frame, face)

        # Perform optical modifications based on the face landmarks
        # Modify the frame according to the desired optical changes

    # Display the modified frame
    cv2.imshow('Video', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close windows
video_capture.release()
cv2.destroyAllWindows()
