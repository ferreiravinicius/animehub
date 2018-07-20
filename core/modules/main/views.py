from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

main = Blueprint('main', __name__)

@main.route('/')
def hello():
    """Render main page"""
    try:
        return render_template('home.html')
    except TemplateNotFound:
        abort(404)