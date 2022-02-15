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


validation_size = 150

theme = 'Topanga'
#theme = 'DarkAmber'
#theme = 'DarkRed'
#theme = 'Dark'

NULL = -1
ep = 0
prefix_name = 'gray'
image_dir = 'ep'+str(ep)
format_ext = '.png'



save_location = 'answers'
dqn_files = os.path.join('dataset','scores')
result_file = 'answr'
extension = '.npy'

fullpath = os.path.join(dqn_files,image_dir, prefix_name)
image_database = os.path.join('dataset','images','2', prefix_name)

image_update_time = 100
n_images = 8



pt_br = {
    "DQNSELECTEDACTION": "Ação selecionada pela DQN: ",
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
    "APPTITLE": "Social MDQN - Feramenta de Validação",
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
    "POSITIVE":"Feliz",
    "NEGATIVE":"Triste"
}


en_us = {
    "DQNSELECTEDACTION": "DQN selected Action: ",
    "AVATAREMOTION": "Human Avatar Emotion: ",
    "DOYOUAGREE": "Do you agree with DQN?" ,  
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
    "APPTITLE": "Social MDQN Validation tool",
    "STEP": "Step:",
    "INDEX": "Index: ",
    "LABEL": "Summary",
    "ACTIONS": "Wait:\t\t do nothing.\nLook:\t\t look at person.\nWave:\t\t handwave wave to get attention.\nHandshake:\t try to start a handshaking.",
    "SAVE": "Save",
    "LOAD": "Load",
    "RESET": "Reset",
    "SAVEPANEL": "File",
    "FILENAME": "Save as: ",
    "LOADFILE": "Load file: ",
    "BROWSE": "Browse"
}



languages = {'pt_br':pt_br, 'en_us':en_us}