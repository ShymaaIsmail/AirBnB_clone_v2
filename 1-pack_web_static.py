#!/usr/bin/python3
"""
    Packing the web static folder in a tgz compressed file
"""
from fabric import task
from fabric.operations import local
from datetime import datetime
import os

def do_pack():
    """Packs content of web static folder into tgz archive"""
    archive_path = None
    src_folder = "webstatic"
    dest_folder = "versions"
    now = datetime.now()	
    time_stamp = f"{now.year}{now.month}{now.day}{now.hour} \
                    {now.minute}{now.second}"
    tar_file_name = f"web_static_{time_stamp}.tgz"
    archive_path = os.path.join(dest_folder, tar_file_name)
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    try:
        local(f'tar -czf {tar_file_name}.tgz {src_folder}')
        return archive_path
    except Exception as e:
        return None
