from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms import ValidationError, validators


class RegisterForm(Form):
    userNameText = 'Username'
    userNameField = StringField(userNameText, [validators.required('Please enter username'),validators.Email('Please enter email')],
                                render_kw={"placeholder": userNameText},)
    registerButtonText = "Register"
    registerButtonField = SubmitField(registerButtonText)
