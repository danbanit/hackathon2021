# coding=utf-8

from flask import request, render_template, flash, redirect, session, url_for, request, g, Markup
from app import app
# import face_recognition 

# from face_recognition_ipde import face_rec
# from fcMqttClient import mqttSendDisarm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/faceRecognize', methods = ['POST'])
def faceRecognize():
    try:
        data = request.get_data() # got from cp
        app.logger.info("/faceRecognize called")
        f = open("/tmp/fr.jpeg", 'wb')
        f.write(bytearray(data))
        f.close()
        
        # refference_img = face_recognition.load_image_file('dan.jpg')
        # refference_face_encoding = face_recognition.face_encodings(refference_img)[0]
        # new_face_encoding = face_recognition.face_encodings(data)[0]
        # results = face_recognition.compare_faces([refference_face_encoding], new_face_encoding)
        
        # if results[0] == True:
        #     app.logger.info("face recognize")
        #     # mqttSendDisarm()
        # else:
        #     app.logger.info("face didn't recognize")
        return "", 200

    except Exception as e:
        return str(e), 404