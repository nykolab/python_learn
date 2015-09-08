x_range = 11
y_range = 11


for x in xrange(1, x_range):
    print ("   {:^3d}".format(x)),
print 
print ("-" * x_range*7)

for x in xrange(1, x_range):
    for y in xrange(1, y_range):
        print ("   {0:^3d}".format(x*y)),
    print "\n"
