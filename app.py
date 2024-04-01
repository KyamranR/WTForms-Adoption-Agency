from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, connect_db, Pet
from form import PetForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    """Home page"""
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Adding a Pet"""
    form = PetForm()
    if form.validate_on_submit():
        new_pet = Pet(
            name = form.name.data,
            species = form.species.data,
            photo_url = form.photo_url.data,
            age = form.age.data,
            notes = form.notes.data,
            available = form.available.data
        )
        db.session.add(new_pet)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_pet.html', form=form)


@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def pet_details(pet_id):
    """Editing pet details"""
    pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj=pet)
    if form.validate_on_submit():
        form.populate_obj(pet)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('pet_details.html', pet=pet, form=form)

if __name__ == '__main__':
    app.run(debug=True)