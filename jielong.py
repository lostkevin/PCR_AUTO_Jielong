from listm import yuntop,ptoyun,listma,idicon,yun
from os import path, mkdir, system
from JielongSearch import choiceEval
from Similarity import *
import cv2
import time
from pinyin import charToID, IDtoYun, IDtopin
from PIL import Image
import random
import json
import imagehash
im = cv2.imread('./icons.png')
idToName = {'00000':'ERROR'}
for i in listma:
    if i[0] not in idToName.keys():
        idToName[i[0]] = [i[2]]
    else:
        idToName[i[0]].append(i[2])

def get_single_icon(id_):
    pass
    index = idicon[id_]
    box = (index[0]+5,index[1]+5,index[0]+75,index[1]+75) # 73 * 73, 为了提高精度,减少一些边框像素
    region = im.crop(box)
    return region

def getIcon() -> dict:
    return { tup[0] : im[tup[1][1]+5:tup[1][1] + 72,tup[1][0]+5:tup[1][0] + 72] \
                 for tup in idicon.items() }

def getIconHash() -> dict:
    return { tup[0] : imgHash(tup[1]) for tup in getIcon().items() }

def findMostSimilar(hashDict: dict, hash):
    def findMax(di: dict):
        index = max(di.keys(), key=(lambda k: di[k]))
        return index if di[index] > 0 else None
    return findMax({tup[0] : similarity(tup[1], hash) for tup in hashDict.items()})

def getInput(src) -> dict:
    inputs = {'left':[]}
    img = src[131:521, 279:669]  # 391 * 391
    for i in range(0, 9):
        x = i // 3
        y = i % 3
        inputs['left'].append(img[x * 131:x * 131 + 125, y * 131:y * 131 + 125])
        cv2.imwrite('./tmp/left_%d.jpg' % i, inputs['left'][-1])
    #854 213 1077 437
    img = src[213:437,854:1077]
    cv2.imwrite('./tmp/right.jpg', img)
    inputs['right'] = img
    return inputs

#根据内部ID选择输入
def selectFromImg(id:int, inputs, rush=None) -> dict:
    def select(id, word_candidate):
        for i in word_candidate:
            #若韵母相同
            if charToID(i[0] if i[0] not in yun else i[1]) == id:
                return i
        return None #不匹配返回None
    r_hash = imgHash(inputs['right'])
    r_id = findMostSimilar(di, r_hash)
    if rush:
        nextHead = rush
    else:
        nextHead = select(id, idToName[r_id]) if r_id else None
        r_hash = str(imagehash.phash(Image.fromarray(cv2.cvtColor(inputs['right'], cv2.COLOR_BGR2RGB))))
    if nextHead is None:
        if r_hash in r_dict.keys():
            nextHead = r_dict[r_hash]
        else:
            print('左侧识别失败,请手动输入,输入0退出:')
            nextHead = input()
            r_dict[r_hash] = nextHead

            if nextHead == '0':
                exit(0)
            with open('./dict.json', 'w', encoding='utf-8') as f:
                json.dump(r_dict, f)
                f.close()
    print('right:', nextHead)
    #更新id
    id = charToID(nextHead[-1])
    id_options = [findMostSimilar(di, imgHash(img)) for img in inputs['left']]  # 识别各图像的id
    print('id:', id_options)
    word_candidate = {}
    for i in range(0, len(id_options)):
        res = select(id, idToName[id_options[i]]) if id_options[i] else None
        if res:
            word_candidate[i] = res
    return word_candidate

def toXY(id: int) -> tuple:
    return 339 + (id % 3) * 131, 191 + (id // 3) * 131

def autoSelect(mem:list, options:dict, yun = None):
    candidates = []
    for i in options.keys():
        if options[i] not in mem:
            candidates.append(i)
    if len(candidates) > 0:
        return random.choice(candidates)
    if yun:
        tmp = {options[x]:[0,0]for x in options.keys()}
        sum = 0;
        res = {}
        for i in yun[1]:
            res = choiceEval(yun[0], i)
            for x in options.keys():
                tmp[options[x]][0] += 1
                tmp[options[x]][1] += res[charToID(options[x][-1])] * yun[2][i]
            sum += yun[2][i]
        for i in tmp.keys():
            tmp[i] = tmp[i][1] / tmp[i][0] / sum
        print('各候选词估值:', tmp)
        m = max(tmp, key=lambda x:tmp[x])
        for i in options.keys():
            if options[i] == m:
                return i
    else:
        for i in options.keys():
            tail = IDtopin(charToID(options[i][-1]))
            if tail == 'ei': #美冬线
                return i
        return random.choice(list(options.keys()))

import sys

with open('./history.json', 'r') as f:
    mem = json.load(f)
    f.close()
with open('./dict.json', 'r') as f:
    r_dict = json.load(f)
rush = len(sys.argv) > 1 and sys.argv[1] == 'r'
all_list = {i:[] for i in yun}
targets = {i:[] for i in yun}
for i in listma:
    if i[2] not in mem:
        targets[i[3]].append(i[2]) #计算每个韵待接的词
    all_list[i[3]].append(i[2])
for i in targets.items():
    if len(i[1]) > 0:
        print('%s: ' % yuntop[i[0]], i[1])
tg_yun = {x:len(targets[x]) for x in targets if len(targets[x]) > 0}
weights = {x:len(targets[x]) / len(all_list[x]) for x in tg_yun}
di = getIconHash()
print('请输入第一个词:')
headID = None
word = None
if rush:
    #------------------获取拼音
    headID = charToID(input()[0])
else:
    word = input()
system('adb connect 127.0.0.1:7555')
retry_times = 5
while retry_times > 0:
    system('adb shell screencap /sdcard/screen.png')
    system('adb pull /sdcard/screen.png')
    inputs = getInput(cv2.imread('./screen.png'))
    try:
        print('开始识别')
        res = selectFromImg(headID, inputs, word if rush else None)
        if len(res) == 0:
            raise SystemError
    except SystemError:
        time.sleep(0.7)
        retry_times -= 1
        continue  # 接龙失败,大概率因为识图错误
    print(res)
    choice = autoSelect(mem, res, [IDtoYun(headID), tg_yun, weights] if len(sys.argv) > 2 else None)
    loc = toXY(choice)
    headID = charToID(res[choice][-1])
    print('选择:', res[choice], '已完成: %.2f%%' % ((len(mem) + 1) / len(listma) * 100))
    word = res[choice]
    #降低没成功点击的风险
    system('adb shell input tap %d %d' % (loc[0], loc[1]))
    time.sleep(0.5)
    system('adb shell input tap %d %d' % (loc[0], loc[1]))
    if res[choice] not in mem:
        mem.append(res[choice])
        with open('./history.json', 'w', encoding='utf-8') as f:
            json.dump(mem, f)
            f.close()
    time.sleep(9 if not rush else 0.5)





