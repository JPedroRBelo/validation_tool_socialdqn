import numpy as np
import torch
import config as cfg
import os



def convert(file):
	filename = os.path.join(cfg.dqn_files,file)
	action_history=torch.load(filename)
	ep_history = action_history[cfg.ep-1]
	filename = os.path.join(cfg.dqn_files,file.replace('.dat','.npy'))
	np.save(filename, ep_history)

def convert_one_hot_tensor(file):
	filename = os.path.join(cfg.dqn_files,file)
	history=torch.load(filename)
	aux = []
	for h in history[0]:
		array = h.cpu().detach().numpy()
		value = array.tolist()[0]
		value = value.index(1)
		aux.append(value)

	#ep_history = action_history[cfg.ep-1]
	filename = os.path.join(cfg.dqn_files,file.replace('.dat','.npy'))
	print(aux)
	np.save(filename, aux)


def main():
	convert('action_reward_history.dat')
	convert_one_hot_tensor('social_signals_history.dat')

if __name__ == "__main__":
	main()
