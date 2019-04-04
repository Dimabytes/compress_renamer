import os

path = 'for-rename/'
for i in os.listdir(path):
	os.rename(path + i, path + i.replace('-min', ''))