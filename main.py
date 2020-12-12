#!/usr/bin python3
from equations import Equations


def main():
    obj = Equations()
    while obj.runloop:
        obj.loop()


if __name__ == "__main__":
    main()
