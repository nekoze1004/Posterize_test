'''
Created on 2017/06/25

@author: nekoze1004
'''
import cv2
import numpy as np

def errMes(inp):
    print("入力された文字列は認識できません")
    print("入力された文字列:"+inp)

def hanten(read):
    write=np.copy(read)
    for i in range(read.shape[0]):
        for j in range(read.shape[1]):
            if read[i][j]==0:
                write[i][j]=255
            else:
                write[i][j]=0
    return write



if __name__ == '__main__':
    print("実行する画像の名前を入力してください")
    inputImg = input(">>> ")
    img = cv2.imread("images/"+inputImg+".png",0)
    if img is None:#入力されたファイル名のファイルが無い場合、imgはNoneを返す
        errMes(inputImg)
    else:
        print("Start")
        
        near4=np.array([[0,1,0],
                        [1,1,1],
                        [0,1,0]],
                       np.uint8)
        near8=np.array([[1,1,1],
                        [1,1,1],
                        [1,1,1]],
                       np.uint8)
              
        
        
        img_erosion=cv2.erode(img,near8,iterations=1)
        
        cv2.imshow("result",img_erosion)
        cv2.imwrite("boutyou_"+inputImg+".png",img_erosion)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        
        
        
        
        
        
        
        
        
        
        