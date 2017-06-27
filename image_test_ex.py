'''
Created on 2017/06/19

@author: user
'''

import cv2
import numpy as np
import matplotlib as plt


def colorCut(read,color):
    if (color>=0)&(color<=2):
        print("ccc")
        write=np.zeros((read.shape[0],read.shape[1]),np.uint8)
        for i in range(read.shape[0]):
            for j in range(read.shape[1]):
                write[i][j]=read[i][j][color]
        return write
    else:
        return read

def GtoC(read,color):
    if (color>=0)&(color<=2):
        print("ggg")
        write=np.zeros((read.shape[0],read.shape[1],3),np.uint8)
        for i in range(read.shape[0]):
            for j in range(read.shape[1]):
                write[i][j][color]=read[i][j]
        return write
    else:
        return read
                    



#入力された文字がおかしいと言って、入力された文字を見せつける
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
        GrayB=colorCut(img,0)
        GrayG=colorCut(img,1)
        GrayR=colorCut(img,2)
        ColorR=GtoC(GrayR,2)
        ColorG=GtoC(GrayG,1)
        ColorB=GtoC(GrayB,0)
        cv2.imshow("Image",img)
        cv2.imshow("image_R",ColorR)
        cv2.imshow("Image_G",ColorG)
        cv2.imshow("Image_B",ColorB)
        cv2.waitKey(0)#なにかキーを押すと↓
        cv2.destroyAllWindows()#表示ウインドウが閉じる
        
        