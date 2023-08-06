#!/usr/bin/env python
# -*- coding: utf-8 -*-
from subprocess import CalledProcessError, check_output, call

import pip
from lztools.text import regex
from lztools.TempPath import TempPath

def extract_module_version(text):
    return regex(" \d+\.\d+\.\d+", text, only_first=True)[1:]

def set_version(original, new):
    new = check_output(["cat", "setup.py"]).decode("utf8").replace(original, new)
    with open("setup.py", "w") as f:
        f.write(new)

def add_versions(left, right):
    l1, l2, l3 = left.split(".")
    r1, r2, r3 = right.split(".")
    e1, e2, e3 = int(l1) + int(r1), int(l2) + int(r2), int(l3) + int(r3),
    return f"{e1}.{e2}.{e3}"

def clean():
    call(["rm", "-rf", "build"])
    call(["rm", "-rf", "dist"])
    call(["rm", "-rf", "*.egg-info"])

def local_install(path, upload=False, add_to_version=None):
    with TempPath(path):
        clean()
        if add_to_version is not None:
            ov = get_version()
            nv = add_versions(ov, add_to_version)
            set_version(ov, nv)
        call(["python3.7", "setup.py", "install"])
        clean()
        if upload:
            call(["python3.7", "setup.py", "install", "sdist", "bdist_wheel"])
            try:
                _upload()
            except:
                raise
            finally:
                clean()

def get_name_from_path():
    _, end = check_output(["cat", "setup.py"]).decode("utf8").split("name='", 1)
    name, _ = end.split("'", 1)
    return name

def _upload():
    online = get_version_online(get_name_from_path())
    local = get_version()
    if online == local:
        raise Exception("Error: Same version as online")
    else:
        call(["twine", "upload", "-u", "zanzes", "dist/*"])

def get_version_online(name):
    try:
        out = check_output(["python3.7", "-m", "pip", "search", "-V", "--no-cache-dir", name]).decode("utf8")
        _, end = out.split(f"{name} (", 1)
        version, _ = end.split(")", 1)
        return version
    except CalledProcessError:
        return "-999"

def get_version():
    return check_output(["python3.7", "setup.py", "-V"]).decode("utf8").rstrip("\n")

def pip_install(package):
    pip.main(['install', package])



