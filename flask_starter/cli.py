import os
import sys
import glob
import click
from flask.cli import FlaskGroup

from flask_starter.app import app

clean_these = ['.', 'templates', 'static/css', 'static/js']

# ========================================================================
#                  c o m m a n d - l i n e   t a s k s
# ========================================================================

@click.group(cls=FlaskGroup)
def main():
    """
    Management commands for the Flask-Starter web application
    """
    pass


@main.command(with_appcontext=False)
def clean():
    """
    Clean up .pyc files (and other detritus)
    """
    click.secho('Tidying up the project directories...', fg='yellow')
    os.chdir(app.config['PROJECT_ROOT'])
    for subdir in clean_these:
        click.secho('  - %s' % os.path.abspath(subdir))
        for root, dirs, _ in os.walk(subdir):
            try:
                for f in glob.glob('%s/*.pyc' % root):
                    os.remove(f)
                if '__pycache__' in dirs:
                    click.secho('    * removing %s/__pycache__'
                                % os.path.abspath(subdir))
                    os.system("rm -rf %s/__pycache__" % root)
                    dirs.remove('__pycache__')
            except:
                click.secho('    Oops. A failure occurred cleaning %s' % root,
                            fg='red')
            finally:
                # Don't even bother traversing 'static' dirs:
                if 'static' in dirs:
                    dirs.remove('static')

    click.secho('\nAll done.', fg='green')
