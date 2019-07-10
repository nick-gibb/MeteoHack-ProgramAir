from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

from ac_calc.data import get_ac_brands

choices = [(g, g) for g in get_ac_brands()]


class LoginForm(FlaskForm):
    postal = StringField('What is your postal code? This is needed to personalize your cost estimate (i.e. the local energy cost, building design, and climate).', validators=[DataRequired()])
    years = StringField('Which year would you like to cost estimate? Enter year(s) between 1959-2100, seperated by commas.', default='1969, 2019, 2099', validators=[DataRequired()])
    brand = SelectField('Air conditioner manufacturer:', choices=choices)
    model = SelectField('Air conditioner model', choices=[('', '')])
    submit = SubmitField('Estimate Air Conditioner Energy Costs')
