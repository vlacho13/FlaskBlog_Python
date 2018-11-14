from flask import Flask, render_template, url_for, flash, redirect
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
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data }!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login error, please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)   


if __name__ == '__main__':
    app.run(debug=True)