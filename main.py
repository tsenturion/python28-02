import sys

if sys.platform == "win32":
    print("Программа запущена в Windows")
elif sys.platform == "linux":
    print("Программа запущена в Linux")
elif sys.platform == "darwin":
    print("Программа запущена в macOS")