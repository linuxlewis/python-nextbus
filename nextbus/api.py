"""module to handle making api calls to nextbus."""

import requests

from lxml import etree

from .model import parse_command, NextBusAPIError

API_URL = 'http://webservices.nextbus.com/service/publicXMLFeed'
DEFAULTS = {}

def agency_list():
    """returns the list of agency objects"""
    result = __api_call('agencyList') or []
    return result

def route_list(agency=None, **kwargs):
    """returns the list of route objects"""
    result = __api_call('routeList', agency=agency, **kwargs) or []
    return result

def route_config(agency=None, route=None, **kwargs):
    """ takes agency string, route name, and additional api params
    returns list of route objects"""
    result = __api_call('routeConfig', agency=agency, route=route, **kwargs) or []
    return result

def predictions(agency=None, route=None, stop_id=None, **kwargs):
    """prediction"""
    result = __api_call('predictions', agency=agency, route=route, stop_id=stop_id, **kwargs) or []
    return result

def set_defaults(defaults):
    """sets the default parameters"""
    DEFAULTS = __parse_params(defaults)

def __api_call(command, **kwargs):
    """internal method to call nextbus API"""
    #set the command
    kwargs['command'] = command

    #parse the kwargs
    kwargs = __parse_params(kwargs)

    #set the defaults
    params = dict(kwargs, **DEFAULTS)

    #set request headers, gzip according to API guidelines
    headers = {'Accept-Encoding' : 'gzip, deflate'}

    #http
    r = requests.get(API_URL, params=params, headers=headers)

    #parse xml
    x = etree.fromstring(r.content)

    #check for errors
    errors = x.xpath('//Error/text()')

    #raise error for bad API call
    if len(errors) > 0:
        raise NextBusAPIError(errors[0])

    #xml to models
    if x is not None:
        result = parse_command(command, x)
    else:
        result = None

    return result

def __parse_params(params):
    """parses params from methods into API format. returns new dictionary.
    other params are ignored"""

    parsed_params = {}

    for key in params.keys():

        if key == 'agency':
            parsed_params['a'] = params[key]
        elif key == 'route':
            parsed_params['r'] = params[key]
        else:
            parsed_params[key] = params[key]

    return parsed_params










