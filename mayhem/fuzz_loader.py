#!/usr/bin/env python3
from ctypes import ArgumentError

import atheris
import io
import sys

from pefile import PEFormatError
from unicorn import UcError

with atheris.instrument_imports():
    import speakeasy
    import speakeasy.errors


@atheris.instrument_func
def TestOneInput(data):
    try:
        se = speakeasy.Speakeasy()
        se.load_module(data=data)
        se.get_report()
    except (speakeasy.errors.SpeakeasyError, PEFormatError, UcError, ArgumentError):
        return -1
    except AttributeError:
        return -1
    except ValueError as e:
        if 'architecture' not in str(e):
            raise


def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == '__main__':
    main()
