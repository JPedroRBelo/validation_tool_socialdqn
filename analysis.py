import numpy as np

import matplotlib.pyplot as plt
import os
import time
import io
import collections

folder = 'answers/'


dqn_actions = np.load('dqn_files/action_history.npy')
assets = ['Wait','Look','Wave','Handshake','None']


def action(*args):
	actions = []
	for a in args:
		actions.append(assets[int(a)])

	return actions

def accuracy(success,fail):
	if(success+fail):
		return (success/(success+fail))
	else:
		return 0




def calc(dqn_actions):
	an1=np.load(folder+'iury.npy')
	an2=np.load(folder+'iury.npy')
	an3=np.load(folder+'iury.npy')
	#an2=np.load(folder+'padula.npy')
	#an3=np.load(folder+'iury.npy')
	an1 = an1[:-1]
	an2 = an2[:-1]
	an3 = an3[:-1]
	hit = 0
	fail = 0
	wt_hit = 0
	wt_fail = 0
	lk_hit = 0
	lk_fail = 0
	wv_hit = 0
	wv_fail = 0
	hs_hit = 0
	hs_fail = 0

	v_hs_acc = []

	for i,p,j,d in zip(an1,an2,an3,dqn_actions[:len(an1)]):
		robot_action = action(d)[0]
		actions = action(i,p,j)
		most_common = collections.Counter(actions).most_common(1)[0][0]
		if(most_common==robot_action):
			hit += 1
		else:
			fail += 1

		if(robot_action=='Wait'):

			if most_common==robot_action:
				wt_hit += 1
			else:
				wt_fail += 1
		if(robot_action=='Look'):

			if most_common==robot_action:
				lk_hit += 1
			else:
				lk_fail += 1

		if(robot_action=='Wave'):

			if most_common==robot_action:
				wv_hit += 1
			else:
				wv_fail += 1
		if(robot_action=='Handshake'):

			if most_common==robot_action:
				hs_hit += 1
			else:
				hs_fail += 1

	print(hs_hit+hs_fail)
	v_hs_acc.append(accuracy(hs_hit,hs_fail))

	return accuracy(wt_hit,wt_fail),accuracy(lk_hit,lk_fail),accuracy(wv_hit,wv_fail),v_hs_acc[-1],accuracy(hit,fail)




def main():
	v_wt = []
	v_lk = []
	v_wv = []
	v_hs = []
	v_geral = []
	for ep in range(1):
		print("Ep: "+str(ep))
		#dqn_actions = np.load('mdqn/results2/ep'+str(ep)+'/action_history.npy')
		dqn_actions = np.load('socialMDQN/action_history.npy')
		wt_acc, lk_acc, wv_acc, hs_acc, geral_acc = calc(dqn_actions)
		print("Wait Accuracy:\t\t ",wt_acc)
		print("Look Accuracy:\t\t ",lk_acc)
		print("Wave Accuracy:\t\t ",wv_acc)
		print("Handshake Accuracy:\t ",hs_acc)

		print("General Accuracy:\t",geral_acc)
		print("*********************************************")
		v_wt.append(wt_acc)
		v_lk.append(lk_acc)
		v_wv.append(wv_acc)
		v_hs.append(hs_acc)
		v_geral.append(geral_acc)


	plt.ylim([0, 1])
	plt.ylabel('Accuracy')
	plt.xlabel('Epoch')
	plt.plot(v_wt,label='Wait')
	plt.plot(v_lk,label='Look')
	plt.plot(v_wv,label='Wave')
	plt.plot(v_hs,label='Handshake')
	plt.legend()
	plt.show()





if __name__ == "__main__":
	main()
