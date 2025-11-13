darkenstein_save_helper
=========================

This program is workaround for implementing Steam Cloud Save in Darkenstein 3D.

Due to Darkenstein 3D using Unity native saving(which stores vaules on registry), it's hard to implement Steam Cloud Save.

This program does:

1. Restore registry from `%LocalAppData%/Rowye/Darkenstein3D/darkenstein3d_save.reg` into `HKEY_CURRENT_USER\Software\Rowye\Darkenstein3D`
2. Launch `Darkenstein3D.exe` and wait it for closing
3. Backup registry `HKEY_CURRENT_USER\Software\Rowye\Darkenstein3D` into `%LocalAppData%/Rowye/Darkenstein3D/darkenstein3d_save.reg`.


So all you need for Steam Cloud:

* Include this helper to game and set as main executable of the game.
* Backup/Restore `%LocalAppData%/Rowye/Darkenstein3D/darkenstein3d_save.reg` with Steam Cloud.


# Download

[Download latest version](https://github.com/iAmGhost/darkenstein_save_helper/releases/latest)


# How to build

This project uses [uv](https://docs.astral.sh/uv/) as package manager.

Install uv to your environment and run:


```cmd
uv run build_exe
```

Will create single executable in dist/ folder.
