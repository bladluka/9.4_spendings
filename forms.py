from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, FloatField
from wtforms.validators import DataRequired

class SpendingsForm(FlaskForm):
    description = StringField('Wydatek', validators=[DataRequired()])
    category = StringField('Kategoria', validators=[DataRequired()])
    value = FloatField('Wartość', validators=[DataRequired()])
    done = BooleanField('Potwierdź', validators=[DataRequired()])