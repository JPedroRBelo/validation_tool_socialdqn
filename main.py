import numpy as np
import PySimpleGUI as sg
from PIL import Image
import os
import time
import io
import config as cfg

#Change this at config.py file
lang = cfg.languages[cfg.lang]


asset = [lang['WAIT'],lang['LOOK'],lang['WAVE'],lang['HANDSHAKE']]
emot_asset = [lang['NOFACE'],lang['NEUTRAL'],lang['POSITIVE'],lang['NEGATIVE']]
dictAssets = dict(zip(asset, range(len(asset))))

n_steps = cfg.validation_size



def get_time():
	return round(time.time() * 1000)

def show_choose_menu(window,flag,exclude=None):
	window.FindElement('-TEXTCHOOSE-').Update(visible=flag)
	window.FindElement('-WAIT-').Update(visible=flag,disabled=False)
	window.FindElement('-LOOK-').Update(visible=flag,disabled=False)
	window.FindElement('-WAVE-').Update(visible=flag,disabled=False)
	window.FindElement('-HAND-').Update(visible=flag,disabled=False)
	if(exclude != None):
		window.FindElement(exclude).Update(disabled= flag)

def clear_radion_selections(window):
	window.FindElement('-YES-').Update(value=False)
	window.FindElement('-NO-').Update(value=False)
	window.FindElement('-WAIT-').Update(value=False)
	window.FindElement('-LOOK-').Update(value=False)
	window.FindElement('-WAVE-').Update(value=False)
	window.FindElement('-HAND-').Update(value=False)


def make_layout(sg):

	panel_file2 = 	[sg.Submit(lang['SAVE'],key="-SAVE-",disabled=False)]
				

	panel_image = sg.Frame(layout=[
				[sg.Text(size=(24,1),key="-NAMEIMAGE-")],
				[sg.Image(size=(640, 480),key="-IMAGE-")]
			], 
			title='DQN State',					 
			relief=sg.RELIEF_SUNKEN)
	layout_column = [
					[sg.Submit(lang['PREV'],size=(12,1),key="-PREV-",disabled=False),
					 sg.Submit(lang['NEXT'],size=(12,1),key="-NEXT-",disabled=False)],

					[sg.Sizer(100, 30)],
					[sg.Text(lang['LOADFILE']),
					sg.FileBrowse(lang['BROWSE'],key="-LOADINPUT-")],
					[sg.Submit(lang['LOAD'],size=(29,1),key="-LOAD-",disabled=False)],
					[sg.Sizer(50, 30)],
					[sg.Text(lang['FILENAME']),
					sg.Input(os.path.join(cfg.save_location,cfg.result_file+cfg.extension),size=(21,1),justification='left', key='-INPUT-')],
					[sg.Submit(lang['SAVE'],size=(29,1),key="-SAVE-",disabled=False)],
	]



	panel_quest = sg.Frame(
				layout=[
					[sg.Text(lang['AVATAREMOTION']),sg.Text("",size=(20,1),key="-HUMANEMOTION-",text_color="white",background_color="blue",justification='c')],
					[sg.Text(lang['DQNSELECTEDACTION']),sg.Text("",size=(20,1),key="-ROBOTACTION-",text_color="white",background_color="green",justification='c')],					
					[sg.Text(lang['DOYOUAGREE'])],
					[sg.Radio(lang['YES'], "RADIOAGREE",key="-YES-", size=(10, 2))],						 
					[sg.Radio(lang['NO'], "RADIOAGREE",key="-NO-")],
					[sg.Text(lang['CHOOSERIGHTACTION'],key='-TEXTCHOOSE-',visible=True)],
					[sg.Radio(lang['WAIT'], "RADIOCHOOSE",key="-WAIT-",visible=True)],						 
					[sg.Radio(lang['LOOK'], "RADIOCHOOSE",key="-LOOK-", visible=True)],
					[sg.Radio(lang['WAVE'], "RADIOCHOOSE",key="-WAVE-", visible=True)],						 
					[sg.Radio(lang['HANDSHAKE'], "RADIOCHOOSE",key="-HAND-", visible=True)],

					[sg.Column(layout_column, element_justification='center')],				
					[sg.Sizer(100, 55)]
				], 

				title=lang['QUESTIONNAIRE'],					 
				relief=sg.RELIEF_SUNKEN,
				)

	panel_help = sg.Frame(
					layout=[
						[sg.Text(lang['ACTIONS'])],
					], 
					title=lang['LABEL'],					 
					relief=sg.RELIEF_SUNKEN,
				)

	panel_emotion_help = sg.Frame(
				layout=[
					[sg.Text(lang['EMOTIONS_HELP'])],
				], 
				title=lang['EMOTION_LABEL'],					 
				relief=sg.RELIEF_SUNKEN,
			)

	panel_file = sg.Frame(
					layout=[
						[sg.Submit(lang['LOAD'],key="-LOAD-",disabled=False),
					 	sg.Submit(lang['SAVE'],key="-SAVE-",disabled=False),
					 	sg.Submit(lang['RESET'],key="-RESET-",disabled=False)],
					],
					title=lang['SAVEPANEL'],					 
					relief=sg.RELIEF_SUNKEN,)

	

	layout = [
		[panel_image, panel_quest],
		[panel_help,panel_emotion_help]
		
	]
	window = sg.Window(lang['APPTITLE'], layout,size=(1024, 768),finalize=True)
	return window

def main():
	sg.theme(cfg.theme)
	actions_ep=np.load(cfg.dqn_files+'/100_action_reward_history.npy')
	emotion_ep=np.load(cfg.dqn_files+'/100_social_signals_history.npy')

	window = make_layout(sg)
	window.bind('<Key-Y>', 'Y')
	window.bind('<Key-y>', 'y')
	window.bind('<Key-N>', 'N')
	window.bind('<Key-n>', 'n')
	window.bind('<Key-1>', '1')
	window.bind('<Key-2>', '2')
	window.bind('<Key-3>', '3')
	window.bind('<Key-4>', '4')
	window.bind('<Key-F5>', 'F5')
	window.bind('<Key-Right>', 'Right')
	window.bind('<Key-Left>', 'Left')


	
	#x = threading.Thread(target=update_window_image, args=(window,))
	#x.start()
	user_actions = np.ones(n_steps)*-1
	last_update_time = get_time()	
	step_image = 1
	index_image = 1
	exit_thread = False

	#file_


	while True:

		event, values = window.read(timeout=cfg.image_update_time)	
		
		if event == "Exit" or event == sg.WIN_CLOSED:
			exit_thread = True
			break

		#if(actions_ep[step_image]==user_actions[step_image] or actions_ep[step_image]==NULL):
		#	window.FindElement('-YES-').Update(value=True)

		#disable NEXT/PREV buttons if nothing is selected
		disabled_buttons = bool((user_actions[step_image-1]==cfg.NULL))

		
		window['-NEXT-'].Update(disabled=disabled_buttons)
		disabled_buttons = bool((user_actions[step_image-1-1]==cfg.NULL))
		window['-PREV-'].Update(disabled=disabled_buttons)

		loadfile_test = os.path.isfile(values['-LOADINPUT-'])
		window['-LOAD-'].Update(disabled=not loadfile_test)

		if event == 'Right':
			window['-NEXT-'].click()
		if event == 'Left':
			window['-PREV-'].click()


		if event == "-PREV-" or event == "-NEXT-" or event == "-LOAD-":
			add = 1

			if event =="-PREV-":
				add = -1
			step_image = ((step_image+add)%(n_steps+1))
			#Verify if index equals to 0
			##True: aditional increment operation
			if(step_image==0):
				step_image = ((step_image+add)%(n_steps+1))
			index_image = 1

			if event == "-LOAD-":
				step_image = 1
				user_actions = np.load(values["-LOADINPUT-"])
			
			if(user_actions[step_image-1]==cfg.NULL):
				clear_radion_selections(window)
				show_choose_menu(window,False)
			elif(actions_ep[step_image-1][0]==user_actions[step_image-1]):
				window.FindElement('-YES-').Update(value=True)
				clear_radion_selections
			else:
				window.FindElement('-NO-').Update(value=True)
				if(user_actions[step_image-1]==dictAssets[lang['WAIT']]):
					window.FindElement('-WAIT-').Update(value=True)
				elif(user_actions[step_image-1]==dictAssets[lang['LOOK']]):
					window.FindElement('-LOOK-').Update(value=True)
				elif(user_actions[step_image-1]==dictAssets[lang['WAVE']]):
					window.FindElement('-WAVE-').Update(value=True)
				elif(user_actions[step_image-1]==dictAssets[lang['HANDSHAKE']]):
					window.FindElement('-HAND-').Update(value=True)
			print(user_actions[step_image-1])
		if event == "-SAVE-":
			file=values['-INPUT-']
			np.save(file, user_actions)

		'''
		if event == 'Y' or event == 'y':
			window.FindElement('-YES-').Update(value=True)
			#user_actions[step_image-1] = int(actions_ep[step_image-1][0])

		if event == 'N' or event == 'n':
			window.FindElement('-NO-').Update(value=True)
		'''

		if values["-YES-"]:
			#handshake index
			user_actions[step_image-1] = int(actions_ep[step_image-1][0])
			
		
		if values["-NO-"]:
			exclude_key = None
			if(actions_ep[step_image-1][0]==dictAssets[lang['WAIT']]):
				exclude_key = '-WAIT-'
			if(actions_ep[step_image-1][0]==dictAssets[lang['LOOK']]):
				exclude_key = '-LOOK-'
			if(actions_ep[step_image-1][0]==dictAssets[lang['WAVE']]):
				exclude_key = '-WAVE-'
			if(actions_ep[step_image-1][0]==dictAssets[lang['HANDSHAKE']]):
				exclude_key = '-HAND-'

			show_choose_menu(window,True,exclude_key)


			if event == '1':
				window.FindElement('-WAIT-').Update(value=True)
			if event == '2':
				window.FindElement('-LOOK-').Update(value=True)
			if event == '3':
				window.FindElement('-WAVE-').Update(value=True)
			if event == '4':
				window.FindElement('-HAND-').Update(value=True)


			if values["-WAIT-"]:
				user_actions[step_image-1] = dictAssets[lang['WAIT']]
			elif values["-LOOK-"]:
				user_actions[step_image-1] = dictAssets[lang['LOOK']]
			elif values["-WAVE-"]:
				user_actions[step_image-1] = dictAssets[lang['WAVE']]
			elif values["-HAND-"]:
				user_actions[step_image-1] = dictAssets[lang['HANDSHAKE']]
			else:
				user_actions[step_image-1] = cfg.NULL
		else:
			show_choose_menu(window,False)
			#handshake index
		
			#user_actions[step_image] =



		#Update image
		elapsed_time = get_time()-last_update_time
		window["-ROBOTACTION-"].update( asset[int(actions_ep[step_image-1][0])])
		window["-HUMANEMOTION-"].update( emot_asset[int(emotion_ep[step_image-1])])

		if(elapsed_time>cfg.image_update_time):
			filename = cfg.image_database+str(step_image)+'_'+str(index_image)+cfg.format_ext
			if os.path.exists(filename):
				
				image = Image.open(filename)
				image = image.resize((640, 480), Image.ANTIALIAS)
				#image.thumbnail((640, 480))
				bio = io.BytesIO()
				image.save(bio, format="PNG")
				window["-IMAGE-"].update(data=bio.getvalue())
				window["-NAMEIMAGE-"].update(lang["STEP"]+' '+str(step_image)+' - '+lang["INDEX"]+' '+str(index_image))
			# apply mod to keep index betw. 0 and 7; sum up 1
			index_image = ((index_image+1)%(cfg.n_images))
			last_update_time = get_time()

		

	window.close()


if __name__ == "__main__":
	main()
