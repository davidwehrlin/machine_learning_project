#!/usr/bin/env python
# -*- coding: utf-8 -*-

# core modules
import unittest

# 3rd party modules
import gym

# internal modules
import gym_intersection


class Environments(unittest.TestCase):

    def test_env(self):
        env = gym.make('Banana-v0')
        env.reset()
        env.step(0)
