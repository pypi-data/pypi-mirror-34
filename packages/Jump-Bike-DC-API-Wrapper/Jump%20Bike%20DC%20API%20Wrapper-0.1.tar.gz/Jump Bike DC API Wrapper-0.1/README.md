# Jump-Bike-D.C-Python-API-Wrapper

## 🚴 🚴 🚴🚴🚴

A wrapper for Jump Bike D.C's open [API](https://dc.jumpmobility.com/opendata) made in python. Meant to make it easier to make requests to the library.

For now no `PyPi` package but working on creating one.

Package depends on Requests and JSON, depends on no other packages.

To work with here is an example.

```python
from mainClass import JumpBikeAPI, base_url

API1 = JumpBikeAPI()
print(API1.FreeBikeStatus())

```
This will save a variable to the JSON feed that contains all open bikes at the moment. 

Here are all the commands, with documentation as well.

```python
FreeBikeStatus():
    '''
    Returns all the free Jump Bikes in D.C . Returns longitude, latitude,
    bike name, bike ID, and charge level
    '''

SystemInformation():
    '''
    Returns system information about Jump Bike D.C such as phone number
    and email. 
    '''

StationInformation():
    '''
    Returns information about the several rent stations that Jump Bike D.C
    has in D.C . Gives id, name, address, payment methods, longitude, and latitude.
    '''

SystemHours():
    '''
    Returns the hours of the day that renting a Jump Bike is possible.
    '''

SystemCalendar():
    '''
    Returns a simple calendar for the bike system.
    '''

SystemRegions():
    '''
    Returns basic information, really just the name, of the D.C
    Jump Bike region. 
    '''

SystemPricing():
    '''
    Returns the pricing plans Jump Bike has in D.C .
    '''

SystemAlerts():
    '''
    Returns any alerts Jump Bike D.C has. 
    '''

```
Just set any variable equal to `JumpBikeAPI()` and all these functions will be 
available to call, like `print(test.SystemAlerts()` to call any system alerts.
