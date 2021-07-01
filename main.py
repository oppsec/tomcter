#!/usr/bin/env python3

from src.design.ui import get_banner, clear
from src.core.main import connect

def main() -> None:
    clear()
    get_banner()
    connect()


if __name__ == "__main__":
    main()