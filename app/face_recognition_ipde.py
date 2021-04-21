import face_recognition

def face_rec(path_refference_img, data):
    refference_img = face_recognition.load_image_file(path_refference_img)
    refference_face_encoding = face_recognition.face_encodings(refference_img)[0]

    # data = face_recognition.load_image_file(data) # edited
    
    new_face_encoding = face_recognition.face_encodings(data)[0]
    results = face_recognition.compare_faces([refference_face_encoding], new_face_encoding)

    if results[0] == True:
        print("It's a picture of me!")
        return True # Disarm
    else:
        print("It's not a picture of me!")
        return False # Arm
