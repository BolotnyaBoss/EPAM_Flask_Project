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
@app.route("/home")
def home():
    return render_template('home.html', data=some_data)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
