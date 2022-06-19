import os
import subprocess as sp
from subprocess import Popen, PIPE, STDOUT
from sys import stdout

def refresh(packwiz, dir: str):
    """
    Refresh index.toml
    """
    odir = os.getcwd()
    os.chdir(dir)
    process = sp.run([packwiz, "refresh"])
    os.chdir(odir)
    return process.returncode

def update(packwiz, dir: str, mod: str):
    """
    Updates a mod.
    """
    odir = os.getcwd()
    os.chdir(dir)
    process = sp.run([packwiz, "update", mod])
    os.chdir(odir)
    return process.returncode

def update_all(packwiz, dir: str):
    """
    Updates all mods in the pack.
    """
    odir = os.getcwd()
    os.chdir(dir)
    process = sp.Popen([packwiz, "update", "-a"], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    stdout_data = process.communicate(input=b'y\n')[0]
    stdout_data = stdout_data.decode("utf-8")
    stdout_data = stdout_data.split("\n")
    for line in stdout_data:
        if line.startswith("Do you want to update?"):
            line_split = line.split(": ")[1]
            print(line_split)
        else:
            print(line)
    #print(stdout_data)
    os.chdir(odir)
    return process.returncode
