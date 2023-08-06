# -*- coding: utf-8 -*-

"""
This module contains the set of Ndic' exceptions.

"""
from __future__ import absolute_import

from ndic.constants import CONNECTION_ERROR_MESSAGE


class NdicConnectionError(Exception):
    """
    Exception raised when network is unconnected
    """

    def __init__(self):
        pass

    def __str__(self):
        return CONNECTION_ERROR_MESSAGE

    def __repr__(self):
        return CONNECTION_ERROR_MESSAGE
