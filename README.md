画像をポスタライズするプログラムの試作<br>
というかPythonとOpenCVを使って画像を弄る練習

例えば
0～255までを3つに割って0～85までは0、86～170までは127、171～255までは255というように色を少なくする<br>
世の中の漫画カメラは大体こんなことをしてるらしい<br><br>
test1.pyがグレースケール画像のみ<br>
Color_test1.pyがカラー画像に対応してみたもの<br>
Posterize.pyはグレースケールとカラーをコマンドラインで選択できるようにしたもの<br>
他のプログラムは輪郭検出、ぼかし、膨張、雑な合成、二値化、トラックバーの試しなど<br>
Posterize_ex1.pyは上記のものを組み合わせて、一連の動作で輪郭を強調してポスタライズするようにしてみたもの<br>
imagesに入っているのがサンプルとして使った画像　スウェーデンのマルチロール戦闘機グリペンの試作1号機の写真
