#!/usr/bin/python3
"""Full Deployment includes pack and deployment"""
from fabric.api import env, task, local
from os.path import exists
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy
archive_path = do_pack()


env.hosts = ['54.160.107.3', '52.3.245.179']
env.user = 'ubuntu'


def local_deploy(archive_path):
    """Connect to local host and push the archive file"""
    if not exists(archive_path):
        return False
    else:
        try:
            file_n = archive_path.split("/")[-1]
            no_ext = file_n.split(".")[0]
            path = "/data/web_static/releases/"
            # For localhost, use local() instead of put()
            local('mkdir -p {}{}/'.format(path, no_ext))
            local('tar -xzf {} -C {}{}/'.format(archive_path, path, no_ext))
            local('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
            local('rm -rf {}{}/web_static'.format(path, no_ext))
            local('rm -rf /data/web_static/current')
            local('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
            return True
        except Exception as e:
            raise e


@task
def deploy():
    """Full Deployment calling do_pack and do_deploy"""
    if archive_path is None:
        return False
    else:
        return do_deploy(archive_path)
