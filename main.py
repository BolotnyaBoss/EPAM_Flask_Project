from flask import Flask, render_template

app = Flask(__name__)

some_data = [
    {
        'title': 'Title1',
        'body': 'There must be some text',
        'author': 'Author1'
    },
    {
        'title': 'Title2',
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


if __name__ == '__main__':
    app.run(debug=True)
