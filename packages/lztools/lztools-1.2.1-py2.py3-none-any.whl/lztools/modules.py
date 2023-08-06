#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess
from subprocess import CalledProcessError

import pip

from lztools.text import regex
from lztools.TempPath import TempPath

def extract_module_version(text):
    return regex(" \d+\.\d+\.\d+", text, only_first=True)[1:]

def local_install(path, upload=False):
    _install(path, upload)

def get_name_from_path():
    _, end = subprocess.check_output(["cat", "setup.py"]).decode("utf8").split("name='", 1)
    name, _ = end.split("'", 1)
    return name

def _upload():
    online = get_version_online(get_name_from_path())
    local = get_version()
    if online == local:
        raise Exception("Error: Same version as online")
    else:
        subprocess.call(["twine", "upload", "dist/*"])

def _install(path, upload):
    e = None
    with TempPath(path) as rp:
        subprocess.call(["rm", "-rf", "dist"])
        subprocess.call(["python3.7", "setup.py", "install"])

        subprocess.call(["rm", "-rf", "build"])
        subprocess.call(["rm", "-rf", "dist"])
        subprocess.call(["rm", "-rf", "*.egg-info"])
        if upload:
            subprocess.call(["python3.7", "setup.py", "install", "sdist", "bdist_wheel"])
            try:
                _upload()
            except:
                raise
            finally:
                subprocess.call(["rm", "-rf", "build"])
                subprocess.call(["rm", "-rf", "dist"])
                subprocess.call(["rm", "-rf", "*.egg-info"])

def get_version_online(name):
    try:
        out = subprocess.check_output(["python3.7", "-m", "pip", "search", "-V", "--no-cache-dir", name]).decode("utf8")
        _, end = out.split(f"{name} (", 1)
        version, _ = end.split(")", 1)
        return version
    except CalledProcessError:
        return "-999"


def get_version():
    return subprocess.check_output(["python", "setup.py", "-V"]).decode("utf8").rstrip("\n")

def pip_install(package):
    pip.main(['install', package])



