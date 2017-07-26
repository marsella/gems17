from datetime import datetime
DATE = 0
IN = 1
OUT = 2
NOTE = 3


lines = [l.split(' | ') for l in open('time.csv').readlines()[1:]]
lines = [(date, datetime.strptime(inp,'%H%M'), datetime.strptime(out,'%H%M')) 
    for (date,inp,out,note) in lines]

minutes = [l[OUT] - l[IN] for l in lines]
seconds = sum([m.total_seconds() for m in minutes])
hours = seconds / 3600.

print "%f ~ $%.2f" % (hours, 16*hours)

