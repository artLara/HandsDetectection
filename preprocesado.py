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
            if imageCount==2000:
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

            # return

        if imageCount>0:
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

def predataset():
    path = 'D:\\CIC\\Matematicas\\HandsDetectection\\'
    df = pd.read_csv(path+'dataset.csv')
    
    df['xmin'] = df['x']//2
    df['ymin'] = df['y']//2
    df['xmax'] = df['xmin'] + df['w']//2
    df['ymax'] = df['ymin'] + df['h']//2
    df["object_exist"].replace({1: "hand", 0: "not hand"}, inplace=True)
    columns = list(df)
    name=[]
    # df = df.reset_index()  # make sure indexes pair with number of rows
    for index, row in df.iterrows():
    	spl = row['path'].split(".")[0]
    	name.append(spl + '.jpg')
    	# row['path'] = spl + '.jpg'
    	# print(name)
    	# break

    # for i in columns[0]:
    # 	spl = i.split(".")[0]
    # 	name.append(spl + '.jpg')
    # 	print(i)
    	# break
    df['path'] = name
    df.drop('x', inplace=True, axis=1)
    df.drop('y', inplace=True, axis=1)
    df.drop('w', inplace=True, axis=1)
    df.drop('h', inplace=True, axis=1)

    df.drop(df[df.object_exist == "not hand"].index, inplace=True)
    df.rename(columns={'path': 'filename', 'object_exist': 'class'}, inplace=True)
    df.to_csv(path+'just_hands.csv', index=False)
# preTest()
predataset()
print('Finish!!')
