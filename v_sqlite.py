import sqlite3 as lite
import pandas as pd
con = lite.connect("sample.db")


cities = ( ('New York City', 'NY'),
    ('Boston', 'MA'),
    ('Chicago', 'IL'),
    ('Miami', 'FL'),
    ('Dallas', 'TX'),
    ('Seattle', 'WA'),
    ('Portland', 'OR'),
    ('San Francisco', 'CA'),
    ('Los Angeles', 'CA')  )

weather = (("New York City",2013,"July","January",62),
  ("Boston",2013,"July","January",59),
  ("Chicago",2013,"July","January",59),
  ("Miami",2013,"August","January",84),
  ("Dallas",2013,"July","January",77),
  ("Seattle",2013,"July","January",61),
  ("Portland",2013,"July","December",63),
  ("San Francisco",2013,"September","December",64),
  ("Los Angeles",2013,"September","December",75))

minput=raw_input("Please Select A Month : ")
with con:    
  cur=con.cursor()

#Delete Old Tables
  cur.execute("DROP TABLE IF EXISTS cities")
  cur.execute("DROP TABLE IF EXISTS weather")

#Create new tables
  cur.execute("Create Table cities(name text, state text)")
  cur.execute("Create Table weather(city text, year integer, warm_month text, cold_month text, average_high integer)")
  
#Insert Data
  cur.executemany("Insert into cities values(?,?)",cities)
  cur.executemany("Insert into weather values(?,?,?,?,?)",weather)

#Group Table
  cur.execute("SELECT name, state, year, warm_month, cold_month FROM cities INNER JOIN weather ON name = city")

#Make DataFrame
  data=cur.fetchall()
  cols = [desc[0] for desc in cur.description]
  data_frame=pd.DataFrame(data,columns=cols)

#Convert to strings
for month in data_frame["warm_month"]:
  month=str(month)
#Month Data Frame
month=data_frame[data_frame["warm_month"]==minput]
length=len(month.index)
print length

element =0


print "The cities that are warmest in",minput,"are:",
while element <=length:
  city=data_frame["name"][element]
  state=data_frame["state"][element]
  print city,",", state,

  if element+1>length:
    break;
  else:
    print ",",
  element+=1

