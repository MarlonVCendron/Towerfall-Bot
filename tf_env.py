import gym
from gym import spaces
import numpy as np
from collections import deque
import cv2

from get_players_positions import get_players_positions
from get_level_layout import get_level_layout
from take_action import take_action, MULTIDISCRETE_NVEC

PREVPOS_LEN = 600

class TFEnv(gym.Env):
    def __init__(self):
        super(TFEnv, self).__init__()

        # 4 pos + 24*32 level = 772
        OBSERVATION_SPACE_SHAPE = (770,)
        # OBSERVATION_SPACE_SHAPE = (2,)

        # self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)
        self.action_space = spaces.MultiDiscrete(MULTIDISCRETE_NVEC)
        self.observation_space = spaces.Box(low=0, high=350, shape=OBSERVATION_SPACE_SHAPE, dtype=np.float32)

    # def show_avg_prev_pos(self, pos):
    #     img = cv2.resize(self.level_layout_matrix*255, (961, 725), interpolation=cv2.INTER_AREA)
    #     img = cv2.circle(img, (int(pos[0]), int(pos[1])), 50, (0, 0, 255), 50)
    #     while True:
    #         cv2.imshow('level', img)
    #         if cv2.waitKey(33) & 0xFF in (ord('q'), 27):
    #             break

    def step(self, action):
        take_action(action)

        self.players_positions = get_players_positions()
        # self.observation = np.concatenate((self.players_positions, self.level_layout))
        self.observation = np.concatenate((self.players_positions[:2], self.level_layout))
        # self.observation = self.players_positions
        # self.observation = self.players_positions[:2]

        self.prev_positions.append(self.players_positions[:2])
        average_prev_positions = np.average(np.array(self.prev_positions), axis=0)
        stagnated_factor = np.linalg.norm(average_prev_positions - self.players_positions[:2])
        # print('                    sf',  500/(stagnated_factor**2))
        # self.show_avg_prev_pos(self.players_positions[:2])

        # self.reward = 5 + (np.linalg.norm(self.players_positions[:2] - self.players_positions[2:]) / -10)
        self.reward = (np.linalg.norm(self.players_positions[:2] - [256, 86]) / -15) - 500/(stagnated_factor**2) 
        # player1x, player1y, *_ = self.players_positions
        # self.reward = 7 + (abs(player1x - 256) / -20) + (abs(player1y - 86) * -3)

        return self.observation, self.reward, self.done, self.info
    def reset(self):
        self.info = {}
        self.done = False
        self.players_positions = get_players_positions()
        self.level_layout = get_level_layout()
        self.level_layout_matrix = get_level_layout(flatten=False)

        self.prev_positions = deque(maxlen=PREVPOS_LEN)
        for _ in range(PREVPOS_LEN):
            self.prev_positions.append([0,0])

        #self.observation = np.concatenate((self.players_positions, self.level_layout))
        self.observation = np.concatenate((self.players_positions[:2], self.level_layout))
        # self.observation = self.players_positions
        # self.observation = self.players_positions[:2]
        return self.observation
    def render(self, mode='human'):
        pass