import platform

class Runner():
    def is_windows():
        # Windows is used for UI design & basic testing
        # This can also be seen as "is test mode on"
        return platform.system() == "Windows"
    def is_linux():
        return platform.system() == "Linux"