### <p align= "center">Blank Obfuscator Runtime Dumper</p>

This is a <a href="https://github.com/Blank-c/BlankOBF">Blank Obfuscator</a> dumper that works by <a href="https://www.geeksforgeeks.org/monkey-patching-in-python-dynamic-behavior">monkey patching</a> the builtin exec function, by doing this, 
each time exec is invoked, we can analyze the arguments passed to it and decompile the code object that
it should execute, since <a href="https://github.com/Blank-c/BlankOBF">Blank Obfuscator</a> has 2 layers of protection we can just allow exec to be invoked
twice and get the disassembled version of the final code without executing the payload.
