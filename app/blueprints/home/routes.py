from flask import render_template
from . import home

@home.route('/')
def index():
    import os
    all_envs = os.environ
    return render_template('home/index.html', all_envs=all_envs)

@home.route('/debug')
def index():
    import os
    import configparser
    all_envs={}
    with open('/tmp/all_vars') as f:
        for line in f:
            values = line.split('=')
            all_envs[values[0]] = values[1]
    return render_template('home/index.html', all_envs=all_envs)