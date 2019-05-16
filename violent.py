# coding=UTF-8
import zipfile
import threading
import string
import time

flag = True


def extractFile(zipfile, pwd):
    try:
        zipfile.extractall(pwd=str.encode(pwd))
        print('Found password: ' + pwd)
        global flag
        flag = False
    except:
        print("[-] Guessing password: " + pwd + " is wrong!")
        pass


def main():
    zfile = zipfile.ZipFile("group4.zip")
    filePwd = open("dictionary.txt")
    for line in filePwd.readlines():
        pwd = line.strip('\n')
        if flag is True:
            t = threading.Thread(target=extractFile, args=(zfile, pwd))
            t.start()
            t.join()
        if flag is False:
            break


if __name__ == '__main__':
    start = time.clock()
    main()
    end = time.clock()
    print(end - start)
