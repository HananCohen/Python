#!/usr/bin/python
# 
# #############################################################################################
# File name: wiki_backup.py
# Date: 26/10/2016
# Maintainer: Hanan Cohen <hanan.c80@gmail.com>
# Purpose: script used to backup wiki server data folders
#
# Help: requires python 2.7 installed 
#       
# Usage:  change the folders pathes to the correct direcrories with user credentials
#        
#
###########################################################################################

import boto
import subprocess
import datetime
import os
 
 

# Params 

WIKI_PATH = '/path/to/wiki'
BACKUP_PATH = '/path/to/backup/to'
AWS_ACCESS_KEY = 'access key'
AWS_SECRET_KEY = 'secret key'
BUCKET_NAME = 'bucket name'
BUCKET_KEY_PREFIX = 'dokuwiki/'
 
TARGET_DIRS = ['conf', 'data/attic', 'data/media', 'data/meta', 'data/pages']
 
dirs = [WIKI_PATH + '/' + d for d in TARGET_DIRS]
weekday = datetime.datetime.now().strftime('%a')
filename = '{}/wiki-{}.tar'.format(BACKUP_PATH, weekday)
subprocess.call(['tar', '-cvf', filename] + dirs)
subprocess.call(['gzip','-f', filename])
filename += '.gz'
 
s3 = boto.connect_s3(AWS_ACCESS_KEY, AWS_SECRET_KEY)
bucket = s3.get_bucket(BUCKET_NAME)
k = bucket.new_key(BUCKET_KEY_PREFIX + os.path.basename(filename))
k.set_contents_from_filename(filename)
