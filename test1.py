'''
Created on 2017/06/15

@author: nekoze1004
'''

import cv2
import numpy as np
#import matplotlib.pyplot as plt

def Posterize(read,write,pos):
    if pos==3:
        for i in range(read.shape[0]):
            for j in range(read.shape[1]):
                if (read[i][j]>=0)&(read[i][j]<=85):
                    write[i][j]=0
                elif (read[i][j]>=86)&(read[i][j]<=170):
                    write[i][j]=127
                elif (read[i][j]>=171)&(read[i][j]<=255):
                    write[i][j]=255
                else:
                    write[i][j]=255
    if pos==4:
        for i in range(read.shape[0]):
            for j in range(read.shape[1]):
                if (read[i][j]>=0)&(read[i][j]<=(255/pos)):
                    write[i][j]=0
                elif (read[i][j]>=(255/pos)+1)&(read[i][j]<=(255/pos)*2):
                    write[i][j]=255/(pos-1)
                elif (read[i][j]>=(255/pos)*2+1)&(read[i][j]<=(255/pos)*3):
                    write[i][j]=(255/(pos-1))*2
                elif (read[i][j]>=(255/pos)*3+1)&(read[i][j]<=255):
                    write[i][j]=255
                #else:
                    #write[i][j]=255
                    
def PosG(r,w,pos):
    if pos == 1:
        for i in range(r.shape[0]):
            for j in range(r.shape[1]):
                if r[i][j]<=127:
                    w[i][j]=0
                else:
                    w[i][j]=255
    elif pos>=256:
        for i in range(r.shape[0]):
            for j in range(r.shape[1]):
                w[i][j]=r[i][j]
    else:
        for i in range(r.shape[0]):
            for j in range(r.shape[1]):
                for p in range(0,pos):
                    if(r[i][j]>=((255//pos)*p)+1)&(r[i][j]<=(255//pos)*(p+1)):
                        w[i][j]=(255//(pos-1))*p
                        if p+1==pos:
                            if(r[i][j]>=(255//pos)*(p+1))&(r[i][j]<=255):
                                w[i][j]=255
                    
                    
                    

if __name__ == '__main__':
    img = cv2.imread('images/img1.jpg',0)
    
    print(img.size)
    print(img.ndim)
    print(img.shape)
    
    #result = np.zeros((img.shape[0],img.shape[1]),np.uint8)
    result2 = np.zeros((img.shape[0],img.shape[1]),np.uint8)
    pos = 17      
    #Posterize(img,result,4)
    PosG(img,result2,pos)
    
    #cv2.imshow('result',result)
    cv2.imshow("result2",result2)
    fName = "pos" + str(pos) + "_.png"
    cv2.imwrite(fName,result2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()