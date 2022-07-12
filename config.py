from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)