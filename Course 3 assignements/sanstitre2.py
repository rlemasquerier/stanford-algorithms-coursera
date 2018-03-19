# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 23:21:40 2018

@author: Rodolphe
"""

import requests
import urllib
parameters = {'api_key': 'LVplVkTrn0PSxny38wvdzlonIf4pj9PXifSFU6NC'}
req = requests.get('https://epic.gsfc.nasa.gov/api/natural/date/2015-10-31', params=parameters)
print(req.json())
for pict in req.json():
    url = 'https://api.nasa.gov/EPIC/archive/natural/2015/10/31/png/'+pict['image']+'.png?api_key='+parameters['api_key']
    a = urllib.request.urlopen(url)
    print(a)
    b = a.read()
    image = open(pict['image']+'.png', 'wb')
    image.write(b)