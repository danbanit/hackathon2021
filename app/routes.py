# coding=utf-8

from flask import render_template, flash, redirect, session, url_for, request, g, Markup
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
    # data = request.files['file'].read()
    return "", 200




