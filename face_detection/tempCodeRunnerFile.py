# LOADING WEBCAME STREAM
webcam = cv2.VideoCapture(0)
# PASS VIDEO PATH AS AN ARGUMENT TO ABOVE FUNCTION TO DETECT FACES IN LOCAL VIDEOS

# SAME THING ON WEBCAM
while True:
    is_frame_read_success, frame = webcam.read()
    grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_frame)
    for face_coordinate in face_coordinates:
        (x, y, w, h) = face_coordinate
        cv2.rectangle(frame, (x, y), (x+w, y+h),
                      (randrange(255), randrange(255), randrange(255)), 2)
    cv2.imshow('WEBCAM', frame)
    key = cv2.waitKey(1)

    if(key == 81 or key == 113):
        break

webcam.release()
