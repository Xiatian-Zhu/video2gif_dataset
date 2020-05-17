'''
 This file shows how to download the dataset videos using python
 For each video in the test set it
  - randomly scores frames
  - computes the average precision and nMSD
'''
__author__ = 'xzhu'
import pdb
import re
from pytube import YouTube
 

def read_meta():

	f = open('metadata.txt')
	lines = f.readlines()
	lines.pop(0)
	
	pdb.set_trace()
	for l in lines:
		el = re.split(';\t', l)
		yid = el[0]
		# print(el[0])
		
		# To download a video with ID yid
		vid_link = 'https://www.youtube.com/watch?v=' + yid
		# print(vid_link)
		YouTube(vid_link).streams[0].download()


if __name__=='__main__':
    read_meta()