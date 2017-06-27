'''
Created on 2017/06/20

@author: nekoze1004
'''
import cv2
import numpy as np

def nothing(x):
    pass

def kido(read):
    ki = np.zeros(256)
    for i in range(read.shape[0]):
        for j in range(read.shape[1]):
            ki[read[i][j]]+=1
    return ki

def P(ki,read):
    s=0
    print("対象物の面積の割合を入力")
    pa=input(">>> ")
    for k in range(256):
        s=s+ki[k]
        if s/read.size*100>=int(pa):
            return k
        
def P_tairu(read):
    p=P(kido(read),read)
    print(p)
    r=np.zeros((read.shape[0],read.shape[1]),np.uint8)
    for i in range(read.shape[0]):
        for j in range(read.shape[1]):
            if read[i][j]>=p:
                r[i][j]=255
            else:
                r[i][j]=0
    return r

def P_tairu_P(p,read):
    r=np.zeros((read.shape[0],read.shape[1]),np.uint8)
    for i in range(read.shape[0]):
        for j in range(read.shape[1]):
            print(str(i)+","+str(j))
            if read[i][j]>=p:
                r[i][j]=255
            else:
                r[i][j]=0
    return r

def errMes(inp):
    print("入力された文字列は認識できません")
    print("入力された文字列:"+inp)

if __name__ == '__main__':
    print("実行する画像の名前を入力してください")
    inputImg = input(">>> ")
    img = cv2.imread("images/"+inputImg+".png")
    if img is None:#入力されたファイル名のファイルが無い場合、imgはNoneを返す
        errMes(inputImg)
    else:
        print("aaa")
        gImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #ki=kido(gImg)
        cv2.namedWindow("image")
        cv2.createTrackbar("P","image",0,255,nothing)
        
        r=np.zeros((img.shape[0],img.shape[1]),np.uint8)
        while(1):
            bo=input(">>> ")
            
            cv2.imshow("image",r)
            print("sss")
            
            print("p")
            p=cv2.getTrackbarPos("P","image")
            r=P_tairu_P(int(p),gImg)
            print("qq")
            
        cv2.destroyAllWindows()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        