from dotenv import load_dotenv
import os

load_dotenv()

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False

ADMIN_USERNAME = os.getenv('ADMIN_PASSWORD')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')