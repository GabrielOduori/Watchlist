from flask import Flask
from .config import DevConfig
from .config import DevConfig


# Initializing application
app = Flask(__name__)

# Seting up configuration
app.config.from_object(DevConfig)

from app import views