#! /usr/bin/env python


"""Router"""


from __future__ import print_function

import os
import sys


from circuits import Component


class Router(Component):

    name = "router"
    version = "0.0.1"


def main():
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)

    args = iter(sys.argv)
    next(args)

    Router().run()


if __name__ == "__main__":
    main()
