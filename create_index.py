from os import listdir, extsep
from os.path import isfile, join, splitext
import csv
import sys

mypath = sys.argv[1]
space = ''
maps = []

for f in listdir(mypath):
    if isfile(join(mypath, f)):
        name, extension = splitext(f)
        if extension == ''.join([extsep, 'map']):
            maps.append(name)


with open('maps.csv', 'wt') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=';', lineterminator='\n', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for m in maps:
        print(m)
        filewriter.writerow([m, space])
