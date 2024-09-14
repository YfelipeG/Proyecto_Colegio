import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import ConfigDevelopment


app = Flask(__name__)

base_dir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(base_dir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

  

from app import models


from app import routes