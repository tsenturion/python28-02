import os
import platform
import sys
from pathlib import Path

print("Операционная система:", platform.system())
print("Идентификатор платформы:", sys.platform)
print("Тип ОС:", os.name)
print("Интерпретатор:", sys.executable)
print("Рабочий каталог:", Path.cwd())
print("Домашний каталог:", Path.home())
print("Разделитель пути:", os.sep)
print("Разделитель PATH:", os.pathsep)