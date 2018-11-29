#!/usr/bin/env python
# -*- coding: utf-8 -*-

# core modules
import unittest

# 3rd party modules
import gym
import numpy as np

# internal modules
import gym_intersection
from gym_intersection.envs.intersection_tools import Intersection

def select_action(q_row, method, epsilon=0.5):
    if method not in ["random", "epsilon"]:
        raise NameError("Undefined method.")
    if method == "random":
        return np.random.randint(len(q_row))
    if method == "epsilon":
        rand_num = np.random.uniform()
        if rand_num > epsilon:
            action = 0
            max_q = q_row[0]
            for i in range(len(q_row)):
                if q_row[i] >= max_q:
                    action = i
                    max_q = q_row[i]
            return action
        else: 
            return np.random.randint(len(q_row))

def calculate_new_q_val(q_table, state, action, reward, next_state, alpha, gamma):
    max_action = -1
    for i in range(len(q_table[state])):
        if q_table[next_state][i] > max_action:
            max_action = q_table[next_state][i]
    return (1-alpha)*q_table[state][action] + alpha*(reward + gamma * max_action)

class DictHolder():

    def __init__(self):
        self.dict = {}

    def __getitem__(self, i):
        if i not in self.dict:
            self.dict[i] = [0]*6
        return self.dict[i]

class EnvironmentTests(unittest.TestCase):

    def test_env(self):
        self.env = gym.make('Intersection-v0')
        self.env.reset()
        self.env.step(0)
        self.env.render()

    def train_sim(self, num_episodes=100):
        self.episodes = num_episodes
        self.q_table = DictHolder()
        for i in range(num_episodes):
            current_state = self.env.reset()
            done = False
            while not done:
                action = select_action(self.q_table[current_state], "epsilon", epsilon=0.1)
                next_state, reward, done, info = self.env.step(action)
                self.q_table[current_state][action] = calculate_new_q_val(self.q_table, current_state, action, reward, next_state, 0.1, 0.5)
                current_state = next_state
                self.env.render()
        print(self.q_table.dict)

    def test_intersection(self):
        #Checks to make sure that intersection will not overflow
        intersection = Intersection(5)
        for i in range(100):
            done = intersection.add_cars(i)
            if done:
                break
            intersection.intersection_step()
            intersection.draw_intersection()
        intersection.draw_intersection()
    def agent(self):
        pass


test = EnvironmentTests()
test.test_env()
test.train_sim()
#test.test_intersection()
