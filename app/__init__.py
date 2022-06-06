from flask import Flask

from config import Config as conf
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(conf)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models