import logging
from logging.handlers import SMTPHandler
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_login import LoginManager
from flask import Flask

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

moment = Moment(app)
bootstrap = Bootstrap(app)
mail = Mail(app)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
from app import routes, models, errors
