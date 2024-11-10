from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

# Add debug prints
print(f"Current ENV value: {os.getenv('ENV')}")
print(f"Current working directory: {os.getcwd()}")

if os.getenv('ENV') == 'local':
    print("Running in local mode")
    app.config.from_object('config.LocalConfig')
    # Print the database URI to verify
    print(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
elif os.getenv('ENV') == 'dev':
    print("Running in development mode")
    app.config.from_object('config.DevelopmentConfig')
elif os.getenv('ENV') == 'ghci':
    print("Running in github mode")
    app.config.from_object('config.GithubCIConfig')
else:
    print("Running in production mode")
    app.config.from_object('config.DevelopmentConfig')  # Changed from ProductionConfig since it doesn't exist

db = SQLAlchemy(app)

from iebank_api.models import Account

# Add error handling for database creation
try:
    with app.app_context():
        db.create_all()
        print("Database tables created successfully")
except Exception as e:
    print(f"Error creating database tables: {str(e)}")

CORS(app)

from iebank_api import routes