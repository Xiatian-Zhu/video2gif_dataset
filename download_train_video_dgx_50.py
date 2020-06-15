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
from utils.utils import video_ID_list


def download_videos():

    video_list = video_ID_list()

    video_list.reverse()

    # Stats
    all_vid_num = len(video_list)
    vid_idx = 0
    dl_vid_num = 0
    
    ydl_opts = {
        'outtmpl': './train_videos/%(id)s.%(ext)s'
	}

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:

        for yid in video_list:
            
            vid_idx += 1
            
            # Skip existing videos
            if path.exists('./train_videos/'+yid+'.mp4'):
                print('\n\n {}-th (all {}) video !!! Exist !!! \n\n'.format(vid_idx, all_vid_num))
                continue
        
            # To download a video
            vid_link = 'https://www.youtube.com/watch?v=' + yid
            try:
                ydl.download([vid_link])
                # Check if the video is obtained
                if path.exists('./train_videos/'+yid+'.mp4'):
                    dl_vid_num += 1
                    print('\n {}-th (all {}) $$$ downloaded done $$$ ({} done) \n'.format(vid_idx, all_vid_num, dl_vid_num))
                    if dl_vid_num % 50 == 0: # Stop as crawling every 50 videos
                        time.sleep(random.randint(1200, 2000))
                    else:
                        time.sleep(random.randint(5,20))
                else:
                    print('\n {}-th (all {}) ^^^ downloaded failed ^^^ \n'.format(vid_idx, all_vid_num))
                    time.sleep(random.randint(5, 10))
            except:
                print('\n {}-th (all {}) *** downloaded error *** \n'.format(vid_idx, all_vid_num))
                time.sleep(random.randint(3,5))
			
				
if __name__=='__main__':
    download_videos()