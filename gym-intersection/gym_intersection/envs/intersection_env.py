#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simulates the environment of an Intersection
Each episode is the time it takes for a set amount of cars to get through the intersection
"""

import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
from intersection_tools import *

class IntersectionEnv(gym.Env):
    def __init__(self):
        # General variables defining the environment
        # Intersection states include NS & SS, ES & WS, NL, EL, SL, WL
        # Where first character could be N-Northbound, E-Eastbound, S-Southbound, W-Westbound
        # and second character could be S-Straight and left or L-Left
        self.num_states = 6
        self.num_lanes = 2 #Straight/Right and Left
        self.num_directions = 4 #NESW
        self.lane_size = 5
        self.is_blocked = False



        # Initializing
        self.current_step = -1
        self.current_episode = -1
        self.current_state = -1

        # Define actions
        # Specifically the agent can only change the light to a Discrete amount of states
        self.action_space = spaces.Discrete(num_states)

        # Define observations
        # A 2 by 4 box represent the amount of cars in each lane
        self.observation_space = spaces.Box(low=0, high=lane_size, shape=(num_lanes, num_directions))

        # Store memory of the agents actions
        # These will be the state change the agent made during one runthrough of the algorithm
        self.action_episode_memory = []

    def step(self, action_state):
        """
        The agent makes a decision in the environment

        Parameters
        ----------
        action_state: int - Represents which light configuration the agent took

        Returns
        -------
        ob, reward, episode_over, info : tuple
            ob (object) :
                an environment-specific object representing your observation of
                the environment.
            reward (float) :
                amount of reward achieved by the previous action. The scale
                varies between environments, but the goal is always to increase
                your total reward.
            episode_over (bool) :
                whether it's time to reset the environment again. Most (but not
                all) tasks are divided up into well-defined episodes, and done
                being True indicates the episode has terminated. (For example,
                perhaps the pole tipped too far, or you lost your last life.)
            info (dict) :
                 diagnostic information useful for debugging. It can sometimes
                 be useful for learning (for example, it might contain the raw
                 probabilities behind the environment's last state change).
                 However, official evaluations of your agent are not allowed to
                 use this for learning.
        """
        self.current_step += 1
        self._take_action(action)
        observation = self._get_observation()
        reward = self._get_reward()
        done = True
        info = {}
        return observation, reward, done, info


    def _take_action(self, action):
        print("Changed State")
        return

    def _get_reward():
        return 0

    def _get_observation(self, action):
        print("Received Observation")
        return
