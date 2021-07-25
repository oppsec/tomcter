#!/usr/bin/env python3

from src.design.ui import banner, clear
from src.core.main import connect

from argparse import ArgumentParser


if __name__ == "__main__":
    clear()
    banner()

    parser = ArgumentParser()
    parser.add_argument('-l', help="Text file with targets to bruteforce", required=True)
    args = parser.parse_args()

    connect(args)