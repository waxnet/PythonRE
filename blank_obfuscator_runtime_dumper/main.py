from utilities import (
    cmd,
    io
)
import os

# setup
cmd.execute(["title Blank Obfuscator Runtime Dumper", "cls"])
if not os.path.exists(".output"):
    os.makedirs(".output")

# ask for the obfuscated script path
script_path = io.inp("Drag the obfuscated script here and press enter")

# dump
io.out("\nCheck the output folder once this script exits.\n\nDumping script . . .")

with open("utilities/dumper.py", "r") as file:
    dumper_code = file.read()
    file.close()
with open(script_path, "r") as file:
    script_code = file.read()
    file.close()
exec(f"{dumper_code}\n{script_code}")
