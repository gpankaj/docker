from flask import render_template,request
from . import home
from form import FilePath

@home.route('/')
def index():
    import os
    all_envs = os.environ
    return render_template('home/index.html', all_envs=all_envs)


@home.route('/debug/', methods = ['GET', 'POST'])
def debug():
    import os
    import configparser
    file_name="/tmp/all_current_envs"
    form=FilePath()
    all_envs = {}
    all_lines=[]
    file_name = ""
    if form.validate_on_submit():
        file_name = request.form.get('file_name_with_path')
        try:
            with open(file_name) as f:
                for line in f:
                    all_lines.append("\n"+line+"\n\n")
            return render_template('home/index.html', all_envs={file_name: all_lines})
        except:
            return render_template('home/index.html', all_envs={file_name: "File Not found"})

    return render_template('home/debug.html',form=form)