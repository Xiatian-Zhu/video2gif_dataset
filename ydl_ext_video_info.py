'''
 This file shows how to download the dataset videos using python
'''
__author__ = 'xzhu'

import youtube_dl
import pdb
import csv
import os.path
from os import path
import time
import re
import pdb
import os


def download_videos():

	ydl_opts = {
    'outtmpl': './train_videos/%(id)s.%(ext)s'
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	
		f = open('metadata.txt')
		lines = f.readlines()
		lines.pop(0)
	
		# pdb.set_trace()
		all_vid_num = len(lines)
		vid_idx = 0
		dl_vid_num = 0
		for l in lines:
			vid_idx += 1
	
			el = re.split(';\t', l)
			yid = el[0]
			# print(el[0])
			
			if path.exists('./train_videos/'+yid+'.mp4'):
				print('\n\n {}-th (all {}) video !!! Exist !!! \n\n'.format(vid_idx, all_vid_num))
				continue
		
			# To download a video with ID yid
			vid_link = 'https://www.youtube.com/watch?v=' + yid
			# print(vid_link)
			try:
				result = ydl.extract_info(vid_link, download=False)
				vid_fname = result['title'] + '.mp4'
				
				if path.exists(vid_fname):
					# rename with ID
					os.rename(vid_fname, yid+'.mp4')
			except:
				print('\n\n {}-th (all {}) video *** ext info failed *** \n\n'.format(vid_idx, all_vid_num))
				
if __name__=='__main__':
    download_videos()