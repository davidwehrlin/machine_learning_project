#!/usr/bin/env python
# -*- coding: utf-8 -*-

# core modules
import unittest
import threading

# 3rd party modules
import gym
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np

# internal modules
import gym_intersection
from gym_intersection.envs.intersection_tools import Intersection

var = {
    # Action selection hyperparams
    "method": "epsilon",
    "epsilon": 0.1,
    "alpha": 0.3,
    "gamma": 0.8
}

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

def rotate_tuple(tup):
    return (tup[6], tup[7],  tup[0], tup[1], tup[2], tup[3], tup[4], tup[5])

def double_rotate(tup):
    tup = rotate_tuple(tup)
    tup = rotate_tuple(tup)
    return tup

def quadrouple_rotate(tup):
    tup = rotate_tuple(tup)
    yield tup
    tup = rotate_tuple(tup)
    yield tup
    tup = rotate_tuple(tup)
    yield tup
    tup = rotate_tuple(tup)
    yield tup


class DictHolder():

    def __init__(self):
        self.dict = {}

    def __getitem__(self, i):
        if i in self.dict:
            return self.dict[i]
        self.dict[i] = [np.random.random_sample()*(-1), 
        np.random.random_sample()*(-1), 
        np.random.random_sample()*(-1), 
        np.random.random_sample()*(-1), 
        np.random.random_sample()*(-1), 
        np.random.random_sample()*(-1)]
        return self.dict[i]

class EnvironmentTests(unittest.TestCase):

    def test_env(self):
        self.env = gym.make('Intersection-v0')
        self.env.reset()
        self.env.step(0)
        # self.env.render()

    def train_sim(self, num_episodes=1000000, av_over=1000):
        self.episodes = num_episodes
        self.q_table = DictHolder()
        rewards = []
        for i in range(1,num_episodes):
            current_state = self.env.reset()
            done = False

            total_reward = 0

            while not done:
                action = select_action(self.q_table[current_state], "epsilon", epsilon=var["epsilon"])
                next_state, reward, done, info = self.env.step(action)
                new_q_val = calculate_new_q_val(self.q_table, current_state, action, reward, next_state, var["alpha"], var["gamma"])
                if action in [0, 1]:
                    for (index, tup) in enumerate(double_rotate(current_state)):
                        self.q_table[tup][(action + index) % 2] = new_q_val
                else:
                    for (index, tup) in enumerate(quadrouple_rotate(current_state)):
                        self.q_table[tup][((action + index) % 4) + 2] = new_q_val
                current_state = next_state
                total_reward += reward
            rewards.append(total_reward)
            if i % av_over == 0:
                # plt.scatter(list(range(len(rewards))[-1000:]), rewards[-1000:]))
                plt.scatter(i, sum(rewards[-av_over:])/av_over)
                # plt.pause(0.1)
                plt.savefig('foo.png')
        # print(self.q_table.dict)
        plt.show()

    def test_sim(self):
        rewards = []
        for i in range(100):
            current_state = self.env.reset()

            total_reward = 0
            done = False
            step = 0

            while not done:
                q_row = self.q_table[current_state]
                action = 0
                max_q = q_row[0]
                for i in range(len(q_row)):
                    if q_row[i] >= max_q:
                        action = i
                        max_q = q_row[i]
                next_state, reward, done, info = self.env.step(action)
                current_state = next_state
                total_reward += reward
                step += 1
            rewards.append(total_reward)
        # print(rewards)
        plt.scatter(list(range(len(rewards))), rewards)
        plt.show()

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

threads = []
for _ in range(48):
    threads.append(threading.Thread(target=test.train_sim))
for t in threads:
    t.start()
for t in threads:
    t.join()

test.test_sim()
# test.test_intersection()
