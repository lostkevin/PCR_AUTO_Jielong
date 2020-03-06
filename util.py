import json
def convert(filepath: str, targetFile: str):
    l = []
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)['data']
        for i in data:
            if 'clicked' in i.keys() and i['clicked']:
                l.append(i['name'])
        f.close()
    with open(targetFile, 'w', encoding='utf-8') as f:
        json.dump(l, f)
        f.close()

convert('./PCR_TW_JIELONG/clicked.json', './history.json')