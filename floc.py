import numpy as np
import time
import sys

e=1

prob=" ".join(sys.argv[1:]).split('.')[0]
fil=prob+'.npz'

npzfile = np.load(fil)
npzfile.files
m=npzfile['m'] #Location count, int
n=npzfile['n'] #Customer count, int
s=npzfile['s'] #Supply, vector
d=npzfile['d'] #Demand, vector
f=npzfile['f'] #Initial cost, vector
c=npzfile['c'] #Flow cost, matrix
#print 'm:',m,' n:',n
#print 's:',s
#print 'd:',d
#print 'f:',f
#print 'c:',c

t1=time.time()
x=np.zeros((m,n),dtype=np.int)
y=np.zeros((m),dtype=np.int)

ss=s
dd=d

#Create a list of tuples on the form (index, total_flow_cost + e*construction_cost) sorted on cost in descending order
indicies = [(i, int(sum(c[i])) + int(e*f[i])) for i in range(m)]
indicies.sort(lambda x, y: y[1] - x[1])
locations = [i[0] for i in indicies]

u = n - 1
while sum(dd) > 0:
    l = locations.pop()
    y[l] = 1

    while ss[l] > 0:

        #ship as much as possible from the factory
        #while not shipping more than the customers demand
        w = min(ss[l], dd[u])
        x[l, u] = w
        ss[l] = ss[l] - w
        dd[u] = dd[u] - w
        
        #if the customer want more than the current factory can supply
        #we construct and begin shipping from the next factory (if we are done we break out of both loops)
        #else start shipping to the next customer
        if dd[u] > 0 or sum(dd) == 0:
            break
        else:
            u = u - 1

        
elapsed = time.time() - t1
print('Tid: ' + str('%.4f' % elapsed))

cost=sum(sum(np.multiply(c,x))) + e*np.dot(f,y)
print('Problem:',prob,' Totalkostnad: ' + str(cost))
print('y:',y)
print('Antal byggda fabriker:',sum(y),'(av',m,')')
