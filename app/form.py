import os
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
    file_upload = FileField('UploadImage', validators=[FileRequired(), FileAllowed(['png', 'jpg'], 'Incorrect File Type, Try again.')])



