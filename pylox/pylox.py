#!/usr/bin/env python3
import sys


def error(line, msg):
    print('[line {}] ERROR: {}: {}'.format(line, '', msg))


def run(src: str):
    print(src)


def run_prompt():
    while True:
        print('> ', flush=True)
        line = sys.stdin.readline()
        run(line)


def run_file(path: str):
    print(path)


if __name__ == '__main__':
    if len(sys.argv) > 2:
        print('Usage: pylox [script]')
        sys.exit(-1)
    elif len(sys.argv) == 2:
        run_file(sys.argv[1])
    else:
        run_prompt()
