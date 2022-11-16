#!/usr/bin/env python3
import atheris
import io
import sys

from pefile import PEFormatError

with atheris.instrument_imports():
    import speakeasy
    import speakeasy.errors


@atheris.instrument_func
def TestOneInput(data):
    try:
        se = speakeasy.Speakeasy()
        module = se.load_module(data=data)
        del module
        del se
    except (speakeasy.errors.SpeakeasyError, PEFormatError):
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
