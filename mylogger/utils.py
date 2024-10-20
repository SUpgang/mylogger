""" Basic helper functions """

import os


def check_and_create_directory(path: str):
    """Checks if a directory exists otherwise creates it"""
    if not os.path.exists(path):
        os.makedirs(path)
