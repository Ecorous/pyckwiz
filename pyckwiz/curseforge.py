import os
import subprocess as sp


def install(mod_name: str, packwiz, dir: str):
    """
    Installs a mod to the specified modpack.
    """
    print(f"Installing {mod_name}")
    odir = os.getcwd()
    os.chdir(dir)
    process = sp.run([packwiz, "cf", "install", mod_name])
    os.chdir(odir)
    return process.returncode

def export(packwiz, pack_dir: str, export_dir: str):
    """
    Exports the modpack to the specified directory.

    export_dir: str
    The directory to export the modpack to. "/output.zip" is appended to the provided directory.
    """
    print("Exporting pack")
    odir = os.getcwd()
    os.chdir(pack_dir)
    process = sp.run([packwiz, "cf", "export", "-o", f"{export_dir}/output.zip"])
    os.chdir(odir)
    return process.returncode
    