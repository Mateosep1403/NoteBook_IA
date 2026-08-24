import numpy as np
import random



def choose_action(Q, state, epsilon, env):

    if random.random() < epsilon:
        return env.action_space.sample()
    else:
        return np.argmax(Q[state])

