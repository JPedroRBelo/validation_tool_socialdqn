import os
import config.config as cfg
lang = 'pt_br'
#lang = 'en_us'



themes = [
'Black',
'TealMono',
'TanBlue',
'LightGreen1',
'LightGreen2',
'LightGreen3',
'LightGreen4',
'DarkBlue15',
'Tan',
'SystemDefault',
'LightBlue5',
'LightBrown',
'DarkPurple',
'DarkGreen',
'LightPurple',
'LightGrey',
'Green',
'Dark',
'BrownBlue',
'BrightColors',
'BlueMono',
'BluePurple',
'DarkRed',
'DarkBlack',
'Topanga']

answer_default_folder = 'socialdqn'

validation_size = 100

theme = 'Topanga'
#theme = 'DarkAmber'
#theme = 'DarkRed'
#theme = 'Dark'

NULL = -1
ep = 0
prefix_name = 'gray'
image_dir = 'ep'+str(ep)
format_ext = '.png'
mode = 'experiment'
result_file = 'answr'
merge_file = 'merge'
extension = '.npy'

#Real
#image_ep='selected0830'

image_ep='socialdqn'

#image_ep = 'selected0730'



#Treino parametros originais, probabilidades antigas
#image_ep = 'selected0830'


save_location = os.path.join('answers',answer_default_folder)
if(mode =='experiment'):    
    dqn_files = os.path.join('dataset',image_ep)
    fullpath = os.path.join(dqn_files, prefix_name)
    image_database = os.path.join('dataset',image_ep,prefix_name)
else:
    dqn_files = os.path.join('dataset','scores')
    fullpath = os.path.join(dqn_files,image_dir, prefix_name)
    image_database = os.path.join('dataset','images','2', prefix_name)



#image_databese = os.path.join('dataset','13',)

image_update_time = 100
n_images = 8



pt_br = cfg.pt_br

en_us = cfg.en_us
languages = cfg.languages