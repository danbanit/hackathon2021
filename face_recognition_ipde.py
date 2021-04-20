import face_recognition
import argparse


def face_rec(refference_img, data)
    #refference_img = face_recognition.load_image_file(path_refference_img)
    refference_face_encoding = face_recognition.face_encodings(refference_img)[0]

    #face_locations = face_recognition.face_locations(refference_img)
    #print("I found {} face(s) in this photograph.".format(len(face_locations)))

    # my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

    #new_img = face_recognition.load_image_file(path_new_img)
    new_face_encoding = face_recognition.face_encodings(data)[0]

    face_locations = face_recognition.face_locations(new_img)
    #print("I found {} face(s) in this photograph.".format(len(face_locations)))

    # Now we can see the two face encodings are of the same person with `compare_faces`!

    results = face_recognition.compare_faces([refference_face_encoding], new_face_encoding)

    if results[0] == True:
	return True  # Disarm
        print("It's a picture of me!")
    else:
        return False # Arm
        print("It's not a picture of me!")

    #face_distance = face_recognition.api.face_distance([refference_face_encoding], new_face_encoding)
    #print("Face distance: {}".format(face_distance))
