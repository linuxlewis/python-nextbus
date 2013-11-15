"""Tests for nextbus"""
import nextbus
from nextbus.model import Agency, Route

import unittest

def test_agencyList():
    #agency list should always return a list of agencies
    agencies = nextbus.agency_list()
    assert len(agencies) > 0 and type(agencies[0]) == Agency

def test_routeList():
    #route list should always return a list of routes filtered by agency.
    routes = nextbus.route_list(agency='sf-muni')
    assert len(routes) > 0 and type(routes[0]) == Route and routes[0].title == 'F-Market & Wharves'

def test_routeConfig():
    #route config should return a route object by the given route tag
    route = nextbus.route_config(agency='sf-muni', route='1')
    assert route and type(route) == Route and route.title == '1-California'


