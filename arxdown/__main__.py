#!/usr/bin/env python3

"""
Simple tool to download files from arXiv, and arrange them in appropriate folders.

When no specific name or path is specified, it will create (if it does not already exist) a folder
with the primary subject name of the paper, and name the file accordingly.
"""


import argparse
from arxdown import meta
from typing import Any
from arxdown import Extractor


def main() -> None:
    parser = argparse.ArgumentParser(prog=meta.name, description=meta.description)

    parser.add_argument(
        "-p",
        "--path",
        action="store",
        type=str,
        dest="path",
        default=None,
        help="extract files to the given path (default: creates a folder).",
    )

    parser.add_argument(
        "-n",
        "--name",
        action="store",
        type=str,
        dest="name",
        default=None,
        help="Give the name to the downloaded file"
    )

    parser.add_argument(
        "ref",
        metavar="REFNAME",
        type=float,
        help="The encoding of the arXiv paper to download",
        nargs="+"
    )

    args = parser.parse_args()
    p = Extractor(ref=args.ref[0], path=args.path, name=args.name)
    p.extract()


if __name__ == "__main__":
    main()