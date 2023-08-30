from flask import Blueprint

blueprint = Blueprint(
    'app2 blueprint',
    __name__,
    url_prefix='/app2'
)
