import sys
from cx_Freeze import setup, Executable
exe = Executable(
    script=r"game.py",
    base="Win32GUI",
    )

setup(
    name="SnakeGame",
    version="0.1",
    description="My first python program. A snake game that I made without watching tutorials \
    or looking up code, using only pygame documentation.",
    executables=[exe]
    )