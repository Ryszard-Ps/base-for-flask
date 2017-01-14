# -*- encoding: utf-8 -*-
from flask import Blueprint

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
    ''' Renders the App index page.
    :return:
    '''
    return "Welcome to the Flask App."
