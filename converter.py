import os

dir = "../"

for file in os.listdir(dir):
	if os.path.isfile(dir+file):
		os.system(f'ffmpeg -i {dir+file} -codec copy {file.replace("mkv", "mp4")}')
