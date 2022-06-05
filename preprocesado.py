from os import walk
from shutil import copyfile
from cv2 import cv2
from pandas import pandas as pd
import os

# tipo = 'maligno'

def preprocess():
    path = 'D:\\CIC\\Matematicas\\Object'
    commitCount = 0
    # f = []
    # dirpath, dirnames, filenames = walk(path)

    print(path)
    dst = 'D:\\CIC\\Matematicas\\HandsDetectection\\Object\\'
    for (dirpath, dirnames, filenames) in walk(path):
        # f.extend(filenames)
        # print(filenames)
        imageCount = 0

        for (index, name) in enumerate(filenames):
            # print(name, index) 
            # elements = name.split('-')
            # zoom = elements[3]
            # num = elements[4]
            # print(dirpath+'\\'+name)
            image = cv2.imread(dirpath+'\\'+name, cv2.IMREAD_UNCHANGED)
            image = cv2.resize(image, (300,300), interpolation = cv2.INTER_AREA)
            # print(name)
            name_without_extension = name.split(".")[0]
            # print(name_without_extension)
            cv2.imwrite(dst+name_without_extension+'.jpg', image)
            imageCount += 1
            if imageCount==2000 or True:
            	command = "git add ."
            	print(command)
            	p_ans = os.popen(command).read()
            	command = 'git commit -m "Upload '+str(commitCount)+'"'
            	print(command)
            	p_ans = os.popen(command).read()
            	commitCount += 1
            	command = "git push"
            	print(command)
            	p_ans = os.popen(command).read()
            	imageCount = 0

            # print('zoom = {} num={}'.format(zoom, num))
            # print(dst+zoom+'x\\maligno\\'+name)
            # copyfile(dirpath+'\\'+name, dst+'\\'+name)

            return

        if imageCount>0:
        	command = "git add ."
        	print(command)
        	# p_ans = os.popen(command).read()
        	command = 'git commit -m "Upload '+str(commitCount)+'"'
        	print(command)
        	# p_ans = os.popen(command).read()
        	commitCount += 1
        	command = "git push"
        	print(command)
        	# p_ans = os.popen(command).read()
        	imageCount = 0

def preTrain():
    path = 'D:\\CIC\\Matematicas\\ReconocedorAlfabeto\\asl_alphabet_train\\asl_alphabet_train'
    df = pd.DataFrame()
    imageNames = []
    classes = []
    # f = []
    # dirpath, dirnames, filenames = walk(path)

    print(path)
    dst = 'D:\\CIC\\Matematicas\\ReconocedorAlfabeto\\vocales'
    for (dirpath, dirnames, filenames) in walk(path):
        # f.extend(filenames)
        # for signal in dirnames:
        
        # print(filenames)
        for (index, name) in enumerate(filenames):
            # print(name) 
            # elements = name.split('-')
            # zoom = elements[3]
            # num = elements[4]
            # print(dirpath+'\\'+name)
            # print('zoom = {} num={}'.format(zoom, num))
            # print(dst+zoom+'x\\maligno\\'+name)
            # copyfile(dirpath+'\\'+name, dst+'\\'+name)
            # imageNames.append(name)
            c = list(name)[0]
            if c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
                # print(name, c)
                imageNames.append(name)
                classes.append(c)
                # copyfile(dirpath+'\\'+name, dst+'\\'+name)



            # gray = cv2.imread(dirpath+'\\'+name, 0)
            # cv2.imwrite(dst+name, gray)
            if index == 2000:
                break

    df['Name'] = imageNames
    df['Class'] = classes
    df.to_csv('D:\\CIC\\Matematicas\\ReconocedorAlfabeto\\vocales\\vocales2000.csv', index=False)
# preTest()
preprocess()
print('Finish!!')
