import numpy as np
import torch
import config as cfg
import os


def main():
	filename = os.path.join(cfg.dqn_files,'action_history.dat')
	action_history=torch.load(filename)
	ep_history = action_history[cfg.ep-1]
	filename = os.path.join(cfg.dqn_files,'action_history.npy')
	np.save(filename, ep_history)

if __name__ == "__main__":
	main()
