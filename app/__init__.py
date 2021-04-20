from flask import Flask
import logging
logging.basicConfig(
    filename='/tmp/dockerFr.log',
	format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

app = Flask(__name__)
# app.config.from_object('config')
from app import routes

