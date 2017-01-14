# -*- encoding: utf-8 -*-
from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/', methods=['GET'])
def index():
    ''' Renders the API index page.
    :return:
    '''
    return "Welcome to the API."
