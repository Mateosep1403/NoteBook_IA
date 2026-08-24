
import gymnasium as gym
import numpy as np
import random
import matplotlib.pyplot as plt

from IPython.display import HTML
from matplotlib import animation



def update_q(Q, state, action, reward, next_state, alpha, gamma):

    target = reward + gamma * np.max(Q[next_state])

    td_error = target - Q[state, action]

    Q[state, action] += alpha * td_error


    