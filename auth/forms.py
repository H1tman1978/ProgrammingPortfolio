from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms import StringField
from wtforms import BooleanField
from wtforms import SubmitField
from wtforms.validators import Email
from wtforms.validators import EqualTo
from wtforms.validators import InputRequired
from wtforms.validators import Length
from wtforms.validators import ValidationError

from .form_utils import *
from .models import User


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[InputRequired(message=REQUIRED_FIELD)
                                       ]
                           )
    password = PasswordField('Password', validators=[InputRequired(message=REQUIRED_FIELD)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
                             validators=[InputRequired(message=REQUIRED_FIELD),
                                         Length(min=3, max=25, message="First Name Field must be between 3 and 25 "
                                                                       "characters long.")
                                         ]
                             )
    last_name = StringField('Last Name',
                            validators=[InputRequired(message=REQUIRED_FIELD),
                                        Length(min=3, max=30, message="Last Name Field must be between 3 and 30 "
                                                                      "characters long.")
                                        ]
                            )

    phone_number = StringField('Phone Number',
                               validators=[InputRequired(message=REQUIRED_FIELD), Length(min=10, max=20)])
    email = StringField('Email',
                        validators=[InputRequired(message=REQUIRED_FIELD),
                                    Email(message="Please enter a valid email. Ex email@example.com"),
                                    Length(min=5, max=120)])
    username = StringField('Username',
                           validators=[InputRequired(message=REQUIRED_FIELD),
                                       Length(min=3, max=30, message=USERNAME_LENGTH)])
    password = PasswordField('Password',
                             validators=[InputRequired(message=REQUIRED_FIELD),
                                         EqualTo('confirm', message='Passwords must match.'),
                                         Length(min=10, message="Password must be at least 10 characters long")])
    confirm = PasswordField('Confirm Password', validators=[InputRequired(message=REQUIRED_FIELD)])

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('A user is already registered with that username. Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('A user is already registered with that email address. Please use a different email '
                                  'address.')

    def validate_phone_number(self, phone_number):
        user = User.query.filter_by(phone_number=phone_number.data).first()
        if user is not None:
            raise ValidationError('A user is already registered with that phone number. Please use a different phone '
                                  'number.')
