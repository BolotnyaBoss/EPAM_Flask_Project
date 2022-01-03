from flask import Flask, render_template, url_for,  flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SECRET_KEY'] = 'e1d0978645e2b4c2dc2542f9de894f06'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    agreements = db.relationship('Agreement', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Agreement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(100), nullable=False)
    date_confirmed = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Agreement('{self.service}', '{self.date_confirmed}')"




some_data = [
    {
        'title': 'Title1',
        'body': 'There must be some text',
        'author': 'Author1'
    },
    {
        'title': 'NewTitle',
        'body': 'There must be some another text',
        'author': 'Author2'
    },
    {
        'title': 'Title3',
        'body': 'There must be different text',
        'author': 'Author3'
    }
]

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/users")
def users():
    return render_template('users.html', data=some_data)


@app.route("/employees")
def employees():
    return render_template('employees.html', data=some_data)


@app.route("/departments")
def departments():
    return render_template('departments.html', data=some_data)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'likht@lpnu.ua' and form.password.data == 'skleroz':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)
