"""
This script runs at background, moves the videos from a specified 
directory to another place such as a remote server.

"""

import time

import os
from os import listdir
from os.path import isfile, join
import glob
import pdb

import pexpect
from pexpect import pxssh

import paramiko


exts = ['.m4a', '.webm', '.mp4', '.mkv']

src_dir = './videos/'


host_ip = '106.1.153.40' # DGX

user_name = 'xiatian.zhu'

user_ip = user_name + '@' + host_ip

des_dir = '/home/nfs/datasets/video2gif/train/'

my_password = 'Samsung99$'


# tempChannel = pexpect.spawn('scp  xiatian.zhu@106.1.153.40:/home/nfs/datasets/video2gif/')
# tempChannel.expect('password:')
# tempChannel.sendline(my_password)


# make sftp connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host_ip, username = user_name, password = my_password, timeout=10)
sftp = ssh.open_sftp()

######################################
while True:

    for ext in exts:
        # Get all the videos of specific format
        vfiles = glob.glob(src_dir + '*' + ext)

        # Upload videos to a remote server
        print(f'>>>>>---> To copy {len(vfiles)} {ext} videos')
        try: 
            for vid in vfiles:
                src_size = os.path.getsize(vid)
                print(f'0===> To upload video {vid}, size: {src_size}')
                
                ########## copy file to the remote server
                # tempChannel = pexpect.spawn('scp ' + vid + ' ' + user_ip + ':' + des_dir)
                # tempChannel.expect('password:')
                # tempChannel.sendline(my_password)
                tgt_path = des_dir + os.path.basename(vid)
                print(f'>>> target file path: {tgt_path}')
                sftp.put(vid, tgt_path)

                ########### Check the size at serve
                info = sftp.stat(tgt_path)
                tgt_size = info.st_size

                ########## Delete the local file
                print(f'>>> target file size: {tgt_size}')
                if tgt_size == src_size:
                    print(f'>>> detele the local video file {vid}\n')
                    os.remove(vid)

                time.sleep(1)
        except FileNotFoundError:
            print(f'FileNotFoundError {vid}')
        except: 
            print(f'Something wrong: {vid}')

        print(f'\n---> Just copied {len(vfiles)} {ext} videos\n')

    # wait for new videos to come in
    time.sleep(360)

