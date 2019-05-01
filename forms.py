# forms.py

from wtforms import Form, StringField, SelectField, validators

class MusicSearchForm(Form):
    choices = [('Tweets', 'Tweets'),
               ('Speeches', 'Speeches'),
               ('Interviews', 'Interviews'),
               ('AllAbove', 'All of the Above')]
    select = SelectField('Enter you search term below:', choices=choices)
    search = StringField('')


class AlbumForm(Form):
    media_types = [('Digital', 'Digital'),
                   ('CD', 'CD'),
                   ('Cassette Tape', 'Cassette Tape')
                   ]
    artist = StringField('Artist')
    title = StringField('Title')
    release_date = StringField('Release Date')
    publisher = StringField('Publisher')
    media_type = SelectField('Media', choices=media_types)
