import numpy as np
import argparse
import matplotlib.pyplot as plt
import os
import time
import io
import collections
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.metrics import accuracy_score as a_score
import pandas as pd
import config.config as cfg

folder = 'answers/'


#dqn_actions = np.load('dataset/scores/action_reward_history.npy')
assets = ['Wait','Look','Wave','Handshake','None']

def parse_arguments():
    parser = argparse.ArgumentParser(description='Process command line arguments.')
    parser.add_argument('-a','--alg',default='greedy')
    return parser.parse_args()
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




def calc(dqn_actions,human_actions):

	size = cfg.validation_size
	human_anwers = np.transpose(human_actions)

	true_label = []
	pred_label = []

	for i in range(size):
		robot = dqn_actions[i]
		if not isinstance(human_anwers[i],np.float64):
			human = collections.Counter(human_anwers[i]).most_common(1)[0][0]
		else: 
			human = human_anwers[i]
		h_index = int(human)
		r_index = int(robot[0])
		true_label.append(h_index)
		pred_label.append(r_index)
	return true_label, pred_label

def Average(lst):
    return sum(lst) / len(lst)

def padronizar(listdf):
	aux_df = [element * 100 for element in listdf]
	aux_df = [ '%.2f%%' % element for element in aux_df ]
	return aux_df

def analytics(human_anwers,dqn_actions,debug=False):



	#wt_acc, lk_acc, wv_acc, hs_acc, geral_acc,true_label,pred_label = calc(dqn_actions)
	true_label,pred_label = calc(dqn_actions,human_anwers)



	y_actu = pd.Series(true_label, name='Actual')
	y_pred = pd.Series(pred_label, name='Predicted')
	confusion_matrix = pd.crosstab(y_actu, y_pred)

	if(debug):
		print(confusion_matrix)
		print('\n')

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
	Recall_Score = TP / (FN + TP)
	F1_Score = 2* Precision_Score * Recall_Score/ (Precision_Score + Recall_Score)
	df_scores = pd.DataFrame(columns = ["Accuracy","Prec.","Recall","Fscore",],index=["Wait","Look","Wave","Handshake","General"])

	aux_df = Accuracy_Score.values.tolist()
	aux_df.append(Accuracy_Score.mean())

	df_scores["Accuracy"] = aux_df#padronizar(aux_df)

	aux_df = Precision_Score.values.tolist()
	aux_df.append(Precision_Score.mean())
	df_scores["Prec."] = aux_df#padronizar(aux_df)

	aux_df = Recall_Score.values.tolist()
	aux_df.append(Recall_Score.mean())
	df_scores["Recall"] = aux_df#padronizar(aux_df)

	aux_df = F1_Score.values.tolist()
	aux_df.append(F1_Score.mean())
	df_scores["Fscore"] = aux_df#padronizar(aux_df)


	return df_scores


def standardize(df):
	for column in df:
	    
		aux_df = [element * 100 for element in df[column]]
		aux_df = [ '%.2f%%' % element for element in aux_df ]
		df[column] = aux_df
	return df


def main():
	arguments = parse_arguments()
	alg = arguments.alg
	size = cfg.validation_size


	#dqn_actions = np.load('mdqn/results2/ep'+str(ep)+'/action_history.npy')
	if(alg=='greedy'):
		dqn_actions = np.load('dataset/scores/100_action_reward_history.npy')
	elif(alg=='noemotion'):
		dqn_actions = np.load('dataset/scores/test_action_reward_history.npy')
	else:
		dqn_actions = np.random.random_integers(0,3, (size, 2)) 
	human_anwers_files = []
	names = []
	for file in os.listdir(folder):
		if file.endswith(".npy"):
			human_anwers_files.append(np.array(np.load(os.path.join(folder, file)))[:size])
			names.append(file)

	human_anwers= np.array(human_anwers_files)
	df_array = []
	for ha,hf  in zip(human_anwers,names):
		print('\n*****************************')
		print(hf)
		print('*****')
		df = analytics(ha,dqn_actions,debug=True)
		print(df.to_string(index=True))
		df_array.append(df.to_numpy())

	print('\n\n*****************************')
	print('Average Scores')
	matrices = np.mean( np.array(df_array), axis=0 )
	df_scores = pd.DataFrame(matrices,columns = ["Accuracy","Prec.","Recall","Fscore",],index=["Wait","Look","Wave","Handshake","General"])
	print(standardize(df_scores))
	print('\n*****************************')
	print('Votation method\n')
	print('#Answers: {}\n'.format(len(human_anwers)))

	df = analytics(human_anwers,dqn_actions)
	print(standardize(df).to_string(index=False))



if __name__ == "__main__":
	main()
