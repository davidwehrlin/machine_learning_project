#!/usr/bin/env python
# -*- coding: utf-8 -*-

# core modules
import unittest

# 3rd party modules
import gym

# internal modules
import gym_intersection
from gym_intersection.envs.intersection_tools import Intersection

class EnvironmentTests(unittest.TestCase):

    def test_env(self):
        env = gym.make('Intersection-v0')
        env.reset()
        env.step("NS & SS")
        env.render()

    def test_intersection(self):
        intersection = Intersection(5)
        intersection.draw_intersection()
        intersection.add_cars(5)
        intersection.draw_intersection()
        intersection.intersection_step()
        intersection.add_cars(6)
        intersection.draw_intersection()
        intersection.intersection_step()




test = EnvironmentTests()
test.test_env()
test.test_intersection()
