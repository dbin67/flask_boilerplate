from flask import Blueprint

blueprint = Blueprint(
    'app1 blueprint',
    __name__,
    url_prefix='/app1'
)
