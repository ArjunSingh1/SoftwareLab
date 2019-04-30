# forms.py

from wtforms import Form, StringField, SelectField

class GameSearchForm(Form):
    choices = [('All', 'All'), ('Exclusives', 'Exclusives'), ('PS4', 'PS4'), ('Xbox One', 'Xbox One'), ('PS3', 'PS3'), ('Xbox 360', 'Xbox 360'), ('Wii U', 'Wii U'), ('Nintendo Switch', 'Nintendo Switch'), ('Highest Rated', 'Highest Rated'), ('Lowest Rated', 'Lowest Rated')]
    select = SelectField('', choices=choices)
    search = StringField('')