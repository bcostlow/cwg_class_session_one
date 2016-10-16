import logging
import sys

from examplepack.modtwo import return_something

logger = logging.getLogger(__name__) # name will be 'examplepack.modeone.modthree'

_private_data = ""

def get_data():
    return _private_data

def set_data(data):
    global _private_data
    _private_data = data

def log_something():
    logger.info("write to the log")

def main():
    try:
        print("I only fire if this was run from command line")
        return 0
    except:
        return 1


if __name__ == "__main__":
    sys.exit(main())