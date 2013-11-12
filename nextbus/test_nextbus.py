"""Tests for nextbus"""

import nextbus

import unittest

def text_agencyList():
    #agency list should always return a list of agencies
    r = nextbus.agency_list()

    assert len(r) > 0