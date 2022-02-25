from flask_wtf import FlaskForm
from flask_wtf.file import _FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
    file_upload = _FileField('Upload Image', validators=[FileRequired(), FileAllowed(['png', 'jpg'], 'Incorrect File Type, Try again.')])
    

