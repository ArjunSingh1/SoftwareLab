# forms.py

from wtforms import Form, StringField, SelectField

class GameSearchForm(Form):
    choices = [('All_Games', 'All_Games'), ('Exclusive_Games', 'Exclusive_Games'), ('PS4_Games', 'PS4_Games'), ('XboxOne_Games', 'XboxOne_Games'), ('PS3_Games', 'PS3_Games'), ('Xbox360_Games', 'Xbox360_Games'), ('WiiU_Games', 'WiiU_Games'), ('Switch_Games', 'Switch_Games')]
    select = SelectField('Search for games:', choices=choices)
    search = StringField('')