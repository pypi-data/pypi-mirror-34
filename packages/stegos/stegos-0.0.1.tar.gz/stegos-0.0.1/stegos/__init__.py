#!/usr/bin/env python3
import os
import wget

def createFolder():
    try:
        os.mkdir('img')
    except FileExistsError:
        print('Folder already exists!')


def urlImg(url):
    createFolder()
    wget.download(url,out='img')


def readFile(file_name):
    try:
        with open(file_name, 'rb') as r:
            byte = r.read(1)
            k = 0
            while byte:
                byte = r.read(1)
                k+=1
    except FileNotFoundError:
        print('\n[x] File: "' + str(file_name)+'" is not defined!')

    else:
        print('[+] Number of bytes in the "'+str(file_name)+'" '+str(k))


def hideMsg(file_name,msg):
    try:
        with open(file_name, 'ab') as file:
            file.write(msg.encode('utf-8'))

    except FileNotFoundError:
        print('\n[x] File: "' + str(file_name)+'" is not defined!')

    else:
        print('[+] File: "'+str(file_name)+'" successfully overwritten!')

def hideArh(file_name,arh_name):
    try:
        with open(file_name,'rb') as file:
            read = file.read()
    except FileNotFoundError:
            print('\n[x] File: "' + str(file_name)+'" is not defined!')

    try:
        with open(arh_name, 'rb') as file_two:
            read_two_file = file_two.read()
    except FileNotFoundError:
            print('\n[x] File: "' + str(arh_name)+'" is not defined!')

    with open(file_name, 'wb') as file_three:
        file_three.write(read)
        file_three.write(read_two_file)
        print('[+] File: "'+str(file_name)+'" successfully overwritten!')
