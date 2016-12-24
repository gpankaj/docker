from flask import render_template
from . import dsystem


@dsystem.route('/dsystem',methods=['GET', 'POST'])
def index():
    pass