import numpy as np
import torch
import config.config as cfg
import os
import argparse
import os
import torch


database_index = range(38)
dataset = 'dataset'
new_database_name = os.path.join(dataset,'merged')


def get_file_name(index, count,image_index):
	return os.path.join(dataset,str(index),'gray'+str(count)+'_'+str(image_index)+'.png')

def main():
	step = 1
	if(os.path.exists(new_database_name)):
		os.system('rm -rf '+new_database_name)

	os.mkdir(new_database_name)

	new_ep_emotions = []
	new_ep_actions = []
	for i in database_index:

		path_files = os.path.join(dataset,str(i))

		file_ep_actions = os.path.join(path_files,'action_reward_history.dat')
		file_ep_emotions = os.path.join(path_files,'social_signals_history.dat')
		if(os.path.exists(file_ep_actions) and os.path.exists(file_ep_emotions)):
			ep_actions = torch.load(file_ep_actions)
			ep_emotions = torch.load(file_ep_emotions)

			ep_actions = ep_actions[0]
			ep_emotions = ep_emotions[0]
			len_ep = len(ep_actions)
			#image_file = get_file_name(i,count)
			#print(file)

			for j in range(1,len_ep+1):
				new_ep_actions.append(ep_actions[j-1])
				#new_ep_emotions.append(ep_emotions[j-1])

				array = ep_emotions[j-1].cpu().detach().numpy()
				value = array.tolist()[0]
				value = value.index(1)
				new_ep_emotions.append(value)
				#print(image_file)
				#image_file = get_file_name(i,j,image_index)
				#print(image_file)
				#print(step)
				for image_index in range(8):
					new_file_name = os.path.join(new_database_name,'gray'+str(step)+'_'+str(image_index)+'.png')
					old_file_name = get_file_name(i,j,image_index)
					#print(new_file_name)
					os.system("cp "+old_file_name+" "+new_file_name)
				step += 1

	print(len(new_ep_actions))
	np.save(os.path.join(new_database_name,'action_reward_history.npy'),new_ep_actions)
	np.save(os.path.join(new_database_name,'social_signals_history.npy'),new_ep_emotions)



if __name__ == "__main__":
	main()
