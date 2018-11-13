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
# Description:
#     There are four designated locations in the grid world indicated by R(ed), B(lue), G(reen), and Y(ellow).
#     When the episode starts, the taxi starts off at a random square and the passenger is at a random location.
#     The taxi drive to the passenger's location, pick up the passenger, drive to the passenger's destination (another one of the four specified locations),
#     and then drop off the passenger. Once the passenger is dropped off, the episode ends.
#     Observations:
#     There are 500 discrete states since there are 25 taxi positions, 5 possible locations of the passenger
#     (including the case when the passenger is the taxi), and 4 destination locations.

from gym_intersection.envs.intersection_tools import LaneQueue, Car, Intersection



class IntersectionEnv(gym.Env):
    def __init__(self):
        # General variables defining the environment
        # Intersection states include NS & SS, ES & WS, NL, EL, SL, WL
        # Where first character could be N-Northbound, E-Eastbound, S-Southbound, W-Westbound
        # and second character could be S-Straight and left or L-Left
        self.num_actions = 6
        self.num_lanes = 2 #Straight/Right and Left
        self.num_directions = 4 #NESW
        self.lane_size = 5
        self.is_blocked = False

        self.intersection = Intersection(self.lane_size)

        # Initializing
        self.current_step = -1
        self.current_episode = -1
        self.current_state = -1

        # Define actions
        # Specifically the agent can only change the light to a Discrete amount of states
        self.action_space = spaces.Discrete(self.num_states)

        # Define observations
        # An array of length 8 which represents the amount of cars in each lane
        self.observation_space = spaces.Discrete(self.num_lanes ** (self.lane_size + 1))

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
        -------def reset(self):
        print("Reset")
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

        #D uring step insert cars
        #
        self.current_step += 1
        self._take_action(action_state)
        observation = self._get_observation()
        reward = self._get_reward()
        done = True
        info = {}
        return observation, reward, done, info

    def render(self):
        return "no"

    def _take_action(self, action):

        return

    def _get_reward(self):

        return 0

    def _get_observation(self):
        return intersection.get_observation()

    def reset(self):
        #returns observation
        print("Reset")
        return [0] * 8
