'''
 This file shows how to count the training videos using python
'''
__author__ = 'xzhu'

import pdb
import re

from os import listdir
from os.path import isfile, join
import glob
import pdb

import csv

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


def video_ID_list():
	f = open('metadata.txt')
	lines = f.readlines()
	lines.pop(0)
	
	vid_dict = {}
	for l in lines:
		el = re.split(';\t', l)
		yid = el[0]
		vid_dict[yid] = 1

	video_list = list(vid_dict.keys())

	return video_list


def download_status():
	dirname = '/home/nfs/datasets/video2gif/train_videos/'
	vfiles = glob.glob(dirname+'*.mp4')

	# pdb.set_trace()
	downloaded_video_list = vfiles.copy()

	for idx in range(len(vfiles)):
		downloaded_video_list[idx] = vfiles[idx][len(dirname):-4]

	print('*** Videos downloaded: {}'.format(len(downloaded_video_list)))

	print(downloaded_video_list[0:2])

	######## All (train) video list ############
	all_video_list = video_ID_list()

	print('*** All videos: {}'.format(len(all_video_list)))

	print(all_video_list[0:2])
	
	######## Undownloaded (train) video list ############
	undownloaded_video_list = list(set(all_video_list) - set(downloaded_video_list))
	
	print('*** Videos to download: {}'.format(len(undownloaded_video_list)))

	######## Write out a csv file #######################
	with open('video2gif_train_left.csv', 'w', newline='') as file:
		writer = csv.writer(file)
		# writer.writerows(nonexist_vid)
		for item in undownloaded_video_list:
			writer.writerow([item])

	with open('video2gif_train_all.csv', 'w', newline='') as file:
		writer = csv.writer(file)
		# writer.writerows(nonexist_vid)
		for item in all_video_list:
			writer.writerow([item])


def overlap_phdd_vid2gif():
	with open('video2gif_train_all.csv', 'r') as file:
		r = csv.reader(file)
		vid2gif_train = []
		for it in r:
			vid2gif_train.append(it[0])
		
		print(vid2gif_train[0:2])

	with open('PHD-GIFs_train_all.csv', 'r') as file:
		r = csv.reader(file)
		phdd_train = []
		for it in r:
			phdd_train.append(it[0])

		print(phdd_train[0:2])

	overlap_list = set(vid2gif_train).intersection(set(phdd_train))
	print(f'o===> Overlap video numer: {len(overlap_list)}')


if __name__=='__main__':
    overlap_phdd_vid2gif()