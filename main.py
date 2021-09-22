#!/usr/bin/env python3

from src.interface.ui import banner
from src.core.main import connect

from argparse import ArgumentParser


if __name__ == "__main__":
    banner()

    parser = ArgumentParser()
    parser.add_argument('-l', help="Specify the file containing the targets URLs", required=True)
    args = parser.parse_args()

    connect(args)