import numpy as np

import matplotlib.pyplot as plt
import os
import time
import io
import collections
from sklearn.metrics import confusion_matrix

folder = 'answers/'


dqn_actions = np.load('dataset/scores/action_reward_history.npy')
assets = ['Wait','Look','Wave','Handshake','None']


def action(*args):
	actions = []
	for a in args:
		actions.append(assets[int(a)])

	return actions

def action_index(action):
	return assets.index(action)


def accuracy(success,fail):
	if(success+fail):
		return (success/(success+fail))
	else:
		return 0




def calc(dqn_actions):

	c_len = len(assets)
	c_matrix = []
	for i in range(c_len-1):
		aux = []
		for j in range(c_len-1):
			aux.append(0)
		c_matrix.append(aux)

	#an1=np.load(folder+'100_answr500.npy')
	#an2=np.load(folder+'100_answr500.npy')
	#an3=np.load(folder+'100_answr500.npy')
	an1=np.load(folder+'100_answers.npy')
	an2=np.load(folder+'100_answers.npy')
	an3=np.load(folder+'100_answers.npy')
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
	true_label = []
	pred_label = []


	for i,p,j,d in zip(an1,an2,an3,dqn_actions[:len(an1)]):
		robot_action = action(d[0])[0]
		import random
		robot_action =assets[random.randint(0, 3)]

		actions = action(i,p,j)
		most_common = collections.Counter(actions).most_common(1)[0][0]
		
		human = action_index(most_common)
		h_index = int(human)
		r_index = int(d[0])
		#r_index = int(random.randint(0, 3))
		true_label.append(h_index)
		pred_label.append(r_index)
		c_matrix[h_index][r_index] += 1




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

	v_hs_acc.append(accuracy(hs_hit,hs_fail))
	table = ''
	for i in range(len(c_matrix)):
		for j in range(len(c_matrix[i])):
			table += str(c_matrix[j][i])+" "
		table += "\n"





	#print(table) 


	return accuracy(wt_hit,wt_fail),accuracy(lk_hit,lk_fail),accuracy(wv_hit,wv_fail),v_hs_acc[-1],accuracy(hit,fail),true_label,pred_label



def plot_confusion_matrix(df_confusion, title='Confusion matrix', cmap=plt.cm.gray_r):
    plt.matshow(df_confusion, cmap=cmap) # imshow
    #plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(df_confusion.columns))
    plt.xticks(tick_marks, df_confusion.columns, rotation=45)
    plt.yticks(tick_marks, df_confusion.index)
    #plt.tight_layout()
    plt.ylabel(df_confusion.index.name)
    plt.xlabel(df_confusion.columns.name)
    plt.show()
def Average(lst):
    return sum(lst) / len(lst)


def main():
	v_wt = []
	v_lk = []
	v_wv = []
	v_hs = []
	v_geral = []
	for ep in range(1):
		print("Ep: "+str(ep))
		#dqn_actions = np.load('mdqn/results2/ep'+str(ep)+'/action_history.npy')
		dqn_actions = np.load('dataset/scores/100_action_reward_history.npy')
		wt_acc, lk_acc, wv_acc, hs_acc, geral_acc,true_label,pred_label = calc(dqn_actions)
		print("Wait Accuracy:\t\t ",wt_acc)
		print("Look Accuracy:\t\t ",lk_acc)
		print("Wave Accuracy:\t\t ",wv_acc)
		print("Handshake Accuracy:\t ",hs_acc)

		print("General Accuracy:\t",geral_acc)
		print("*********************************************")
		print(wt_acc)
		print(lk_acc)
		print(wv_acc)
		print(hs_acc)
		print(geral_acc)
		print("*********************************************")
		v_wt.append(wt_acc)
		v_lk.append(lk_acc)
		v_wv.append(wv_acc)
		v_hs.append(hs_acc)
		v_geral.append(geral_acc)

		import pandas as pd
		y_actu = pd.Series(true_label, name='Actual')
		y_pred = pd.Series(pred_label, name='Predicted')
		confusion_matrix = pd.crosstab(y_actu, y_pred)
		print(confusion_matrix)
		#df_conf_norm = df_confusion / df_confusion.sum(axis=1)
		#plot_confusion_matrix(df_confusion)
		from sklearn.metrics import precision_recall_fscore_support as score
		from sklearn.metrics import accuracy_score as a_score
		FP = confusion_matrix.sum(axis=0) - np.diag(confusion_matrix)  
		FN = confusion_matrix.sum(axis=1) - np.diag(confusion_matrix)
		TP = np.diag(confusion_matrix)
		TN = confusion_matrix.values.sum() - (FP + FN + TP)
		#print(FP)
		#print(FN)
		#print(TP)
		#print(TN)
		Precision_Score = TP / (FP + TP)
		Accuracy_Score = (TP + TN)/ (TP + FN + TN + FP)

		print('accuracy {}\n accuracy mean {}'.format(Accuracy_Score,Accuracy_Score.mean()))
		print('precision {}\n precision mean {}'.format(Precision_Score,Precision_Score.mean()))
		precision, recall, fscore, support = score(true_label, pred_label)
		accuracy = a_score(true_label,pred_label)
		#print(Accuracy_Score)
		print('accuracy: {}'.format(accuracy))
		print('precision: {}'.format(precision))
		print('recall: {}'.format(recall))
		print('fscore: {} \n Average fscore {}'.format(fscore,Average(fscore)))
		print('support: {}'.format(support))


		#print(c_matrix)	


	plt.ylim([0, 1])
	plt.ylabel('Accuracy')
	plt.xlabel('Epoch')
	plt.plot(v_wt,label='Wait')
	plt.plot(v_lk,label='Look')
	plt.plot(v_wv,label='Wave')
	plt.plot(v_hs,label='Handshake')
	plt.legend()
	#plt.show()





if __name__ == "__main__":
	main()
