from flask import render_template
from . import home

@home.route('/')
def index():
    import os
    all_envs = os.environ
    return render_template('home/index.html', all_envs=all_envs)


@home.route('/debug/<string:file_name>', methods = ['GET', 'POST'])
def debug(file_name):
    import os
    import configparser
    all_envs={}
    with open(file_name) as f:
        for line in f:
            values = line.split('=')
            all_envs[values[0]] = values[1]
    return render_template('home/index.html', all_envs=all_envs)