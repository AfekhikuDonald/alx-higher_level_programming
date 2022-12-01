#!/usr/bin/python3

if __name__ == "__main__":
    import logging

    logging.basicConfig(format='%(message)s')
    log = logging.getLogger(__name__)
    log.warning("#pythoniscool")
