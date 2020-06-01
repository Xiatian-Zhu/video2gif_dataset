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
         		# We just want to extract the info
				print(result)
				time.sleep(5)
				
				# ydl.download([vid_link])
# 				if path.exists('./train_videos/'+yid+'.mp4'):
# 					dl_vid_num += 1
# 					print('\n\n {}-th (all {}/{}) video $$$ downloaded done $$$ \n\n'.format(vid_idx, dl_vid_num, all_vid_num))
# 				else:
# 					print('\n\n {}-th (all {}/{}) video ^^^ downloaded failed ^^^ \n\n'.format(vid_idx, dl_vid_num, all_vid_num))
			except:
# 				print('\n\n {}-th (all {}/{}) video *** downloaded failed *** \n\n'.format(vid_idx, dl_vid_num, all_vid_num))
			
# 			time.sleep(3)
				
if __name__=='__main__':
    download_videos()