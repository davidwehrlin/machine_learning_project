from gym.envs.registration import register

register(
    id='Intersection-v0',
    entry_point='gym_intersection.envs:IntersecionEnv',
)
