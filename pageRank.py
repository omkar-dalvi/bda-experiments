import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
def p(M, it=100000, d=0.8):
  N=M.shape[1]
  ebyn=np.full((N,N),1/N)
  vprime=d*M+(1-d)*ebyn
  v=np.full((N,1),1/N)
  iteration=0
  while(iteration<it):
    iteration+=1
    v=np.matmul(vprime,v)
  return v
M=np.array([
 [0.5,0.5,0],
 [0.5,0,0,],
 [0,0.5,1]
  ])
G=nx.from_numpy_matrix(M)
nx.draw(G, with_labels=True)
plt.show()
v=p(M)
print("Page ranks are: ")
print(v)
