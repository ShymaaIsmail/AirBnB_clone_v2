#!/usr/bin/python3
"""Packing the web static"""
from fabric import task
from fabric.operations import local
from datetime import datetime
import os

@task
def do_pack(c):
    """Packs content of web static folder into tgz archive"""
    archive_path = None
    dest_folder = "versions"
    now = datetime.now()
    time_stamp = f"{now.year}{now.month}{now.day}{now.hour} \
                    {now.minute}{now.second}"
    tar_file_name = f"web_static_{time_stamp}.tgz"
    archive_path = os.path.join(dest_folder, tar_file_name)
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    try:
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception as e:
        return None
