from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import TextAreaField, StringField, SubmitField


class PostForm(FlaskForm):
    title = StringField('Title: ', validators=[DataRequired('Every post needs a title.')])
    body = TextAreaField('Post Body: ', validators=[DataRequired('Every post needs a body.')])
    submit = SubmitField('Save')
