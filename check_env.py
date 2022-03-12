from stable_baselines3.common.env_checker import check_env
from tf_env import TFEnv

env = TFEnv()
check_env(env)