import gym
from gym import spaces
import numpy as np
from get_players_positions import get_players_positions
from get_level_layout import get_level_layout
from take_action import take_action, N_DISCRETE_ACTIONS

class TFEnv(gym.Env):
    """Custom Environment that follows gym interface"""

    def __init__(self):
        super(TFEnv, self).__init__()

        # 4 pos + 24*32 level
        OBSERVATION_SPACE_SHAPE = (772,)

        self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)
        self.observation_space = spaces.Box(low=0, high=350, shape=OBSERVATION_SPACE_SHAPE, dtype=np.float32)

    def step(self, action):
        take_action(action)

        self.players_positions = get_players_positions()
        self.observation = np.concatenate((self.players_positions, self.level_layout))

        self.reward = 5 + (np.linalg.norm(self.players_positions[:2] - self.players_positions[2:]) / -10)

        self.info = {}
        return self.observation, self.reward, self.done, self.info
    def reset(self):
        self.done = False
        self.players_positions = get_players_positions()
        self.level_layout = get_level_layout()

        self.observation = np.concatenate((self.players_positions, self.level_layout))
        return self.observation
    def render(self, mode='human'):
        pass