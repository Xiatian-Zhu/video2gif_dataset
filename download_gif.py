'''
 This file shows how to download the dataset videos using python
 For each video in the test set it
  - randomly scores frames
  - computes the average precision and nMSD
'''
__author__ = 'xzhu'
import pdb
import re
import requests
import os
# from pytube import YouTube
 

def read_meta():

	f = open('metadata.txt')
	lines = f.readlines()
	lines.pop(0)
	
	pdb.set_trace()
	all_gif_num = len(lines)
	gif_idx = 0
	dl_gif_num = 0
	for l in lines:
		gif_idx += 1
	
		el = re.split(';\t', l)
		gid = el[2]
		print(gid)
		uri = el[3]
		print(uri)
		
		gif_file = './gif/' + gid + '.gif'
		try:
			with open(gif_file, 'wb') as f:
				f.write(requests.get(uri).content)
			dl_gif_num += 1
			print('\n\n {}-th (all {}/{}) gif ### downloaded ### \n\n'.format(gif_idx, dl_gif_num, all_gif_num))
			f.close()
		except:
			f.close()
			os.remove(gif_file)
			print('\n\n {}-th (all {}/{}) gif *** unavailable *** \n\n'.format(gif_idx, dl_gif_num, all_gif_num))
			

if __name__=='__main__':
    read_meta()