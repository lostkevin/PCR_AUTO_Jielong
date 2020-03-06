from pypinyin import *
from listm import listma, yuntop, ptoyun, yun

yuntoicron = {}
vName = {}
same = ['ㄓ', 'ㄔ', 'ㄕ', 'ㄖ', 'ㄗ', 'ㄘ', 'ㄙ']
_count = 0
for vn in [item[3] for item in listma]:
    if vn in vName:
        continue
    if not vn in same:
        vName[vn] = _count
    else:
        if not 'same' in vName.keys():
            vName['same'] = _count
        else:
            _count -= 1
    _count += 1

for i in listma:
    y = i[3]
    p = yuntop[y]
    if p in same:
        p = 'same'
    if p not in yuntoicron:
        yuntoicron[p] = [i]
    else:
        yuntoicron[p].append(i)

def charToID(c: str):
    return yunToID(ptoyun[_normalizePinyin(c)] if c not in yun else c)

def IDtoYun(id: int)->str:
    return [i for i in vName.keys()][id] if len(vName.keys()) > 0 else ''

def yunToID(yun: str)-> int:
    return vName['same' if yun in same else yun] if len(vName) > 0 else -1

def IDtopin(id:int)->str:
    return yuntop[IDtoYun(id)] if IDtoYun(id) != 'same' else 'same'

def yuntopin(yun:str)->str:
    return IDtopin(yunToID(yun))
#返回标准的拼音
def _normalizePinyin(text: str):
    xiuzhen = {
        'iu': 'ou', 'uen': 'un', 'ueng':'ong',
        've': 'yue', 'van': 'yuan', 'vn': 'yun', 'iong':'eng'
    }
    same2 = {'zhi': 'jh', 'chi': 'ch', 'shi': 'sh', 'ri': 'r', 'zi': 'z', 'ci': 'c', 'si': 's'}
    tailtext = text[-1]
    if tailtext == '骰':
        return 'ai'
    a = lazy_pinyin(tailtext, Style.FINALS)
    b = lazy_pinyin(tailtext)
    p = same2[b[-1]] if b[-1] in same2 else a[-1]
    if a[-1] in xiuzhen:
        p = xiuzhen[a[-1]]
    return p

