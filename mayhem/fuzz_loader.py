#!/usr/bin/env python3
import atheris
import io
import sys

with atheris.instrument_imports():
    import speakeasy
    import speakeasy.errors

@atheris.instrument_func
def TestOneInput(data):
    try:
        se = speakeasy.Speakeasy()
        module = se.load_module(data=data)
        # se.run_module(module)
        se.get_report()
    except speakeasy.errors.SpeakeasyError:
        return -1

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == '__main__':
    main()
