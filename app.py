from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, connect_db, Pet
from form import PetForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)