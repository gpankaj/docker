from flask import render_template
from . import home
import paramiko

@home.route('/')
def index():
    import os
    all_envs = os.environ
    return render_template('home/index.html', all_envs=all_envs)