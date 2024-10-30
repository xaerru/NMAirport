import os
from dotenv import load_dotenv

class Config:
    load_dotenv()
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
