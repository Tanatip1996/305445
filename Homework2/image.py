from flask import Flask , request
from flask_restful import Resource ,Api,reqparse
import json,time
from datetime import datetime,date
from werkzeug.datastructures import FileStorage

app = Flask (__name__)

api = Api(app)

def calculate_age(born):
	today = date.today()
	return today.year-born.year-((today.month, today.day) < (born.month, born.day))

parser = reqparse.RequestParser()
parser.add_argument('birthdate')
parser.add_argument('image', type=FileStorage, location='files')
