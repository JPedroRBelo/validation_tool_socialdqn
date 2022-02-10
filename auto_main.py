import numpy as np
import os
from pathlib import Path
import shutil
from torchToNumpy import main as ttn
from main import main as execute
from time import sleep 
def erase_folder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            error('Failed to delete %s. Reason: %s' % (file_path, e))

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def main():


	dqn_folder = os.path.join(str(Path.home()),'SocialDQN')
	scores_folder = os.path.join(dqn_folder,'scores')
	images_folder = os.path.join(dqn_folder,'images')


	erase_folder(os.path.join('dataset','scores'))
	erase_folder(os.path.join('dataset','images'))
	shutil.copytree(scores_folder,os.path.join('dataset','scores'), dirs_exist_ok=True)
	shutil.copytree(images_folder,os.path.join('dataset','images'), dirs_exist_ok=True)
	
	ttn()
	sleep(5)
	execute()


if __name__ == "__main__":
	main()
