import sqlite3
import codecs
conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()
table = cur.execute('SELECT * from Locations')
fhand = codecs.open('where.js','w','utf-8')
fhand.write("myData = [\n")
count = 1
for row in table:
    if count>=1:
        output = "["+str(row[1])+","+str(row[2])+", '"+str(row[3])+"']"
        fhand.write(output)
        fhand.write(",\n")
        count+=1
fhand.write("\n];\n")
cur.close()
fhand.close()
