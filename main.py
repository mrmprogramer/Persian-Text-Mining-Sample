import PreProcess as pr
from os import listdir
from os.path import isfile, join

from apicontoroller import api


files = [f for f in listdir('datamodel') if isfile(join('datamodel', f))]

for f in files:
    pr.pl('*******************************')
    pr.pl('filename:'+f)
    pr.Normalize(f)
    pr.removestopwords(f)
    pr.stemmingandcounting(f)

# # run api 



api().run()
