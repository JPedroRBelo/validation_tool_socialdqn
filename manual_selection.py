import numpy as np
import PySimpleGUI as sg
from PIL import Image
import os
import time
import io
import config.config as cfg
from utils.face_info import FaceDetection

#Change this at config.py file
lang = cfg.languages[cfg.lang]


asset = [lang['WAIT'],lang['LOOK'],lang['WAVE'],lang['HANDSHAKE']]
emot_asset = [lang['NOFACE'],lang['NEUTRAL'],lang['POSITIVE'],lang['NEGATIVE']]
dictAssets = dict(zip(asset, range(len(asset))))


n_steps = cfg.validation_size

face = FaceDetection()
new_database_name = "selected"

def get_time():
	return round(time.time() * 1000)



def clear_radion_selections(window):
	window['-YES-'].Update(value=False)
	window['-NO-'].Update(value=False)



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
					sg.Input(os.path.join(cfg.save_location,cfg.merge_file+cfg.extension),size=(21,1),justification='left', key='-INPUT-')],
					[sg.Submit(lang['SAVE'],size=(29,1),key="-SAVE-",disabled=False)],
					[sg.Submit('Generate',size=(29,1),key="-GENERATE-",disabled=False)],
	]



	panel_quest = sg.Frame(
				layout=[
					[sg.Text(lang['AVATAREMOTION']),sg.Text("",size=(20,1),key="-HUMANEMOTION-",text_color="white",background_color="blue",justification='c')],
					[sg.Text(lang['DQNSELECTEDACTION']),sg.Text("",size=(20,1),key="-ROBOTACTION-",text_color="white",background_color="green",justification='c')],					
					
					[sg.Radio(lang['YES'], "RADIOAGREE",key="-YES-", size=(10, 2))],						 
					[sg.Radio(lang['NO'], "RADIOAGREE",key="-NO-")],				

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
	emotions = []
	actions_ep=np.load(cfg.dqn_files+'/action_reward_history.npy')
	emotion_ep=np.load(cfg.dqn_files+'/social_signals_history.npy')
	print(emotion_ep)

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

	global n_steps
	n_steps=len(actions_ep)
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

		if event == "-GENERATE-":

			new_folder = os.path.join('dataset',new_database_name)
			if(os.path.exists(new_folder)):
				os.system('rm -rf '+new_folder)
			os.mkdir(new_folder)
			save_index = []	
			new_actions_ep = []
			new_emotion_ep = []
			

			for index in range(len(user_actions)):
				if(user_actions[index]==1):
					save_index.append(index)
			print(len(save_index))		

			count = 0
			for value in save_index:
				count += 1
				new_actions_ep.append(actions_ep[value])
				new_emotion_ep.append(emotion_ep[value])
				for i in range(8):
					new_name = os.path.join(new_folder,'gray'+str(count)+'_'+str(i)+'.png')
					old_name = cfg.image_database+str(value+1)+'_'+str(i)+'.png'
					os.system("cp "+old_name+" "+new_name)

			np.save(os.path.join(new_folder,'action_reward_history.npy'),new_actions_ep)
			np.save(os.path.join(new_folder,'social_signals_history.npy'),new_emotion_ep)
			print("Generated!")
		
		if event == "Exit" or event == sg.WIN_CLOSED:
			exit_thread = True
			break

		#if(actions_ep[step_image]==user_actions[step_image] or actions_ep[step_image]==NULL):
		#	window['-YES-').Update(value=True)

		#disable NEXT/PREV buttons if nothing is selected
		disabled_buttons = bool((user_actions[step_image-1]==cfg.NULL))
		disabled_buttons = False

		
		window['-NEXT-'].Update(disabled=disabled_buttons)
		disabled_buttons = bool((user_actions[step_image-1-1]==cfg.NULL))
		disabled_buttons = False
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
			
			if(user_actions[step_image-1]==1):
				clear_radion_selections(window)
				window['-YES-'].Update(value=True)
			else:
				clear_radion_selections(window)
				window['-NO-'].Update(value=True)

			print(str(step_image)+": "+str(user_actions[step_image-1]))
		if event == "-SAVE-":
			file=values['-INPUT-']
			np.save(file, user_actions)

		'''
		if event == 'Y' or event == 'y':
			window['-YES-').Update(value=True)
			#user_actions[step_image-1] = int(actions_ep[step_image-1][0])

		if event == 'N' or event == 'n':
			window['-NO-').Update(value=True)
		'''

		if values["-YES-"]:
			#handshake index
			user_actions[step_image-1] = 1
			
		
		if values["-NO-"]:
			user_actions[step_image-1] = -1





		#Update image
		elapsed_time = get_time()-last_update_time
		window["-ROBOTACTION-"].update( asset[int(actions_ep[step_image-1][0])])
		window["-HUMANEMOTION-"].update( emot_asset[int(emotion_ep[step_image-1])])
		#if(index_image==0):
		#	emotions = []
		if(elapsed_time>cfg.image_update_time):

			filename = cfg.image_database+str(step_image)+'_'+str(index_image)+cfg.format_ext
			if os.path.exists(filename):

				image = Image.open(filename)
				#emotion = face.recognize_face_emotion(image=image,preprocess='adaptative',save_path='')
				#emotions.append(emotion)
				image = image.resize((640, 480), Image.ANTIALIAS)
				#image.thumbnail((640, 480))
				bio = io.BytesIO()
				image.save(bio, format="PNG")
				window["-IMAGE-"].update(data=bio.getvalue())
				window["-NAMEIMAGE-"].update(lang["STEP"]+' '+str(step_image)+' - '+lang["INDEX"]+' '+str(index_image))
			# apply mod to keep index betw. 0 and 7; sum up 1
			index_image = ((index_image+1)%(cfg.n_images))
			#if(index_image==7):
			#	emotion = face.choose_emotion_by_conf(emotions)
			#	print(emotion)
			last_update_time = get_time()

		

	window.close()


if __name__ == "__main__":
	main()
