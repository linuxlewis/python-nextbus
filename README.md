#python-nextbus
==============

python client for nextbus api


## description
Simple python wrapper around the nextbus api.
See the nextbus api docs http://www.nextbus.com/xmlFeedDocs/NextBusXMLFeed.pdf

## installation
    sudo pip install python-nextbus
or
    sudo easy_install python-nextbus

## dependencies
Depends on requests and lxml

## examples

### agency list
```python
>>> import nextbus
>>> agencies = nextbus.agency_list()
>>> agencies
[Agency(AC Transit), Agency(CMRT and Howard Transit), Agency(California University of Pennsylvania),...
```
### route list
```python
>>> routes = nextbus.route_list(agency='sf-muni')
>>> routes
[Route(F-Market & Wharves), Route(J-Church), Route(KT-Ingleside/Third Street),....
```

### route config
```python
>>> route = nextbus.route_config(agency='sf-muni', route='1')
>>> route
Route(1-California)
```






