import numpy as np
import torch
import config.config as cfg
import os





def main():
	array = np.load('answers/merge1.npy')
	for i in range(len(array)):
		print(str(i)+": "+str(array[i]))

if __name__ == "__main__":
	main()
