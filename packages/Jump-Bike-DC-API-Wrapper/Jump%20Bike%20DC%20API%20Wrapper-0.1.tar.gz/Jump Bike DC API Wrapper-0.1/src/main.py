import requests
import json

base_url = 'https://dc.jumpmobility.com/opendata'
class JumpBikeAPI:
    '''
    Main class to wrap the various JSON requests that the Jump Bike D.C API has 
    available. 
    '''
    def FreeBikeStatus(self):
        '''
        Returns all the free Jump Bikes in D.C . Returns longitude, latitude,
        bike name, bike ID, and charge level
        '''
        req = requests.get(base_url + '/free_bike_status.json')
        Data = json.loads(req.text)  
        return Data    

    def SystemInformation(self):
        '''
        Returns system information about Jump Bike D.C such as phone number
        and email. 
        '''
        req = requests.get(base_url + '/system_information.json')
        Data = json.loads(req.text)      
        return Data

    def StationInformation(self):
        '''
        Returns information about the several rent stations that Jump Bike D.C
        has in D.C . Gives id, name, address, payment methods, longitude, and latitude.
        '''
        req = requests.get(base_url + '/station_information.json')
        Data = json.loads(req.text) 
        return Data

    def SystemHours(self):
        '''
        Returns the hours of the day that renting a Jump Bike is possible.
        '''
        req = requests.get(base_url + '/system_hours.json')
        Data = json.loads(req.text) 
        return Data

    def SystemCalendar(self):
        '''
        Returns a simple calendar for the bike system.
        '''
        req = requests.get(base_url + '/system_calendar.json')
        Data = json.loads(req.text) 
        return Data

    def SystemRegions(self):
        '''
        Returns basic information, really just the name, of the D.C
        Jump Bike region. 
        '''
        req = requests.get(base_url + '/system_regions.json')
        Data = json.loads(req.text) 
        return Data
        
    def SystemPricing(self):
        '''
        Returns the pricing plans Jump Bike has in D.C .
        '''
        req = requests.get(base_url + '/system_pricing_plans.json')
        Data = json.loads(req.text) 
        return Data
        
    def SystemAlerts(self):
        '''
        Returns any alerts Jump Bike D.C has. 
        '''
        req = requests.get(base_url + '/system_alerts.json')
        Data = json.loads(req.text) 
        return Data
        