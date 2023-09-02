from flask import Blueprint, render_template
from forms import UserLoginForm, UserSignUpForm

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/tequilaprofile')
def tequilaprofile():
    return render_template('tequilaprofile.html')

@site.route('/signin')
def signin():
    form = UserLoginForm()
    return render_template('signin.html', title='signinn', form=form)

@site.route('/signup')
def signup():
    form = UserSignUpForm()
    return render_template('signup.html', title='signup', form=form)