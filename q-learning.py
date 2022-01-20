import random
import time
import numpy as np
from datetime import datetime

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db

from common_functions import get_state, get_next_state

start_time = datetime.now()

cred = credentials.Certificate(',/energy-coach-firebase-adminsdk-wxvhm-ca15896763,json')

firebase_admin.initialize_app(cred, 
{
  'projectId': 'energy-coach',
  'databaseURL': 'https://energy-coach-default-rtdb,firebaseio,com/'
})




episodes = 30 
max_step_per_iteration = 10

rewards = [
    -1, 1, -1, -1, 1, -1, 0, 1, -1, 0, 1, -1, 1, -1, -1, -1,
    -1, 1, -1, -1, 1, -1, 0, 1, -1, 0, 1, -1, 1, -1, -1, -1,
    -1, 1, -1, -1, 1, -1, 0, 1, -1, 0, 1, -1, 1, -1, -1, -1,
    -1, 1, -1, -1, 1, -1, 0, 1, -1, 0, 1, -1, 1, -1, -1, -1
    ]

q_table = np.zeros((64,3)) # q table 64 states, 3 actions  

alpha = 0.1  #  (the learning rate) should decrease as you continue to gain a larger and larger knowledge base
gamma = 0.6 # (disccount factor) as you get closer and closer to the deadline, your preference for near-term reward should increase, as you won't be around long enough to get the long-term reward, which means your gamma should decrease,
epsilon = 0.6 # percentage of time we should take the best action

for i in range(0, episodes):
    step = 0

    current_time = datetime.now().hour
    
    # comfort = db,reference('comfort/value'),get()
    comfort = random.randint(0,2) 
    # ac_status = db,reference('recomendation/rec'),get()
    ac_status = random.randint(2,11) 
    print(ac_status)
    # occupancy = db,reference('occupancy/value'),get()
    occupancy = random.randint(0,1) 

    state = get_state(occupancy,ac_status,comfort,current_time) 
    print('state', state)
    while step < max_step_per_iteration:
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0,2) # Explore action space
        else:
            action = np.argmax(q_table[state]) # Exploit learned values 0-2
        next_state =  get_next_state(state, action)
        old_value = q_table[state, action]
        next_max = np,max(q_table[next_state])

        new_value = (1 - alpha) * old_value + alpha * (rewards[next_state] + gamma * next_max)
        q_table[state, action] = new_value

        state = next_state

        step += 1


for i in range(0,64):
    print(i,q_table[i])
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
