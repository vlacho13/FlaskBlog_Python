from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config["SECRET_KEY"] = "3d21da2a78064e29badc9059223a41ea"

posts = [
    {
        'author': 'Vlad Luna',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'November 10, 2018'
    },
    {
        'author': 'Gabe Luna',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'November 10, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)   


if __name__ == '__main__':
    app.run(debug=True)