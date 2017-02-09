#!/usr/bin/env python
import os
import click
from flask import Flask, render_template

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    TEMPLATES_AUTO_RELOAD=True,
    EXPLAIN_TEMPLATE_LOADING=True,
    PROJECT_ROOT=os.path.abspath(os.path.dirname(__file__)),
)


@app.route('/')
def index():
    return render_template('index.html')


@app.cli.command(with_appcontext=False)
def clean():
    """
    Clean up .pyc files (and other detritus)
    """
    click.secho('Tidying up the project directories...', fg='yellow')
    os.chdir(app.config['PROJECT_ROOT'])
    for subdir in ['.', 'templates', 'static/css', 'static/js']:
        try:
            click.secho('  - %s' % subdir)
            os.system("rm %s/*.pyc" % subdir)
            os.system("rm -rf %s/__pycache__" % subdir)
            os.system("rm %s/.*.un~" % subdir)
        except:
            click.secho('    Oops. A failure occurred cleaning %s' % subdir,
                        fg='red')

    click.secho('\nAll done.', fg='green')


if __name__ == '__main__':
    click.secho('\nPlease launch the demo API with\n', err=True)
    click.secho('    export FLASK_APP=api.py', bold=True,
                err=True)
    click.secho('    flask run [--host=X.X.X.X] [--port=YYYY]\n', bold=True,
                err=True)
    sys.exit(1)
