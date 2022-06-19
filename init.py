import os
import subprocess as sp


def init(packwiz, pack_dir: str, modloader_version: str, version: str = "1.0.0", name: str = "My Modpack", author="Me!", mc_version="1.19", modloader="none"):
    """
    Initializes a modpack.

    Parameters:

    packwiz: PathBuf || str
    The packwiz executable.

    name: str = "My Modpack"
    The name of the modpack.

    author: str = "Me!"
    The author of the modpack.

    mc_version: str
    The Minecraft version of the modpack.

    modloader: str
    The modloader of the modpack. 
    Valid values are: "forge" || "liteloader" || "none" || "fabric" || "quilt"

    modloader_version: str
    The modloader version of the modpack.
    """
    print("Initializing pack")
    #os.system(f"{packwiz} init --name {name} --author {author} --mc-version {mc_version} --modloader {modloader} --{modloader}-version {modloader_version}")
    odir = os.getcwd()
    os.chdir(pack_dir)
    init = sp.run([packwiz, "init", "--version", version, "--name", name, "--author", author, "--mc-version",
                   mc_version, "--modloader", modloader, f"--{modloader}-version", modloader_version])
    os.chdir(odir)
    return init.returncode


def reinitialize(packwiz, pack_dir: str, name: str = "", author: str = "", mc_version: str = "", modloader: str = "", modloader_version: str = ""):
    """
    Reinitializes a modpack. This is useful if you want to change the name, author, or Minecraft version of the modpack.

    Parameters:

    packwiz: PathBuf || str
    The packwiz executable.

    name: str = "My Modpack"
    The name of the modpack.

    author: str = "Me!"
    The author of the modpack.

    mc_version: str
    The Minecraft version of the modpack.

    modloader: str
    The modloader of the modpack. 

    Valid values are: "forge" || "liteloader" || "none" || "fabric" || "quilt"
    """
    args = []
    name_bool = name != ""
    author_bool = author != ""
    mc_version_bool = mc_version != ""
    modloader_bool = modloader != ""
    if name_bool:
        args.append(f" --name {name}")
    if author_bool:
        args.append(f" --author {author}")
    if mc_version_bool:
        args.append(f" --mc-version {mc_version}")
    if modloader_bool:
        args.append(f" --modloader {modloader}")
    if name_bool == False and author_bool == False and mc_version_bool == False and modloader_bool == False:
        raise ValueError("No arguments to reinitialize with")
    #os.system(f"{packwiz} init -r{''.join(args)}")
    odir = os.getcwd()
    os.chdir(pack_dir)
    process = sp.run([packwiz, "init", "-r", *args])
    os.chdir(odir)
    return process.returncode
