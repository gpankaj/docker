from flask import render_template
from . import dsystem
import paramiko
from sshtail import SSHTailer, load_rsa_key
import socket
import traceback2
import sys
from form import LoginInfoForm

@dsystem.route('/dsystem',methods=['GET', 'POST'])
def index():
    form = LoginInfoForm()
    hostname = '192.168.88.128'
    port = 22
    username = "gpankaj"

    if form.validate_on_submit():
        hostname = form.hostname.data
        password = form.password.data
        label = form.label.data
        save = form.save.data

        print "Hostname: " + hostname + " password " + password + " label " + label + " save " + str(save)

    return render_template('dsystem/index.html', form=form)

@dsystem.route('/tail')
def ssh_tail():
    tailer = SSHTailer('192.168.88.134', '/var/log/syslog', private_key=load_rsa_key(r'c:/Users/pankajg/Desktop/flask/supercloud1/app/private_key'))

    for host, filename, line in tailer.tail():
        print "%s:%s - %s" % (host, filename, line)