#!/usr/bin/python3
"""Full Deployment includes pack and deployment"""
from fabric.api import  put, run, local, env
from datetime import datetime
from os.path import isdir, exists

env.hosts = ['54.160.107.3', '52.3.245.179']
env.user = 'ubuntu'


def do_pack():
    """Packs content of web static folder into tgz archive
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        return None


def do_deploy(archive_path):
    """Connect to remote server and push the archive file"""
    if not exists(archive_path):
        return False
    else:
        try:
            file_n = archive_path.split("/")[-1]
            no_ext = file_n.split(".")[0]
            path = "/data/web_static/releases/"
            put(archive_path, '/tmp/')
            run('mkdir -p {}{}/'.format(path, no_ext))
            run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
            run('rm /tmp/{}'.format(file_n))
            run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
            run('rm -rf {}{}/web_static'.format(path, no_ext))
            run('rm -rf /data/web_static/current')
            run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
            return True
        except Exception as e:
            raise e


def deploy():
    """Full Deployment calling do_pack and do_deploy"""
    archive_path = do_pack()
    if not archive_path:
        return False
    else:
        return do_deploy(archive_path)
