"""Launch the preserved shell tools from their installed data directory."""
import os
from pathlib import Path
import shutil
import sys
import sysconfig

COMMANDS = ['checkforce', 'data-converge', 'data-converge-magnetic', 'dfpt-data-converge', 'generate-converge', 'kgs_gen_kpts', 'nbands-epsopt-data-converge', 'nbands-generate-converge']
PREFIX = 'vaspup2'
DATA_DIR = 'vaspup2'

def main():
    command = Path(sys.argv[0]).name
    args = sys.argv[1:]
    if command == PREFIX:
        if not args or args[0] in ("-h", "--help"):
            print("Usage: " + PREFIX + " <command> [arguments]")
            print("Commands: " + ", ".join(COMMANDS))
            return 0
        command, args = args[0], args[1:]
    elif command.startswith(PREFIX + "-"):
        command = command[len(PREFIX) + 1:]
    if command not in COMMANDS:
        print("Unknown command: " + command, file=sys.stderr)
        return 2
    script = Path(sysconfig.get_path("data")) / "share" / DATA_DIR / "bin" / command
    interpreter = "perl" if command == "checkforce" else "bash"
    executable = shutil.which(interpreter)
    if not executable:
        print("Required executable is missing: " + interpreter, file=sys.stderr)
        return 127
    options = ["-w"] if interpreter == "perl" else []
    os.execv(executable, [executable, *options, str(script), *args])
