# CS4750--Getting-started-with-Python-and-SQLite

This is the code for the tutorial conducted in class on 11/009/2017.

* Learn how to insert and retrieve data from sqlite3 using Python.
* Using Google Maps API, get latitude and longitude of locations and push it to the database.


## Required Softwares & Packages
* [SQLite browser](http://sqlitebrowser.org/)
* sqlite3
* It is always a good idea to create a developer account when you work with APIs. For geocoding API, you'll have to use an API [key](https://developers.google.com/maps/documentation/geocoding/start)
## Running the code

* Create a text file in the working directory called 'where.txt'. This would contain the name of the locations we would
  want to mark in map.
* Run geoload.py to populate data in the database
* Run geodump.py, this reads from the sqlite database created and pulls data
* Open where.html to see locations you specified on where.txt marked on the map.


## Note
This tutorial is part of a course I took a couple of years back. If you guys are interested, you can take the [course](https://www.coursera.org/learn/python-databases).



