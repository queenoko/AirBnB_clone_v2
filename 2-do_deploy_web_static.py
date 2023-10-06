#!/usr/bin/python3
"""
This script will deploy archive to the web servers
"""
from fabric.api import *
from fabric.decorators import task
import os
from datetime import datetime


#env.hosts = ['34.207.156.213', '54.237.20.30']
env.hosts= ["964ffa937b2a.d1ee86f7.alx-cod.online"]


@task
def do_deploy(archive_path):
    """This code deploy an archived to servers"""
    try:
        if os.path.exists(archive_path):
            file_name = archive_path.split(".")[0]
            ext = archive_path.split(".")[1]
            file_name = file_name.split("/")[-1]
            put(archive_path, "/tmp/")
            dst = "/data/web_static/releases/{}".format(file_name)
            run("mkdir -p " + dst + "/")
            run("tar -xzf /tmp/{}.{} -C {}/".format(file_name, ext, dst))
            run("rm /tmp/{}.{}".formart(file_name, ext))
            run("mv {}/web_static/* {}/".format(dst, dst))
            run("rm -rf {}/web_static".format(dst))
            run("ln -rf {}.{} /data/web_static/current".format(dst, ext))
            return True
        else:
            return False
    except Exception:
        return False


@task
def do_pack():
    """Archive 'web_static' dir"""
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    arc_name = "web_static_{}.tgz".format(time)

    if local("tar -cvzf versions/{} web_static".format(arc_name)).succeeded:
        return "versions/{}".format(arc_name)
    return None
