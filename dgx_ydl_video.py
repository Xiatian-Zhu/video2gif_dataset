'''
 This file shows how to download the dataset videos using python
'''
__author__ = 'xzhu'

import youtube_dl
import youtube_dl.utils
import pdb
import csv
import os.path
from os import path
import time
import re
import random


def download_videos():

	# User agent list
	ua_list = ['Mozilla/5.0 (Linux; <Android Version>; <Build Tag etc.>) AppleWebKit/<WebKit Rev> (KHTML, like Gecko) Chrome/<Chrome Rev> Mobile Safari/<WebKit Rev>',
		'Mozilla/5.0 (Linux; <Android Version>; <Build Tag etc.>) AppleWebKit/<WebKit Rev>(KHTML, like Gecko) Chrome/<Chrome Rev> Safari/<WebKit Rev>',
		'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19',
		'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1',
		'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1',
		'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12',
		'Mozilla/5.0 (Linux; U; Android 4.1.1; en-gb; Build/KLP) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30',
		'Mozilla/5.0 (Linux; Android 4.4; Nexus 5 Build/_BuildID_) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36',
		'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36',
		'Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36',
		'Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36',
		'Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36',
		'Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36',
		'Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36',
		'Mozilla/5.0 (Linux; Android 4.4.3; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/47.1.79 like Chrome/47.0.2526.80 Safari/537.36',
		'Mozilla/5.0 (Linux; Android 5.0.2; LG-V410/V41020c Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.1847.118 Safari/537.36',
		'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
		'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
		'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
		'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'
		]

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
		
		dl_count = 0
		ua_idx = 0 # user agent index
		
		for l in lines:
			# Setting env
			if dl_count % 50 == 0:
				# To change user agent
				cur_ua = ua_list[ua_idx%len(ua_list)]
				youtube_dl.utils.std_headers['User-Agent'] = cur_ua
				ua_idx += 1
		
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
				ydl.download([vid_link])
				if path.exists('./train_videos/'+yid+'.mp4'):
					dl_vid_num += 1
					dl_count += 1
					print('\n\n {}-th (all {}/{}) video $$$ downloaded done $$$ \n\n'.format(vid_idx, dl_vid_num, all_vid_num))
					time.sleep(random.randint(5,7))
				else:
					print('\n\n {}-th (all {}/{}) video ^^^ downloaded failed ^^^ \n\n'.format(vid_idx, dl_vid_num, all_vid_num))
					time.sleep(random.randint(3,5))
			except:
				print('\n\n {}-th (all {}/{}) video *** downloaded error *** \n\n'.format(vid_idx, dl_vid_num, all_vid_num))
				time.sleep(random.randint(3,5))
			
				
if __name__=='__main__':
    download_videos()