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

cred = credentials.Certificate('./energy-coach-firebase-adminsdk-wxvhm-d5099bd43d.json')

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
ref = db.reference("/recomendation/")
recommendation = ref.get()

def sendToDB(state, action):
  print("estado y accion:",state,action)
  code = 0
  if action == 0:#apagar
    code = 2
  if action == 1: #subir
    if (0 <= state <=2) or  (16 <= state <= 18) or (32<= state <=34) or (48<= state <=50):
      print("hola")
      code = random.randint(9,11) #seteamos a T3
    elif 3 <= state <=5 or  19 <= state <= 21 or 35<= state <=37 or 51<= state <=53:
      code = random.randint(6,8) #seteamos a T2
    elif 6 <= state <=8 or  22 <= state <= 24 or 38<= state <=40 or 54<= state <=56:
      code = random.randint(9,11) #seteamos a T3
    elif 9 <= state <=11 or  25 <= state <= 27 or 41<= state <=43 or 57<= state <=59:
      code = random.randint(9,11) #seteamos a T3
    else:
      print("no entra a los otros")
      code=2 #apagar
  if action == 2: #bajar
    if 0 <= state <=2 or  16 <= state <= 18 or 32<= state <=34 or 48<= state <=50:
      code = 2 #apagar
    elif 3 <= state <=5 or  19 <= state <= 21 or 35<= state <=37 or 51<= state <=53:
      code = random.randint(3,5) #seteamos a T1
    elif 6 <= state <=8 or  22 <= state <= 24 or 38<= state <=40 or 54<= state <=56:
      code = random.randint(3,5) #seteamos a T1
    elif 9 <= state <=11 or  25 <= state <= 27 or 41<= state <=43 or 57<= state <=59:
      code = random.randint(6,8) #seteamos a T2
    else:
      code=2 #apagar
  print("codigo a  enviar:",code)
  ref.update({"rec":code})
  time.sleep(3600)
  return None

previous_state = 0

while 1:
  current_time = datetime.now().hour
  comfort = db.reference('comfort/value').get()
  ac_status = db.reference('recomendation/rec').get()
  occupancy = db.reference('occupancy/value').get()
  state = get_state(occupancy,ac_status,comfort,current_time) 
  action=np.argmax(Q[state])
  new_state = get_next_state(state,action)
  print("estado, accion, nexstate", state,action,new_state)

  if state == previous_state:
    print("si es igual")
    time.sleep(60) 
  elif state ==  new_state:
    print("no es ")
    time.sleep(60)   
  else:
    sendToDB(state,action)
  previous_state = state

    
