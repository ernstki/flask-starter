import os

class Config(object):
    DEBUG=True,
    TEMPLATES_AUTO_RELOAD=True,
    EXPLAIN_TEMPLATE_LOADING=True,
    PROJECT_ROOT=os.path.abspath(os.path.dirname(__file__))
