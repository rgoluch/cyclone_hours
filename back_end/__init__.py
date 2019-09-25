from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

back_end = Flask(__name__)
back_end.config.from_object(Config)
db = SQLAlchemy(back_end)
migrate = Migrate(back_end, db)
login = LoginManager(back_end)
login.login_view = 'login'

from back_end import routes