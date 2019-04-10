from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmiField
from wtforms import Required

class ReviewForm(FlaskForm):
    title = StringField('Review title', validators=[Required()])
    review = TextAreaField('Movies Review', validators=[Required])
    submit = SubmiField('Submit')
    
    
    