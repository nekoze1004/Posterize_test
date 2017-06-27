'''
Created on 2017/06/27

@author: user
'''
import cv2
import numpy as np

#カラーでポスタライズする関数(元画像,書き出し先,階数)
def PosC(r,w,pos):
    if pos == 1:
        #もし１が入ってきたら、普通の処理では０で割る動作があるので例外的に処理
        for i in range(r.shape[0]):
            for j in range(r.shape[1]):
                for k in range(r.shape[2]):
                    if r[i][j][k]<=127:
                        w[i][j][k]=0
                    else:
                        w[i][j][k]=255
    elif pos>=256:
        #もし256以上が入ってきたら、画像をそっくりそのまま返す
        for i in range(r.shape[0]):
            for j in range(r.shape[1]):
                for k in range(r.shape[2]):
                    w[i][j][k]=r[i][j][k]
    else:
        #2~255までを想定
        #読み込んだ元画像の全画素を巡回して、閾値と比べて当てはまる階級の値を
        #書き出し先の同じ場所の画素に入れていく
        for i in range(r.shape[0]):
            for j in range(r.shape[1]):
                for k in range(r.shape[2]):
                    for p in range(0,pos):
                        #pos=3のとき、0-85,86-170,171-255で分けられる
                        #それぞれ0,127,255が入れられる
                        if(r[i][j][k]>=((255//pos)*p)+1)&(r[i][j][k]<=(255//pos)*(p+1)):
                            w[i][j][k]=(255//(pos-1))*p
                            if p+1==pos:
                                #255//posが本来２５５ぴったしになるといいが、現実は非常なので、２５５になるべき者たちが２５５になれるようにしている（謎の言い回し）
                                if(r[i][j][k]>=(255//pos)*(p+1))&(r[i][j][k]<=255):
                                    w[i][j][k]=255

#グレースケールでポスタライズする関数(元画像,書き出し先,階数)    
def PosG(r,w,pos):
    if pos == 1:
        #もし１が入ってきたら、普通の処理では０で割る動作があるので例外的に処理
        for i in range(r.shape[0]):
            for j in range(r.shape[1]):
                if r[i][j]<=127:
                    w[i][j]=0
                else:
                    w[i][j]=255
    elif pos>=256:
        #もし256以上が入ってきたら、画像をそっくりそのまま返す
        for i in range(r.shape[0]):
            for j in range(r.shape[1]):
                w[i][j]=r[i][j]
    else:
        #2~255までを想定
        #読み込んだ元画像の全画素を巡回して、閾値と比べて当てはまる階級の値を
        #書き出し先の同じ場所の画素に入れていく
        for i in range(r.shape[0]):
            for j in range(r.shape[1]):
                for p in range(0,pos):
                    #pos=3のとき、0-85,86-170,171-255で分けられる
                    #それぞれ0,127,255が入れられる
                    if(r[i][j]>=((255//pos)*p)+1)&(r[i][j]<=(255//pos)*(p+1)):
                        w[i][j]=(255//(pos-1))*p
                        if p+1==pos:
                            #255//posが本来２５５ぴったしになるといいが、現実は非常なので、２５５になるべき者たちが２５５になれるようにしている（謎の言い回し）
                            if(r[i][j]>=(255//pos)*(p+1))&(r[i][j]<=255):
                                w[i][j]=255

#二値画像を反転させる
def reverse(read):
    write=np.copy(read)
    for i in range(read.shape[0]):
        for j in range(read.shape[1]):
            if read[i][j]==0:
                write[i][j]=255
            else:
                write[i][j]=0
    return write

#base画像にmask画像を重ねる mask画像は二値である必要がある
def mask(base,mask):
    for i in range(base.shape[0]):
        for j in range(base.shape[1]):
            if mask[i][j]==0:
                base[i][j]=0
    return base

#CまたはGなのかを判別してTrueかFalseで返す　大文字小文字は関係ない
def IsCorG(str):
    if (len(str) == 1)&((str == "C")|(str == "G")|(str=="c")|(str=="g")):
        return True
    else:
        return False

#Cまたはcであるかを判別してTrueかFalseで返す
def IsC(str):
    if IsCorG:#この先を通りたくば、最低でもCかGであれ　ということ
        if (str=="c")|(str=="C"):
            return True
        else:
            return False
    else:
        return False

#Gまたはgであるかを判別してTrueかFalseで返す    
def IsG(str):
    if IsCorG:#この先を通りたくば、最低でもCかGであれ　ということ
        if (str=="G")|(str=="g"):
            return True
        else:
            return False
    else:
        return False 

#階数が規定の範囲内かどうかを調べてTrueかFalseで返す    
def IsPos(p):
    #今回のプログラムでは、引数として来るものが文字列なので、しっかりとintに変換する
    if (int(p)>0)&(int(p)<256):
        return True
    else:
        return False

#yかYが入力されたらTrueを返す
def IsYes(str):
    if(str=="y")|(str=="Y"):
        return True
    else:
        return False

#入力された文字がおかしいと言って、入力された文字を見せつける
def errMes(inp):
    print("入力された文字列は認識できません")
    print("入力された文字列:"+inp)

if __name__ == '__main__':
    near4=np.array([[0,1,0],
                    [1,1,1],
                    [0,1,0]],
                    np.uint8)
    near8=np.array([[1,1,1],
                    [1,1,1],
                    [1,1,1]],
                    np.uint8)

    print("実行する画像の名前を入力してください")
    inputImg = input(">>> ")
    img = cv2.imread("images/"+inputImg+".png")
    if img is None:#入力されたファイル名のファイルが無い場合、imgはNoneを返す
        errMes(inputImg)
    else:
        print("カラーかグレースケールか選んでください")
        print("カラー:C グレースケール:G")
        CorG = input(">>> ")
        if IsCorG(CorG):
            print("ポスタライズする階調を1~255で入力してください。(推奨:n<20)")#だいたい3,5,7くらいがいい（経験則）
            pos = input(">>> ")
            if IsPos(pos):
                print("実行しています")
                if IsC(CorG):
                                      
                    #画像の下処理
                    GaussImgC=cv2.GaussianBlur(img,(5,5),0)
                    
                    #線を求める
                    while(1):
                        #Canny法を用いて輪郭を検出する
                        sita = input("下の閾値>>> ")
                        ue = input("上の閾値>>> ")
                        CannyGaussImgC=cv2.Canny(GaussImgC,int(sita),int(ue))
                        cv2.imshow("Canny",CannyGaussImgC)
                        cv2.waitKey(0)
                        cv2.destroyAllWindows()
                        #線画像を表示して、確認させる
                        print("よろしいですか？ y/n")
                        i=input(">>> ")
                        if IsYes(i):
                            #Yesならループを出る
                            print("輪郭検出終了")
                            break
                    
                    #線を反転させる
                    ReverseCannyGaussImgC=reverse(CannyGaussImgC)
                    #線を太くする
                    ErosionReverseCannyGaussImgC=cv2.erode(ReverseCannyGaussImgC,near8,iterations=1)
                    
                    #カラーポスタライズ関数に入れる
                    print("ポスタライズしています")
                    PosterizeC=np.copy(GaussImgC)
                    PosC(GaussImgC,PosterizeC,int(pos))
                    
                    #合成する
                    result=mask(PosterizeC,ErosionReverseCannyGaussImgC)                    
                    
                    #名は体を表すファイル名をつける
                    fName=inputImg+"Posterize.png"
                    cv2.imshow("results"+fName,result)#ポスタライズの結果を表示する
                    cv2.imwrite(fName,result)#ポスタライズの結果を保存する
                    cv2.waitKey(0)#なにかキーを押すと↓
                    cv2.destroyAllWindows()#表示ウインドウが閉じる
                    
                elif IsG(CorG):
                    #読み込まれたimgはカラー画像なので、ここでグレースケール化する
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    
                    #画像の下処理
                    GaussImgG=cv2.GaussianBlur(gray,(5,5),0)
                    
                    #線を求める
                    while(1):
                        #Canny法を用いて輪郭を検出する
                        sita = input("下の閾値>>> ")
                        ue = input("上の閾値>>> ")                        
                        CannyGaussImgG=cv2.Canny(GaussImgG,int(sita),int(ue))
                        cv2.imshow("Canny",CannyGaussImgG)
                        cv2.waitKey(0)
                        cv2.destroyAllWindows()
                        #線画像を表示して、確認させる
                        print("よろしいですか？ y/n")
                        i=input(">>> ")
                        if IsYes(i):
                            #Yesならループを出る
                            print("輪郭検出終了")
                            break
                    
                    #線を反転させる
                    ReverseCannyGaussImgG=reverse(CannyGaussImgG)
                    #線を太くする
                    ErosionReverseCannyGaussImgG=cv2.erode(ReverseCannyGaussImgG,near8,iterations=1)
                    
                    #カラーポスタライズ関数に入れる
                    print("ポスタライズしています")
                    PosterizeG=np.copy(GaussImgG)
                    PosG(GaussImgG,PosterizeG,int(pos))
                    
                    #合成する
                    result=mask(PosterizeG,ErosionReverseCannyGaussImgG)                    
                    
                    #名は体を表すファイル名をつける
                    fName=inputImg+"Posterize.png"
                    cv2.imshow("results"+fName,result)#ポスタライズの結果を表示する
                    cv2.imwrite(fName,result)#ポスタライズの結果を保存する
                    cv2.waitKey(0)#なにかキーを押すと↓
                    cv2.destroyAllWindows()#表示ウインドウが閉じる
                    
                else:
                    errMes(CorG)#CかGじゃない文字が入ってるぞ この処理は多分要らないぞ
            else:
                errMes(pos)#1-255以外のものが入ってるぞ
        else:
            errMes(CorG)#CかGじゃない文字が入ってるぞ
    
    print("プログラムは終了しました")#この文字がコマンドラインに出てくると安心感が違う（個人比）
    