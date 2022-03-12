import gym
from stable_baselines3 import A2C
from tf_env import TFEnv

env = TFEnv()
env.reset()

model = A2C('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=1)

episodes = 10

for ep in range(episodes):
	obs = env.reset()
	done = False
	while not done:
		action, _states = model.predict(obs)
		obs, rewards, done, info = env.step(action)
		env.render()
		print(rewards)