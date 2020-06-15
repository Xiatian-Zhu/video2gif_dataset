'''
 This file shows how to count the training videos using python
'''
__author__ = 'xzhu'

import pdb
import re


def count_train_videos():
	
	f = open('metadata.txt')
	lines = f.readlines()
	lines.pop(0)
	
	vid_dict = {}
	for l in lines:
		el = re.split(';\t', l)
		yid = el[0]
		vid_dict[yid] = 1
		
	print('Train video number:{}'.format(len(vid_dict)))
				
if __name__=='__main__':
    count_train_videos()