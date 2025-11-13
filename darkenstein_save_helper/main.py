import os
import sys
from pathlib import Path

import subprocess


LOCALAPPDATA = os.getenv("LOCALAPPDATA")
SAVE_DIR = Path(LOCALAPPDATA).joinpath("Rowye/Darkenstein3D")
GAME_REG_PATH = r"HKEY_CURRENT_USER\Software\Rowye\Darkenstein3D"

GAME_EXECUTABLE_NAME = "Darkenstein3D.exe"


def backup_save():
    SAVE_DIR.mkdir(parents=True, exist_ok=True)
    subprocess.run(["reg", "export", GAME_REG_PATH, str(SAVE_DIR.joinpath("darkenstein3d_save.reg")), "/y"], creationflags=subprocess.CREATE_NO_WINDOW)

def restore_save():
    reg_file = SAVE_DIR.joinpath("darkenstein3d_save.reg")

    if reg_file.exists():
        subprocess.run(["reg", "import", str(reg_file)], creationflags=subprocess.CREATE_NO_WINDOW)


def main():
    restore_save()
    subprocess.run([GAME_EXECUTABLE_NAME, *sys.argv[1:]])
    backup_save()


if __name__ == "__main__":
    main()
