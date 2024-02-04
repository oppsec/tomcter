#!/usr/bin/env python3

from src.interface.ui import get_banner
from src.core.bruteforce import connect

from argparse import ArgumentParser

if __name__ == "__main__":
    get_banner()

    parser = ArgumentParser()
    parser.add_argument('-u', help="Specify the target URL")
    parser.add_argument('-l', help="Specify the file containing the targets URLs")
    args = parser.parse_args()

    connect(args)