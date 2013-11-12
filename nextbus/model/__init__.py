from lxml import etree

def parse_command(command, xml):
    """parses the xml document based on the command used. returns the object structure
    associated with that xml"""
    result = None
    if command == 'agencyList':
        result = __parse_agencyList(xml)
    elif command == 'routeList':
        result = __parse_routeList(xml)
    elif command == 'routeConfig':
        result = __parse_routeConfig(xml)

    return result

def __parse_agencyList(xml):
    """takes in an nextbus xml element and returns a list of agency objects."""

    #get the list of agencies
    agencies = xml.xpath('//agency')

    agencies = map(lambda x: Agency.from_element(x), agencies)

    return agencies

def __parse_routeList(xml):
    """takes in an nextbus xml element and returns a list of route objects."""

    #get the list of routes
    routes = xml.xpath('//route')

    routes = map(lambda x: Route.from_element(x), routes)

    return routes

def __parse_routeConfig(xml):
    """takes in nextbus xml element and returns a route object with stops"""
    #get the route
    routes = xml.xpath('//route')

    result = None
    if len(routes) > 0:
        result = Route.from_element(routes[0])

    return result

class Model(object):

    @classmethod
    def from_element(cls, element):
        """creates an object from element"""

        model = cls()
        model.hydrate(element)

        return model

    def hydrate(self, element):
        """given an element, this method sets the value of the model object"""
        raise NotImplementedError()

class APIError(Exception):
    """error class to describe errors from the API"""
    def __repr__(self):
        return 'NextBusAPIError()'

class Agency(Model):
    """model object to represent the 'Agency' """

    def __init__(self):
        self.tag = None
        self.title = None
        self.region_title = None

    def __repr__(self):
        return 'Agency(%s)' % self.title

    def hydrate(self, element):
        self.tag = element.get('tag')
        self.title = element.get('title')
        self.region_title = element.get('regionTitle')

class Direction(Model):
    """model object to represent the 'Direction'"""
    def __init__(self):
        self.tag = None
        self.title = None
        self.name = None
        self.use_for_ui = False
        self.stops = []

    def __repr__(self):
        return 'Direction(%s)' % self.title

    def hydrate(self, element):
        self.tag = element.get('tag')
        self.title = element.get('title')
        self.name = element.get('name')
        self.use_for_ui = element.get('useForUI') == 'true'

        #get the stops
        stops = element.xpath('stop')

        stps = []
        for s in stops:
            stps.append(Stop.from_element(s))

        self.stops = stps

class Path(Model):
    """model object to represent the 'Path' """

    def __init__(self):
        self.points = []

    def __repr__(self):
        return 'Path()'

    def hydrate(self, element):

        points = element.xpath('//point')

        pts = []
        for p in points:
            pts.append(Point.from_element(p))

        self.points = pts

class Point(Model):

    def __init__(self):
        self.lat = None
        self.lon = None

    def __repr__(self):
        return 'Point(%s,%s)' % (self.lat, self.lon)

    def hydrate(self, element):
        self.lat = element.get('lat')
        self.lon = element.get('lon')

class Route(Model):
    """model object to represent the 'Route' """

    def __init__(self):
        self.color = None
        self.directions = []
        self.lat_min = None
        self.lat_max = None
        self.lon_min = None
        self.lon_max = None
        self.opposite_color = None
        self.paths = []
        self.tag = None
        self.title = None
        self.short_title = None
        self.stops = []

    def __repr__(self):
        return 'Route(%s)' % self.title

    def hydrate(self, element):
        self.color = element.get('color')
        self.lat_max = element.get('latMax')
        self.lat_min = element.get('latMin')
        self.lon_max = element.get('lonMax')
        self.lon_min = element.get('lonMin')
        self.opposite_color = element.get('oppositeColor')
        self.tag = element.get('tag')
        self.title = element.get('title')
        self.short_title = element.get('shortTitle')

        directions = element.xpath('direction')

        dirs = []

        for d in directions:
            dirs.append(Direction.from_element(d))
        self.directions = dirs

        stops = element.xpath('stop')

        stps = []
        for s in stops:
            stps.append(Stop.from_element(s))
        self.stops = stps

        paths = element.xpath('path')

        pths = []
        for p in paths:
            pths.append(Path.from_element(p))
        self.paths = pths

class Stop(Model):

    def __init__(self):
        self.tag = None
        self.title = None
        self.lat = None
        self.lon = None
        self.stop_id = None

    def __repr__(self):
        return 'Stop(%s)' % self.tag

    def hydrate(self, element):
        self.tag = element.get('tag')
        self.title = element.get('title')
        self.lat = element.get('lat')
        self.lon = element.get('lon')
        self.stop_id = element.get('stopId')





