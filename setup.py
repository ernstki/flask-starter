from setuptools import setup

with open('requirements.txt', 'r') as f:
    requires=[line for line in f.read().split("\n")
              if line and not line.startswith('#')]

setup(
    name='Flask-Starter',
    version='0.0.1',
    packages=[
        'flask_starter',
    ],
    install_requires=requires,
    entry_points='''
        [console_scripts]
        starter=flask_starter.cli:main
        # Also interesting:
        # [flask.command]
    ''',
)
