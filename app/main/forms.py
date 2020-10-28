from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField,SelectField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class UpdateProfile(FlaskForm):
    about=TextAreaField("Tell us about you.",validators=[Required()])
    submit=SubmitField("Submit")


class WritePitch(FlaskForm):
    title=StringField("Title of your Idea",validators=[Required()])
    categ=SelectField("Choose Category",choices=[('c','select'),('RI','Re-wild the finance industry'),('ST','Stop treating the planet like a machine'),('DMD','Deploy mindfulness to develop less consumption-focused identities'),('GEW','GeW')],validators=[Required()])
    pitch=TextAreaField("In 200 words Write your Idea",validators=[Required()])
    submit=SubmitField("Submit")

class ReviewForm(FlaskForm):
    title=StringField(" Comment title",validators=[Required()])
    comments=TextAreaField("Comments",validators=[Required()])
    submit=SubmitField("Submit")