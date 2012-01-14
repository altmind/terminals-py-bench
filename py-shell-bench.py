import time
import sys
import math
cycles=500
t1=time.time()
for i in range(cycles):
	print "8"*math.trunc(math.pow(i,1.2))
t2=time.time()
for i in range(cycles):
	print "8"*math.trunc(math.pow(i,1.2))
	sys.stdout.flush()
t3=time.time()
print "Time w/o flush %f sec" % (t2-t1)
print "Time w flush %f sec" % (t3-t2)