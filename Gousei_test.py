'''
Created on 2017/06/27

@author: user
'''

import cv2
import numpy as np


def gousei(base,mask):
    for i in range(base.shape[0]):
        for j in range(base.shape[1]):
            if mask[i][j]==0:
                base[i][j]=0
    return base

def errMes(inp):
    print("入力された文字列は認識できません")
    print("入力された文字列:"+inp)

if __name__ == '__main__':
    
    print("合成するベース画像の名前を入力してください")
    inputImg = input(">>> ")
    img = cv2.imread("images/"+inputImg+".png",0)
    if img is None:#入力されたファイル名のファイルが無い場合、imgはNoneを返す
        errMes(inputImg)
    else:
        print("合成する画像の名前を入力してください")
        inputImg2 = input(">>> ")
        img2 = cv2.imread("images/"+inputImg2+".png",0)
        if img2 is None:
            errMes(inputImg2)
        else:
            print("start")
            result=gousei(img,img2)
            cv2.imshow("result",result)
            cv2.imwrite("mix_"+inputImg+"_and_"+inputImg2+".png",result)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            