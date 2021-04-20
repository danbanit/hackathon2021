# coding=utf-8

from flask import request, render_template, flash, redirect, session, url_for, request, g, Markup
from app import app

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
        data = request.get_data()
        app.logger.info("/faceRecognize called")
        f = open("/tmp/fr.jpeg", 'wb')
        f.write(bytearray(data))
        f.close()
        return "", 200
    except Exception as e:
        return str(e), 404




