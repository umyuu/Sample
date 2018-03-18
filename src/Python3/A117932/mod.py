# -*- coding: utf-8 -*-
import traceback
import re
import sys


def executable_path() -> None:
    print(sys.argv[0])


def hogehoge() -> None:
    """
    stack trace frame -> call script file name
    """
    for line in traceback.format_stack(limit=2):
        m = re.match('\s*File\s"(.*)"', line)
        assert m is not None
        print(m.group(1))
        return


def main():
    # hogehoge()
    executable_path()


if __name__ == "__main__":
    main()
