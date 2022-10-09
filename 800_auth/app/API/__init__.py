# -*- coding: utf-8 -*-
"""This module contains initialization code for the API package."""

from dotenv import load_dotenv
from flask import Flask
import os
from .config import config


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


app = Flask(__name__)
config_name = os.getenv('FLASK_CONFIG', 'development')
app.config.from_object(config[config_name])


from API import routes