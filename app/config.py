import os

class Config:
    SECRET_KEY = os.environ.get('ghostmode')  or 'you-will-never-guess'