import os
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

answer_default_folder = 'mdqn'

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

image_ep='mdqn100'

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



pt_br = {
    "DQNSELECTEDACTION": "Ação selecionada pelo Robô: ",
    "AVATAREMOTION": "Emoção humana: ",
    "DOYOUAGREE": "Esta ação é aceitável no cenário apresentado?",    
    "YES" : "Sim",
    "NO" : "Não",
    "CHOOSERIGHTACTION": "Selecione a ação adequada: ",
    "WAIT": "Esperar",
    "LOOK": "Olhar",
    "WAVE": "Acenar",
    "HANDSHAKE":"Cumprimentar",
    "PREV": "Voltar",
    "NEXT": "Próximo",
    "QUESTIONNAIRE":"Questionário",
    "APPTITLE": "SocialDQN - Feramenta de Validação",
    "STEP": "Interação: ",
    "INDEX": "Índice: ",
    "LABEL": "Resumo",
    "EMOTION_LABEL": "Probabilidade do humano interagir",
    "ACTIONS": "Esperar:\t\t não faz nada, olha para direção aleatória.\nOlhar:\t\t olhar ou procurar por um pessoa.\nAcenar:\t\t acena com a mão para pessoa mais próxima.\nCumprimentar:\t tenta cumprimentar com um aperto de mão.",
    "EMOTIONS_HELP": "Feliz: alta probabilidade de interação\nTriste: pouca probabilidade de interação.\nNeutra: Probabilidade de interação média. \nDesconhecida: humano não presente na cena ou rosto não visível.",
    "FILENAME": "Salvar como: ",
    "SAVE": "Salvar",
    "LOAD": "Carregar",
    "RESET": "Recomeçar",
    "SAVEPANEL": "Arquivo",
    "LOADFILE": "Carregar Arquivo: ",
    "BROWSE": "Procurar",
    "NOFACE": "Desconhecida",
    "NEUTRAL":"Neutra",
    "POSITIVE":"Positiva",
    "NEGATIVE":"Negativa"
}


en_us = {
    "DQNSELECTEDACTION": "Robot selected Action:",
    "AVATAREMOTION": "Human Emotion:         ",
    "DOYOUAGREE": "Is this action acceptable in this scenario?" ,  
    "YES" : "Yes",
    "NO" : "No",    
    "CHOOSERIGHTACTION": "Choose the right Action",
    "WAIT": "Wait",
    "LOOK": "Look",
    "WAVE": "Wave",
    "HANDSHAKE":"Handshake",
    "PREV": "Prev.",
    "NEXT": "Next",
    "QUESTIONNAIRE":"Questionnaire",
    "APPTITLE": "SocialDQN Validation tool",
    "STEP": "Step:",
    "INDEX": "Index: ",
    "LABEL": "Summary",
    "EMOTION_LABEL": "Probability of human interacting",
    "ACTIONS": "Wait:\t\t does nothing, looks in a random direction.\nLook:\t\t look or look for a person.\nWave:\t\t waves your hand to the nearest person. \nHandshake:\t tries to greet with a handshake.",
    "EMOTIONS_HELP": "Happy: high probability of interaction\nSad: low probability of interaction.\nNeutral: Medium probability of interaction. \nUnknown: human not present in scene or face not visible.","SAVE": "Save",
    "SAVE": "Save",
    "LOAD": "Load",
    "RESET": "Reset",
    "SAVEPANEL": "File",
    "FILENAME": "Save as: ",
    "LOADFILE": "Load file: ",
    "BROWSE": "Browse",    
    "NOFACE": "Unknown",
    "NEUTRAL":"Neutral",
    "POSITIVE":"Happy",
    "NEGATIVE":"Sad"
}



languages = {'pt_br':pt_br, 'en_us':en_us}