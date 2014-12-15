#! C:/Python27/python
import csv

templateFile = open('template.html','r')
template = templateFile.read()

# read and replace lat in template file 
reader = csv.reader(open("data/lat.dat","rb"))
lat = ""
for row in reader:
	for val in row:
		lat = lat + val + ","
template = template.replace("<-lat->",lat)

# read and replace lon in template file 
reader = csv.reader(open("data/lon.dat","rb"))
lon = ""
for row in reader:
	for val in row:
		lon = lon + val + ","
template = template.replace("<-lon->",lon)

# read and replace score in template file 
reader = csv.reader(open("data/score.dat","rb"))
score = ""
for row in reader:
	for val in row:
		score = score + val + ","
template = template.replace("<-score->",score)

# read and replace timeseries in template file
reader = csv.reader(open("data/timeseries.dat","rb"))
timeseries = ""
for row in reader:
	timeseries = timeseries + "["
	for val in row:
		timeseries = timeseries + val + ","
	timeseries = timeseries + "],"
template = template.replace("<-timeseries->",timeseries)

outputFile = open('output.html','w')
outputFile.write(template)	
