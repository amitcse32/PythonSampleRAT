from flask import Flask, render_template, request, flash
from src.routes import *
from src.initials import *
from src.forms.AllForms import *

app = Flask(__name__, template_folder=templateFolder)
app.secret_key = SECRET_KEY


@app.route("/")
@app.route(homeRoute)
def home():
    return "Welcome Page " + APPLICATION_MODE


@app.route(loginRoute)
def login():
    return "Login Page " + APPLICATION_MODE


@app.route(registerRoute, methods=['POST', 'GET'])
def register():
    registerForm = RegisterForm()
    if request.method == 'POST':
        if not registerForm.validate():
            flash('All fields are required.')
            return render_template('registertemp.html', form=registerForm)
        else:
            return "SUCCESS"
    else:
        return render_template('registertemp.html', form=registerForm)


@app.route(forgotPasswordRoute)
def forgotPassword():
    return "Forgot Password Page " + APPLICATION_MODE


if __name__ == '__main__':
    app.run(debug=DEBUG_MODE)
