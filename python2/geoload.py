import urllib
import json
import sqlite3
import time
file = open('where.txt')
service_url = "http://maps.googleapis.com/maps/api/geocode/json?"
scontext = None
# scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Locations (address TEXT, lat TEXT, lng TEXT, formatted_address TEXT)''')
for address in file:
    url = service_url + urllib.urlencode({"sensor":"false", "address": address})
    request = urllib.urlopen(url, context = scontext).read()
    js = json.loads(str(request))
    print request
    lat = str(js['results'][0]['geometry']['location']['lat'])
    lng = str(js['results'][0]['geometry']['location']['lng'])
    formatted_address = str(js['results'][0]['formatted_address'])
    cur.execute('''INSERT INTO Locations (address, lat, lng, formatted_address)VALUES ( ?, ?, ?, ? )''', ( buffer(address),buffer(lat),buffer(lng),buffer(formatted_address) ) )
    conn.commit()
    time.sleep(1)