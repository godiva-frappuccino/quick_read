import MeCab
import re

def bunsetsuWakachi(text):
    text = text.replace("、", "， ")
    text = text.replace("。", "． ")

    m = MeCab.Tagger('') #mecabのtagger objectの宣言
    m_result = m.parse(text).splitlines()
    m_result = m_result[:-1] #最後の1行は不要な行なので除く
    break_pos = ['名詞','動詞','接頭詞','副詞','感動詞','形容詞','形容動詞','連体詞'] #文節の切れ目を検出するための品詞リスト
    wakachi = [''] #分かち書きのリスト
    afterPrepos = False #接頭詞の直後かどうかのフラグ
    afterSahenNoun = False #サ変接続名詞の直後かどうかのフラグ
    for v in m_result:
        if '\t' not in v: continue
        surface = v.split('\t')[0] #表層系
        pos = v.split('\t')[1].split(',') #品詞など
        pos_detail = ','.join(pos[1:4]) #品詞細分類（各要素の内部がさらに'/'で区切られていることがあるので、','でjoinして、inで判定する)
        #この単語が文節の切れ目とならないかどうかの判定
        noBreak = pos[0] not in break_pos
        noBreak = noBreak or '接尾' in pos_detail
        noBreak = noBreak or (pos[0]=='動詞' and 'サ変接続' in pos_detail)
        noBreak = noBreak or '非自立' in pos_detail #非自立な名詞、動詞を文節の切れ目としたい場合はこの行をコメントアウトする
        noBreak = noBreak or afterPrepos
        noBreak = noBreak or (afterSahenNoun and pos[0]=='動詞' and pos[4]=='サ変・スル')
        if noBreak == False:
            wakachi.append("")
        wakachi[-1] += surface
        afterPrepos = pos[0]=='接頭詞'
        afterSahenNoun = 'サ変接続' in pos_detail
    if wakachi[0] == '': wakachi = wakachi[1:] #最初が空文字のとき削除する
    tmp = list()
    for c in wakachi:
        sp = c.split("，")
        if len(sp) < 2:
            tmp.append(sp[0])
        elif sp[1] == "":
            tmp.append(sp[0]+"，")
        else:
            tmp.append(sp[0]+"，")
            tmp.append(sp[1])
    ret = list()
    for c in tmp:
        sp = c.split("．")
        if len(sp) < 2:
            ret.append(sp[0])
        elif sp[1] == "":
            ret.append(sp[0]+"．")
            ret.append("")
        else:
            ret.append(sp[0]+"．")
            ret.append("")
            ret.append(sp[1])

    return ret
