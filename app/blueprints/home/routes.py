from flask import render_template
from . import home
import paramiko

@home.route('/')
def index():
    return render_template('home/index.html')