# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.2
#   kernelspec:
#     display_name: xaqlab
#     language: python
#     name: python3
# ---

# %%
# %load_ext autoreload
# %autoreload 2

from my_package import moo
from matplotlib import pyplot as plt
import numpy as np
import torch
import gymnasium as gym
from stable_baselines3 import A2C

# %% [markdown]
# # Test your custom package

# %%
moo("Hello, world!")

# %% [markdown]
# # Test Numpy and Matplotlib

# %%
plt.plot(np.array([1, 2, 3, 4]))
plt.ylabel("some numbers")
plt.show()

# %% [markdown]
# # Test PyTorch

# %%
print("Is CUDA available?", torch.cuda.is_available())

x = torch.rand(5, 3)
print(x)

# %% [markdown]
# # Testing Stable-Baselines

# %%
env = gym.make("CartPole-v1", render_mode="rgb_array")

model = A2C("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=100)

vec_env = model.get_env()
obs = vec_env.reset()
for i in range(2):
    action, _state = model.predict(obs, deterministic=True)
    obs, reward, done, info = vec_env.step(action)
