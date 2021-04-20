import face_recognition
import argparse



parser = argparse.ArgumentParser(description='Get two images.')
parser.add_argument('--img_known', type=str,
                    help='Path for known person img')
parser.add_argument('--img_unknown', type=str,
                    help='Path for unknown person img')

args = vars(parser.parse_args())

path_refference_img = args["img_known"]
path_new_img = args["img_unknown"]


refference_img = face_recognition.load_image_file(path_refference_img)
refference_face_encoding = face_recognition.face_encodings(refference_img)[0]

face_locations = face_recognition.face_locations(refference_img)
print("I found {} face(s) in this photograph.".format(len(face_locations)))

# my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

new_img = face_recognition.load_image_file(path_new_img)
new_face_encoding = face_recognition.face_encodings(new_img)[0]

face_locations = face_recognition.face_locations(new_img)
print("I found {} face(s) in this photograph.".format(len(face_locations)))

# Now we can see the two face encodings are of the same person with `compare_faces`!

results = face_recognition.compare_faces([refference_face_encoding], new_face_encoding)

if results[0] == True:
    print("It's a picture of me!")
else:
    print("It's not a picture of me!")

face_distance = face_recognition.api.face_distance([refference_face_encoding], new_face_encoding)
print("Face distance: {}".format(face_distance))
