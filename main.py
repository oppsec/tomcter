#!/usr/bin/env python3

from src.interface.ui import banner
from src.core.multiple import connect
from src.core.single import single_connect

from argparse import ArgumentParser


if __name__ == "__main__":
    banner()

    parser = ArgumentParser()
    parser.add_argument('-u', help="Specify the target URL")
    parser.add_argument('-l', help="Specify the file containing the targets URLs")
    args = parser.parse_args()

    if (args.l):
        connect(args)
    elif (args.u):
        single_connect(args)