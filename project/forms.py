from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo


class RegisterForm(Form):
	fullName = StringField('Full Name', validators=[DataRequired(), Length(max=40)])
	username = StringField('Username', validators=[DataRequired(), Length(max=16)])
	password = PasswordField('Password', validators=[DataRequired(), Length(max=40)])
	confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])


class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(max=16)])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=40)])

class PostForm(Form):
	title = StringField('Title', validators=[DataRequired()])
	text = StringField('Text', validators=[DataRequired()])     

