import numpy as np

a=np.array([[3],[2],[4]])
b=np.array([5,4,7])
c=np.broadcast(a,b)
out=np.empty(c.shape)
out.flat=[u+v for(u,v) in b]
print(out)