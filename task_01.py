#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Get current date. """


import datetime

CURDATE = None


def get_current_date():
    """
    Returns the current date as a date object.
    """
    return datetime.date.today()

if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
