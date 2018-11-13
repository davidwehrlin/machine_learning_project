import gym_intersection
from time import sleep
from IPython.display import clear_output
import random
import gym
import numpy as np
np.random.seed(0)

def initialize_q_table(env):
    """Initialize a Q table for an environment with all 0s

    Args:
        env (gym.envs): The environment

    Returns:
        np.array: The Q table
    """
    return np.zeros([env.observation_space.n, env.action_space.n])

def select_action(q_row, method, epsilon=0.5):
    """Select the appropriate action given a Q table row for the state and a chosen method

    Args:
        q_row (np.array): The row from the Q table to utilize
        method (str): The method to use, either "random" or "epsilon"
        epsilon (float, optional): Defaults to 0.5. The epsilon value to use for epislon-greed action selection

    Raises:
        NameError: If method specified is not supported

    Returns:
        int: The index of the action to apply
    """
    if method not in ["random", "epsilon"]:
        raise NameError("Undefined method.")
    if method == "random":
        return np.random.randint(len(q_row))
    if method == "epsilon":
        max_value = 0
        max_index = 0
        for i in range(len(q_row)):
            if q_row[i] > max_value:
                max_value = q_row[i]
                max_index = i
        return max_index

def calculate_new_q_val(q_table, state, action, reward, next_state, alpha, gamma):
    """Calculate the updated Q table value for a particular state and action given the necessary parameters

    Args:
        q_table (np.array): The Q table
        state (int): The current state of the simulation's index in the Q table
        action (int): The current action's index in the Q table
        reward (float): The returned reward value from the environment
        next_state (int): The next state of the simulation's index in the Q table (Based on the environment)
        alpha (float): The learning rate
        gamma (float): The discount rate

    Returns:
        float: The updated action-value expectation for the state and action
    """

    return (1-alpha)*q_table[state][action] + alpha*(reward + gamma* select_action(q_table[next_state], "epsilon" ))
    
def main():
    env = gym.make("Intersection-v0")
    my_q = initialize_q_table(env)
    for i in range
    return

main()
