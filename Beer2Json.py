#from __future__ import print_fuction
import csv
import json

csvfile = open('craft_cans.csv', 'r')
jsonfile = open('beer.json', 'w')

field_names = ("Number", "Beer","Brewery","Location","Style","Size","Abv", "Ibus")
print("Reading csv file")
reader = csv.DictReader( csvfile, field_names)

print("Output to json")
out = json.dumps( [ row for row in reader ] )
jsonfile.write(out)
