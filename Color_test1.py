'''
Created on 2017/06/15

@author: nekoze1004
'''
import cv2
import numpy as np

def PosC(r,w,pos):
    if pos == 1:
        for i in range(r.shape[0]):
            for j in range(r.shape[1]):
                for k in range(r.shape[2]):
                    if r[i][j][k]<=127:
                        w[i][j][k]=0
                    else:
                        w[i][j][k]=255
    elif pos>=256:
        for i in range(r.shape[0]):
            for j in range(r.shape[1]):
                for k in range(r.shape[2]):
                    w[i][j][k]=r[i][j][k]
    else:
        for i in range(r.shape[0]):
            for j in range(r.shape[1]):
                for k in range(r.shape[2]):
                    for p in range(0,pos):
                        if(r[i][j][k]>=((255//pos)*p)+1)&(r[i][j][k]<=(255//pos)*(p+1)):
                            w[i][j][k]=(255//(pos-1))*p
                            if p+1==pos:
                                if(r[i][j][k]>=(255//pos)*(p+1))&(r[i][j][k]<=255):
                                    w[i][j][k]=255

if __name__ == '__main__':
    img = cv2.imread('images/img1.jpg')
    
    #resultC = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
    resultC2 = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
    
    print(img.size)
    print(img.ndim)
    print(img.shape)
    print(img[462][699][0])
    
    """for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                if (img[i][j][k]>=0)&(img[i][j][k]<=85):
                    resultC[i][j][k]=0
                elif (img[i][j][k]>=86)&(img[i][j][k]<=170):
                    resultC[i][j][k]=127
                elif (img[i][j][k]>=171)&(img[i][j][k]<=255):
                    resultC[i][j][k]=255
                else:
                    resultC[i][j][k]=255"""
                    
    pos = 5                 
    PosC(img,resultC2,pos)
    
                    
    cv2.imshow("resultC",resultC2)
    fName = "pos" + str(pos) + "C_.png"
    cv2.imwrite(fName,resultC2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()