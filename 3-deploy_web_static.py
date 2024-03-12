#!/usr/bin/python3
"""Full Deployment includes pack and deployment"""
from fabric.api import env
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy

env.hosts = ['54.160.107.3', '52.3.245.179']
env.user = 'ubuntu'


def deploy():
    """Full Deployment calling do_pack and do_deploy"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    else:
        return do_deploy(archive_path)
