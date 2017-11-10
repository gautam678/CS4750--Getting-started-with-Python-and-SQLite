import urllib.request
import urllib.parse
import json
import sqlite3
import time
import ssl
file = open('where.txt')
service_url = "http://maps.googleapis.com/maps/api/geocode/json?"
scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Locations (address TEXT, lat TEXT, lng TEXT, formatted_address TEXT)''')
for address in file:
    url = service_url + urllib.parse.urlencode({"sensor":"false", "address": address})
    request = urllib.request.urlopen(url, context = scontext).read()
    js = json.loads(request)
    lat = str(js['results'][0]['geometry']['location']['lat'])
    lng = str(js['results'][0]['geometry']['location']['lng'])
    formatted_address = str(js['results'][0]['formatted_address'])
    cur.execute('''INSERT INTO Locations (address, lat, lng, formatted_address)VALUES ( ?, ?, ?, ? )''', (address,lat,lng,formatted_address) )
    conn.commit()
    time.sleep(1)