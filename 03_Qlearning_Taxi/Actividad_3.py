
import gymnasium as gym
import numpy as np
import random
import matplotlib.pyplot as plt

from IPython.display import HTML
from matplotlib import animation



def train_q_learning(
    env,
    Q,
    episodes=5000,
    alpha=0.1,
    gamma=0.95,
    epsilon=0.1,
    max_steps=200
):
    rewards = []

    for episode in range(episodes):
        state, _ = env.reset()
        total_reward = 0

        for _ in range(max_steps):

            
            action = choose_action(Q, state, epsilon, env)

            
            next_state, reward, terminated, truncated, _ = env.step(action)

            
            update_q(
                Q,
                state,
                action,
                reward,
                next_state,
                alpha,
                gamma
            )

            
            state = next_state
            total_reward += reward

            
            if terminated or truncated:
                break

        rewards.append(total_reward)

    return Q, rewards


