import gym
import gym_intersection
env = gym.make('Intersection-v0')

for episode in range(100):
  while not done:
    observation, reward, done, information = self.env.step(self.env.action_space.sample())
