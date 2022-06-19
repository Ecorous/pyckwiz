import init
import curseforge
import modrinth
import utils
import os

"""
This is a test script for pyckwiz. It tests the following:
    - Initialization of a packwiz pack
    - Installation of a mod from curseforge to a packwiz pack
    - Exporting a packwiz pack to a curseforge zip file
    - Installation of a mod from modrinth to a packwiz pack
    - Exporting a packwiz pack to a modrinth mrpack file
    - Updating a singular mod
    - Updating all mods
"""

if not os.path.isdir("pack_test"):
    os.mkdir("pack_test")
root = os.getcwd()
packwiz = "packwiz" # Path to packwiz executable. In this case, it's reading from path.
os.chdir("pack_test")
files = os.listdir()
for file in files:
    if os.path.isfile(file):
        os.remove(file)
    elif os.path.isdir(file):
        os.rmdir(file)
os.chdir(root)

init_process = init.init(packwiz=packwiz, version="1.0.0", name="My Modpack", author="Me!",
          mc_version="1.18.2", modloader="fabric", modloader_version="0.11.7", pack_dir=f"{root}/pack_test")
if init_process != 0:
    raise Exception("Failed to initialize pack")
cf_install_process = curseforge.install(
    "https://www.curseforge.com/minecraft/mc-mods/controlling/files/3757589", packwiz, f"{root}/pack_test")
if cf_install_process != 0:
    raise Exception("Failed to install mod from curseforge.")

cf_export_process = curseforge.export(packwiz, "pack_test", f"{root}/pack_test/pack_test.zip")
modrinth.install("https://modrinth.com/mod/fabric-api/version/pT09syaU", packwiz, f"{root}/pack_test")
modrinth.export(packwiz, f"{root}/pack_test", f"{root}/pack_test.mrpack")
utils.update(packwiz, f"{root}/pack_test", f"controlling")
print("Pack test nearly complete. ")
utils.update_all(packwiz, f"{root}/pack_test")
