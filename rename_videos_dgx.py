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

	video_dir = '/home/nfs/datasets/video2gif/train_videos/'
	ydl_opts = {
    'outtmpl': video_dir + '%(id)s.%(ext)s'
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	
		f = open('metadata.txt')
		lines = f.readlines()
		lines.pop(0)
	
		# pdb.set_trace()
		all_vid_num = len(lines)
		vid_idx = 0
		dl_vid_num = 0
		
		# to continue from a break point 43917
		lines = lines[43917:]
		for l in lines:
			vid_idx += 1
	
			el = re.split(';\t', l)
			yid = el[0]
			
# 			if path.exists(video_dir+yid+'.mp4'):
# 				print('\n\n {}-th (all {}) video !!! Exist !!! \n\n'.format(vid_idx, all_vid_num))
# 				continue
		
			try:
				vid_link = 'https://www.youtube.com/watch?v=' + yid
				result = ydl.extract_info(vid_link, download=False)
				vid_fname = video_dir + result['title'] + '.mp4'
				
				if path.exists(vid_fname):
					# rename with ID
					os.rename(vid_fname, video_dir+yid+'.mp4')
					print(yid+'.mp4'+' $$$ renamed $$$')
				else:
					print(yid+'.mp4'+' *** not exists ***')
				
			except:
				print('\n\n {}-th (all {}) video *** ext info failed *** \n\n'.format(vid_idx, all_vid_num))
				
if __name__=='__main__':
    download_videos()