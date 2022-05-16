from flask import Blueprint, render_template, request
from uuid import uuid4

home = Blueprint('home', __name__)


@home.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', mess=uuid4())
