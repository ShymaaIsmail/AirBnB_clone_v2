#!/usr/bin/python3
""" Delete unused old versions of deployed packages"""
from fabric.api import local, run, env


env.hosts = ['54.160.107.3', '52.3.245.179']
env.user = "ubuntu"


def do_clean(number=0):
    """ clean old versions """
    number = int(number)
    if number < 2:
        number = 1
    else:
        number += 1
    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
