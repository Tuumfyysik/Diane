#!/usr/bin/python3

import os.path, os
from ftplib import FTP
import logging
import datetime
import config as cfg

# FTP settings

host = cfg.ftp['host']
port = cfg.ftp['port']
user = cfg.ftp['user']
passwd = cfg.ftp['passwd']

# Device settings

device = cfg.device['name']
path = cfg.device['path']

# Log settings

#logpath = cfg.log['logpath']

# Connect FTP

ftp = FTP()
ftp.connect(host, port)
ftp.login(user, passwd)

#logging.basicConfig(filename=logpath, level=logging.INFO)

# Move Files

def placefiles(ftp, path):
    for name in os.listdir(path):
        localpath = os.path.join(path, name)
        if os.path.isfile(localpath):
#            logging.info("### File Uploaded ### Date:{} Device:{} Filename:{} Size:{}B  "
#                 .format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), device, name, os.path.getsize(localpath)))
            print("Uploading ->", name, "Size:", os.path.getsize(localpath),"B")
            ftp.storbinary('STOR ' + name, open(localpath, 'rb'))
            os.remove(localpath)  # Delete files

placefiles(ftp, path)

ftp.quit()

print("### All Done ###")
