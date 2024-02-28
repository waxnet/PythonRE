from utilities import (
    cmd,
    io
)
import importlib.util
import requests
import msvcrt
import shutil
import sys
import os

# setup
cmd.execute(["title Empyrean Dumper", "cls"])
if not os.path.exists("tools"):
    os.makedirs("tools")

# get pyinstxtractor
pyinstxtractor_request = requests.get("https://raw.githubusercontent.com/extremecoders-re/pyinstxtractor/master/pyinstxtractor.py")
if not pyinstxtractor_request.ok:
    io.out("Could not download pyinstxtractor.\nPress any key to exit . . .")
    msvcrt.getch()
    exit()
with open("tools/pyinstxtractor.py", "w+") as file:
    file.write(pyinstxtractor_request.text)
    file.close()
pyinstxtractor = lambda executable_path: os.system(f"python3.10 tools/pyinstxtractor.py {executable_path} > nul")

# ask user for the executable file
executable_path = io.inp("Drag the executable file here and press enter")
extracted_path = (executable_path + "_extracted")

if os.path.exists(extracted_path):
    shutil.rmtree(extracted_path)

# decompile executable
io.out("\nDecompiling executable . . .")
pyinstxtractor(executable_path)

# dump config
found_config = False

for root, dirs, files in os.walk(extracted_path):
    found_config = ("config.pyc" in files)

    if found_config:
        spec = importlib.util.spec_from_file_location("config", os.path.join(root, "config.pyc"))
        module = importlib.util.module_from_spec(spec)

        sys.modules["config"] = module
        spec.loader.exec_module(module)

        io.out("\nDump")
        for key, value in module.__CONFIG__.items():
            io.out(f" - {key} : {value}")
        break

io.out()
if not found_config:
    io.out("The config file could not be found please use Python 3.10")
io.out("Press any key to exit . . .")
msvcrt.getch()
