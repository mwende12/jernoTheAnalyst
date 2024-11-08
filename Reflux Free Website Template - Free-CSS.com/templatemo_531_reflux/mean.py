import numpy as np
def calculate(num):
    n=np.array(num).reshape(3,3)
    cal=dict()
    cal['mean']=[n.mean(0).tolist(),n.mean(1).tolist(),n.mean()] 
    cal['variance']=[n.var(0).tolist(), n.var(1).tolist(),n.var()]
    cal['standard deviation']=[n.std(0).tolist(),n.std(1).tolist(),n.std()]
    cal['max']=[n.max(0).tolist(),n.max(1).tolist(),n.max()]
    cal['min']=[n.min(0).tolist(),n.min(1).tolist(),n.min()]
    cal['sum']=[n.sum(0).tolist(),n.sum(1).tolist(),n.sum()]
    
    print(cal)
   
calculate([0,1,2,3,4,5,6,7,8])