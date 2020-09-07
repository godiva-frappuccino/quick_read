# What's this?
文章を読む際，眼球を動かすのに時間がかかる為，同じ箇所に文字を表示させれば良いのでは？という考え．
参考> https://twitter.com/tdualdir/status/1302802673222127622
ひとまずread.txtに書いた文章を改行区切りで0.5秒ごとに切り替えて表示します．

# How to Use
## 1. 実行環境
ちゃんと検証してないです，（Python3で以下のパッケージが入っていれば動きそう．）
* Python3.6~
* OpenCV3.x~
* PIL
* numpy
* MeCab
*chardet

## 2. fontの追加
.ttfファイルをネットで探して，/quick_readディレクトリ上にfont.ttfというファイル名で追加してください．
日本語を使いたい場合は感じ対応のフォントを追加で．
demoはこちら( https://fontfree.me/2848 )のコーポレート明朝をダウンロードして使用しています．

## 3. 実行
以下のコマンドで実行されます．
```
python main.py read.txt 0.3
```
read.txtのテキストを分かち書きして文節ごとに0.3秒間表示します．
