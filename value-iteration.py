import random
import time
import numpy as np
from datetime import datetime

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db

from probability import probs2
from common_functions import get_state, get_next_state


start_time = datetime.now()

cred = credentials.Certificate('./energy-coach-firebase-adminsdk-wxvhm-ca15896763.json')

firebase_admin.initialize_app(cred, 
{
  'projectId': 'energy-coach',
  'databaseURL': 'https://energy-coach-default-rtdb.firebaseio.com/'
})

q_table = np.zeros((64,3))

P=probs2
gamma=0.9
R= [[1,-1,-1],
[1,-1,-1],
 [-1,1,-1],    
 [1,0,-1],   
 [1,0,-1],    
 [-1,-1,1],    
 [1,0,-1],
 [0,1,-1],
 [-1,-1,1],
 [1,0,-1],
 [1,0,-1],
 [-1,0,1],#11
 [1,-1,-1],
 [1,-1,-1],
 [1,-1,-1],
 [1,-1,-1],
 [1,-1,-1],#16
[1,-1,-1],
 [-1,1,-1],    
 [1,0,-1],   
 [1,0,-1],    
 [-1,-1,1], #21   
 [1,0,-1],
 [0,1,-1],
 [-1,-1,1],
 [1,0,-1],#25
 [1,0,-1],
 [-1,0,1],
 [1,-1,-1],#28
 [1,-1,-1],
 [1,-1,-1],
 [1,-1,-1],
 [1,-1,-1],#32
[1,-1,-1],
 [-1,1,-1],    
 [1,0,-1], #35  
 [1,0,-1],    
 [-1,-1,1],    
 [1,0,-1], #38
 [0,1,-1],
 [-1,-1,1],
 [1,0,-1],#41
 [1,0,-1],
 [-1,0,1],
 [1,-1,-1],#44
 [1,-1,-1],
 [1,-1,-1],
 [1,-1,-1],
 [1,-1,-1],#48
[1,-1,-1],
 [-1,1,-1],    
 [1,0,-1], #51  
 [1,0,-1],    
 [-1,-1,1],    
 [1,0,-1],#54
 [0,1,-1],
 [-1,-1,1],
 [1,0,-1],#57
 [1,0,-1],
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

ref = db.reference("/recomendation/rec/")
recommendation = ref.get()
print(recommendation)
# for key, value in best_sellers.items():
# 	if(value["Author"] == "J.R.R. Tolkien"):
# 		value["Price"] = 90
# 		ref.child(key).update({"Price":80})
        
def sendToDB(state, action):

  code = 0
  if action == 0:#apagar
    code = 2
  if action == 1: #subir
    if 3 <= state <=5 or  19 <= state <= 21 or 35<= state <=37 or 51<= state <=53:
      code = random.randint(6,8) #seteamos a T2
    if 6 <= state <=8 or  22 <= state <= 24 or 38<= state <=40 or 54<= state <=56:
      code = random.randint(9,11) #seteamos a T3
    if 9 <= state <=11 or  25 <= state <= 27 or 41<= state <=43 or 57<= state <=59:
      code = random.randint(9,11) #seteamos a T3
  if action == 2: #bajar
    if 3 <= state <=5 or  19 <= state <= 21 or 35<= state <=37 or 51<= state <=53:
      code = random.randint(3,5) #seteamos a T1
    if 6 <= state <=8 or  22 <= state <= 24 or 38<= state <=40 or 54<= state <=56:
      code = random.randint(3,5) #seteamos a T1
    if 9 <= state <=11 or  25 <= state <= 27 or 41<= state <=43 or 57<= state <=59:
      code = random.randint(6,8) #seteamos a T2
   

  
  

  return None

# for i in range(len(Q)):
#     print(i,Q[i])

previous_state = 0
n = 0
while n<3:
  current_time = datetime.now().hour
  print(n)  
    # comfort = db.reference('comfort/value'),get()
  comfort = random.randint(0,2) 
    # ac_status = db.reference('recomendation/rec'),get()
  ac_status = random.randint(2,11) 
    # occupancy = db.reference('occupancy/value'),get()
  occupancy = random.randint(0,1) 
  #state = get_state(occupancy,ac_status,comfort,current_time) 
  state = 1
  if state == previous_state:
    print("si es igual")
    time.sleep(5) 
  elif state ==  get_next_state(state,action):
    print("no es ")  
  else:
    sendToDB()
  previous_state = state
  # action=np.argmax(Q[state])
  # new_state = get_next_state(state,action)
  n += 1
  # old_state=sendToDB()
  # if old_state == get_state(occupancy,ac_status,comfort,current_time) :
  #   time.sleep(60)
    
  
