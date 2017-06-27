'''
Created on 2017/06/25

@author: nekoze1004
'''
import cv2
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
        print("Start")
        
        Gimg=cv2.GaussianBlur(img,(5,5),0)
        
        sita = input("下の閾値>>> ")
        ue = input("上の閾値>>> ")
        
        result=cv2.Canny(Gimg,int(sita),int(ue))
        
        #cv2.imshow("resurt",result)
        cv2.imwrite("Gaussian_Canny_"+inputImg+"_"+sita+"_"+ue+".png",result)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        print("end")