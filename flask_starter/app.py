#!/usr/bin/env python
import sys
import click
from flask import Flask

from flask_starter.config import Config
from flask_starter.frontend import frontend


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(frontend)


if __name__ == '__main__':
    click.secho('\nPlease launch the demo API with\n', err=True)
    click.secho('    export FLASK_APP=flask_starter/app.py', bold=True,
                err=True)
    click.secho('    flask run [--host=X.X.X.X] [--port=YYYY]\n', bold=True,
                err=True)
    sys.exit(1)
