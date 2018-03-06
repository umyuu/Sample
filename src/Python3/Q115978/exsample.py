# -*- coding: utf-8 -*-
from logging import getLogger, FileHandler, DEBUG
import random


class LFFileHandler(FileHandler):
    def _open(self):
        return open(self.baseFilename, self.mode, encoding=self.encoding, newline=self.terminator)


def main():
    logger = getLogger(__name__)
    handler = LFFileHandler('test.log')
    handler.setLevel(DEBUG)
    logger.addHandler(handler)
    logger.setLevel(DEBUG)
    logger.info(str(random.randint(0, 1000)))


if __name__ == "__main__":
    main()
