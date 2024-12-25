#!/usr/bin/env python3
import subprocess

commands = input('Type the shell command: ')
args: list[str] = commands.split()

for arg in args:
    if 'rm' in arg:
        print('rm command is not allowed for security reasons.')
        exit()

subprocess.run(args)