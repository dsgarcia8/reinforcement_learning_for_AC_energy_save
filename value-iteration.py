
import random
import time
import numpy as np
from datetime import datetime

from probability import probs2

q_table = np.zeros((64,3))

P=probs2
gamma=0.9
R= [[1,-1,-1],
[1,-1,-1],
 [-1,1,-1],    
 [1,1,-1],   
 [1,1,-1],    
 [-1,-1,1],    
 [1,1,-1],
 [0,1,-1],
 [-1,-1,1],
 [1,0,-1],
 [1,1,-1],
 [-1,0,1],
 [1,-1,-1],
 [1,-1,-1],
 [1,-1,-1],
 [1,-1,-1],
 [1,-1,-1],
[1,-1,-1],
 [-1,1,-1],    
 [1,1,-1],   
 [1,1,-1],    
 [-1,-1,1],    
 [1,1,-1],
 [0,1,-1],
 [-1,-1,1],
 [1,0,-1],
 [1,1,-1],
 [-1,0,1],
 [1,-1,-1],
 [1,-1,-1],
 [1,-1,-1],
 [1,-1,-1],
 [1,-1,-1],
[1,-1,-1],
 [-1,1,-1],    
 [1,1,-1],   
 [1,1,-1],    
 [-1,-1,1],    
 [1,1,-1],
 [0,1,-1],
 [-1,-1,1],
 [1,0,-1],
 [1,1,-1],
 [-1,0,1],
 [1,-1,-1],
 [1,-1,-1],
 [1,-1,-1],
 [1,-1,-1],
 [1,-1,-1],
[1,-1,-1],
 [-1,1,-1],    
 [1,1,-1],   
 [1,1,-1],    
 [-1,-1,1],    
 [1,1,-1],
 [0,1,-1],
 [-1,-1,1],
 [1,0,-1],
 [1,1,-1],
 [-1,0,1],
 [1,-1,-1],
 [1,-1,-1],
 [1,-1,-1],
 [1,-1,-1]]

def value_iteration(P, R, gamma, tolerance=1e-3):
  """Find V* using value iteration,

  Args:
    P: numpy array defining transition dynamics, Shape: |S| x |A| x |S|,
    R: numpy array defining rewards, Shape: |S| x |A|,
    gamma: float, discount factor,
    tolerance: float, tolerance level for computation,

  Returns:
    V*: numpy array of shape ns,
    Q*: numpy array of shape ns x na,
  """
  P = np.array(P)
  R = np.array(R)
  print(P.shape)
  print(R.shape)
 

  V = np.zeros(64)
  Q = np.zeros((64, 3))
  
  error = tolerance * 2
  while error > tolerance:
    # This is the Bellman backup (onp,einsum FTW!),
    Q = R + gamma * np.matmul(P, V)
    new_V = np.max(Q, axis=1)
    error = np.max(np.abs(V - new_V))
    V = np.copy(new_V)
  return V, Q

V,Q=value_iteration(P,R,gamma)
print(V)

for i in range(len(Q)):
    print(i,Q[i])
