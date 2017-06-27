'''
Created on 2017/06/27

@author: nekoze1004
'''

import cv2
import numpy as np


def hanten(read):
    write=np.copy(read)
    for i in range(read.shape[0]):
        for j in range(read.shape[1]):
            if read[i][j]==0:
                write[i][j]=255
            else:
                write[i][j]=0
    return write

def errMes(inp):
    print("入力された文字列は認識できません")
    print("入力された文字列:"+inp)

if __name__ == '__main__':
    print("実行する画像の名前を入力してください")
    inputImg = input(">>> ")
    img = cv2.imread("images/"+inputImg+".png",0)
    if img is None:#入力されたファイル名のファイルが無い場合、imgはNoneを返す
        errMes(inputImg)
    else:
        print("aaa")
        result=hanten(img)
        cv2.imshow("result",result)
        cv2.imwrite("reverse_"+inputImg+".png",result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        