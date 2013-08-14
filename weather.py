import sys
import urllib
import lxml.html
import datetime

sock = urllib.urlopen("http://www.weather.com/weather/hourbyhour/graph/USNY0996")
wsource = sock.read()
sock.close()
html = lxml.html.fromstring(wsource)


# part 1: wx-timepart
# part 2: wx-conditions (image + description)
# part 3: temperature
# part 4: details

now = datetime.datetime.now().strftime('%H:%M:%S')
print 'now=%s'%now

temp = []
elements = html.find_class("wx-temp")
for i in range(len(elements)):
    temp.append(float(elements[i].text_content()[1:3]))
print temp

time1 = []
elements = html.find_class("wx-time")
for i in range(len(elements)):
    time1.append(elements[i].text_content())
print time1

res = []


sys.exit(2)

for line in res:
    print line
    line = line.split('\n')
    for k,x in enumerate(line):
        print k, x
    sys.exit()
