from utilities import data

import dis
import io

import builtins

exec_original = builtins.exec
def exec_patch(*args, **kwargs):
    first_exec_argument = str(args[0])
    
    # check if exec argument needs to be disassembled
    if "<string>" not in first_exec_argument:
        return exec_original(*args, **kwargs)

    # capture disassembly output
    output = io.StringIO()
    dis.dis(args[0], file=output)
    disassembly_output = output.getvalue()

    # write disassembly output to file
    if data.dumps == 0:
        with open(f"{data.output_folder}/stage-2-dump.txt", "w+") as file:
            file.write(disassembly_output)
            file.close()
    
    # check cycles
    data.dumps += 1
    if data.dumps != 2:
        return exec_original(*args, **kwargs)
    
    # dump last exec
    with open(f"{data.output_folder}/final-dump.txt", "w+") as file:
        file.write(disassembly_output)
        file.close()
builtins.exec = exec_patch
