# utils.py

import platform

def get_os():
    return platform.system().lower()  # 'windows', 'linux', 'darwin'