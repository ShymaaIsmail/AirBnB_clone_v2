#!/usr/bin/python3
"""
Packing the web static folder in a tgz
compressed file
"""
from datetime import datetime
from fabric.api import local
from os.path import isdir


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


if __name__ == "__main__":
    do_pack()
