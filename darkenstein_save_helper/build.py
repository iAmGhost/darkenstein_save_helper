import PyInstaller.__main__


def build():
    PyInstaller.__main__.run([
        'darkenstein_save_helper/main.py',
        '--name=darkenstein_save_helper',
        '--onefile',
        '--icon=darkenstein_save_helper/darkenstein.ico',
        '--noconsole',
    ])


if __name__ == "__main__":
    build()
