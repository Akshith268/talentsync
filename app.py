from flask import Flask, render_template, request,session,jsonify,render_template_string
from flask import redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
import bcrypt
from flask import flash
import pandas as pd
from wtforms import IntegerField, SelectField
from wtforms.validators import InputRequired

#Flask App
#------------------------------------------
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.secret_key = "778031a659c117f6ab82986676e24271"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MediSearch.db'
db = SQLAlchemy(app)


