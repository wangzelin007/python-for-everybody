# -*- coding: utf-8 -*-
"""Commands used to start and test the application."""
from flask.cli import FlaskGroup

from API import app

cli = FlaskGroup(app)

if __name__ == '__main__':
    cli()