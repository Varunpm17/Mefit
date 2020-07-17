#!/usr/bin/env python
# -*- coding: utf -*-

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

MIMETYPES = {
        # Drive Document files as MS dox
        'application/vnd.google-apps.document': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        # Drive Sheets files as MS Excel files.
        'application/vnd.google-apps.spreadsheet': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        # Drive presentation as MS pptx
        'application/vnd.google-apps.presentation': 'application/vnd.openxmlformats-officedocument.presentationml.presentation'
        # see https://developers.google.com/drive/v3/web/mime-types
    }
EXTENSTIONS = {
        'application/vnd.google-apps.document': '.docx',
        'application/vnd.google-apps.spreadsheet': '.xlsx',
        'application/vnd.google-apps.presentation': '.pptx'
}

f = open("failed.txt","w+")
folder_id = '1jR4xAsyjRueHfBG4yGpA5P7BSPMq-kaK'
root = 'drive_download'
os.mkdir(root)

def escape_fname(name):
    return name.replace('/','_')

def search_folder(folder_id, root):
    file_list = drive.ListFile({'q': "'%s' in parents and trashed=false" % folder_id}).GetList()
    for file in file_list:
        # print('title: %s, id: %s, kind: %s' % (file['title'], file['id'], file['mimeType']))
        # print(file)
        if file['mimeType'].split('.')[-1] == 'folder':
            foldername = escape_fname(file['title'])
            create_folder(root,foldername)
            search_folder(file['id'], '{}{}/'.format(root,foldername))
        else:
            download_mimetype = None
            filename = escape_fname(file['title'])
            filename = '{}{}'.format(root,filename)
            try:
                print('DOWNLOADING:', filename)
                if file['mimeType'] in MIMETYPES:
                    print("Yes!")
                    download_mimetype = MIMETYPES[file['mimeType']]

                    file.GetContentFile(filename+EXTENSTIONS[file['mimeType']], mimetype=download_mimetype)
                else:
                    file.GetContentFile(filename)
            except:
                print('FAILED')
                f.write(filename+'\n')

def create_folder(path,name):
    os.mkdir('{}{}'.format(path,escape_fname(name)))

search_folder(folder_id,root+'/')
f.close() 

