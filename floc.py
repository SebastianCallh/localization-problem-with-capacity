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
s=npzfile['s'] #Capacity, vector
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

locations = [zip(c[i], f[i]) for i in range(c.shape[1])]
print(locations)
#locations.sort(lambda x, y: sum(y) - sum(x))
#print([sum(x) for x in locations])

while sum(dd)>0:
    break
    # set x and y
    # deduct from ss and dd,
    # --------



elapsed = time.time() - t1
print('Tid: ' + str('%.4f' % elapsed))

cost=sum(sum(np.multiply(c,x))) + e*np.dot(f,y)
print('Problem:',prob,' Totalkostnad: ' + str(cost))
print('y:',y)
print('Antal byggda fabriker:',sum(y),'(av',m,')')
input('')
