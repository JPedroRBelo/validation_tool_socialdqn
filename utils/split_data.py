import numpy as np

import matplotlib.pyplot as plt
import os
import time
import io
import collections
from sklearn.metrics import confusion_matrix
import random
import config as cfg


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

lenn = cfg.validation_size
factor = lenn/100

probs = [0.1008*factor,0.3246*factor,0.1968*factor,0.5319*factor]

def calc(dqn_actions):

    while(True):
        actions_ep=np.load(cfg.dqn_files+'/action_reward_history.npy')
        emotion_ep=np.load(cfg.dqn_files+'/social_signals_history.npy')
        an1=np.load(folder+'answr500.npy')   
        an1 = an1[:-1]
        selected = []
        new_action_reward = []
        new_emotion_ep = []
        new_human_answer = []
        new_images = []
        for i in range(len(an1)):
            robot_action = int(dqn_actions[i][0])
            human_action = int(an1[i])
            #import random
            #robot_action =assets[random.randint(0, 3)]
            value = random.random()
            rand = random.random()
            aux = -1
            if(value>0.5):
                if(rand<=probs[robot_action]):
                    aux = i
            else:
                if(rand<=probs[human_action]):
                    aux = i

            if(aux>=0):
                selected.append(aux)

        if(len(selected)>=lenn):
            break



            #h_index = int(human)
            #r_index = int(d[0])

    print(len(selected))
    ans = input("Confirm? ")
    if(ans=="y"):
        for i in range(min(lenn,len(selected))):
            index = selected[i]
            new_action_reward.append(actions_ep[index])
            new_emotion_ep.append(emotion_ep[index])
            new_human_answer.append(an1[index])
            image_database = os.path.join('dataset','images','2')  
            if not os.path.exists(image_database):
                os.makedirs(image_database)
            for j in range(cfg.n_images):
                import shutil

                #make a copy of the invoice to work with
                src=os.path.join('dataset','images','1',cfg.prefix_name+str(index+1)+"_"+str(j)+cfg.format_ext)
                dst=os.path.join(image_database,cfg.prefix_name+str(i+1)+"_"+str(j)+cfg.format_ext)
                shutil.copy(src,dst)
        np.save('dataset/scores/100_action_reward_history.npy',new_action_reward)
        np.save('dataset/scores/100_social_signals_history.npy',new_emotion_ep)
        np.save('answers/100_answers.npy',new_human_answer)

        print(len(new_human_answer))


    else:
        print("Canceled")  








def main():

    #dqn_actions = np.load('mdqn/results2/ep'+str(ep)+'/action_history.npy')
    dqn_actions = np.load('dataset/scores/action_reward_history.npy')
    calc(dqn_actions)






if __name__ == "__main__":
    main()
