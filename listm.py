yuntop = {'ㄅ': 'b', 'ㄆ': 'p', 'ㄇ': 'm', 'ㄈ': 'f', 'ㄉ': 'd', 'ㄊ': 't',
'ㄋ': 'n', 'ㄌ': 'l', 'ㄍ': 'g', 'ㄎ': 'k', 'ㄏ': 'h', 'ㄐ': 'ji',
 'ㄑ': 'ci', 'ㄒ': 'si', 'ㄓ': 'jh', 'ㄔ': 'ch', 'ㄕ': 'sh', 'ㄖ': 'r',
  'ㄗ': 'z', 'ㄘ': 'c', 'ㄙ': 's', 'ㄧ': 'i', 'ㄨ': 'u', 'ㄩ': 'v', 'ㄚ': 'a',
   'ㄛ': 'o', 'ㄜ': 'e', 'ㄝ': 'e', 'ㄞ': 'ai', 'ㄟ': 'ei', 'ㄠ': 'ao', 'ㄡ': 'ou',
    'ㄢ': 'an', 'ㄣ': 'en', 'ㄤ': 'ang', 'ㄥ': 'eng', 'ㄦ': 'er',
     'ㄧㄚ': 'ia', 'ㄧㄛ': '', 'ㄧㄝ': 'ie', 'ㄧㄞ': 'yai', 'ㄧㄠ': 'iao',
      'ㄧㄡ': 'iou', 'ㄧㄢ': 'ian', 'ㄧㄣ': 'in', 'ㄧㄤ': 'iang', 'ㄧㄥ': 'ing',
       'ㄨㄚ': 'ua', 'ㄨㄛ': 'uo', 'ㄨㄞ': 'uai', 'ㄨㄟ': 'uei', 'ㄨㄢ': 'uan', 
       'ㄨㄣ': 'un', 'ㄨㄤ': 'uang', 'ㄨㄥ': 'ong', 'ㄩㄝ': 'yue', 'ㄩㄢ': 'yuan', 
       'ㄩㄣ': 'yun', 'ㄩㄥ': 'yong'}
yun = list(yuntop.keys())
ptoyun = {'b': 'ㄅ', 'p': 'ㄆ', 'm': 'ㄇ', 'f': 'ㄈ', 'd': 'ㄉ', 't': 'ㄊ',
 'n': 'ㄋ', 'l': 'ㄌ', 'g': 'ㄍ', 'k': 'ㄎ', 'h': 'ㄏ', 'ji': 'ㄐ', 'ci': 'ㄑ', 
 'si': 'ㄒ', 'jh': 'ㄓ', 'ch': 'ㄔ', 'sh': 'ㄕ', 'r': 'ㄖ', 'z': 'ㄗ', 'c': 'ㄘ',
  's': 'ㄙ', 'i': 'ㄧ', 'v': 'ㄩ','u': 'ㄨ', 'a': 'ㄚ', 'o': 'ㄛ', 'e': 'ㄜ', 'ai': 'ㄞ',
  'ei': 'ㄟ', 'ao': 'ㄠ', 'ou': 'ㄡ', 'an': 'ㄢ', 'en': 'ㄣ', 'ang': 'ㄤ', 
  'eng': 'ㄥ', 'er': 'ㄦ', 'ia': 'ㄧㄚ', 'io': 'ㄧㄛ', 'ie': 'ㄧㄝ', 'yai': 'ㄧㄞ',
  'iao': 'ㄧㄠ', 'iou': 'ㄧㄡ', 'ian': 'ㄧㄢ', 'in': 'ㄧㄣ', 'iang': 'ㄧㄤ',
   'ing': 'ㄧㄥ', 'ua': 'ㄨㄚ', 'uo': 'ㄨㄛ', 'uai': 'ㄨㄞ', 'uei': 'ㄨㄟ', 'uan': 'ㄨㄢ', 
   'un': 'ㄨㄣ', 'uang': 'ㄨㄤ', 'ong': 'ㄨㄥ', 'yue': 'ㄩㄝ', 'yuan': 'ㄩㄢ', 'yun': 'ㄩㄣ', 'yong': 'ㄩㄥ'}

idicon = {
    '10001': (648, 620) ,
'10002': (729, 620) ,
'10003': (810, 620) ,
'10004': (891, 620) ,
'10005': (405, 539) ,
'10006': (405, 458) ,
'10007': (405, 296) ,
'10008': (729, 539) ,
'10009': (405, 215) ,
'10010': (405, 134) ,
'10011': (405, 53) ,
'10012': (486, 539) ,
'10013': (567, 539) ,
'10014': (648, 539) ,
'10015': (567, 620) ,
'10016': (405, 377) ,
'10017': (486, 620) ,
'10018': (891, 701) ,
'10019': (648, 701) ,
'10020': (729, 701) ,
'10021': (810, 701) ,
'10022': (405, 701) ,
'10023': (486, 701) ,
'10024': (567, 701) ,
'10025': (324, 620) ,
'10026': (324, 53) ,
'10027': (324, 539) ,
'10028': (324, 458) ,
'10029': (324, 377) ,
'10030': (324, 296) ,
'10031': (324, 215) ,
'10032': (324, 134) ,
'10033': (405, 620) ,
'10034': (891, 539) ,
'10035': (648, 377) ,
'10036': (486, 458) ,
'10037': (891, 377) ,
'10038': (648, 296) ,
'10039': (648, 215) ,
'10040': (648, 134) ,
'10041': (648, 53) ,
'10042': (729, 296) ,
'10043': (891, 296) ,
'10044': (810, 53) ,
'10045': (729, 215) ,
'10046': (729, 134) ,
'10047': (729, 53) ,
'10048': (810, 215) ,
'10049': (891, 215) ,
'10050': (810, 134) ,
'10051': (810, 377) ,
'10052': (810, 296) ,
'10053': (729, 377) ,
'10054': (648, 458) ,
'10055': (486, 377) ,
'10056': (486, 296) ,
'10057': (486, 215) ,
'10058': (486, 134) ,
'10059': (486, 53) ,
'10060': (567, 458) ,
'10061': (729, 458) ,
'10062': (567, 53) ,
'10063': (810, 458) ,
'10064': (891, 458) ,
'10065': (567, 377) ,
'10066': (567, 296) ,
'10067': (567, 215) ,
'10068': (567, 134) ,
'10069': (324, 701) ,
'10070': (810, 539) ,
'10071': (243, 53) ,
'10072': (162, 863) ,
'10073': (648, 944) ,
'10074': (729, 944) ,
'10075': (810, 944) ,
'10076': (891, 944) ,
'10077': (81, 863) ,
'20001': (81, 782) ,
'20002': (81, 620) ,
'20003': (81, 53) ,
'20004': (81, 539) ,
'20005': (81, 458) ,
'20006': (81, 377) ,
'20007': (81, 296) ,
'20008': (81, 215) ,
'20009': (81, 134) ,
'20010': (567, 944) ,
'20011': (81, 701) ,
'20012': (486, 944) ,
'20013': (0, 377) ,
'20014': (0, 863) ,
'20015': (0, 782) ,
'20016': (0, 701) ,
'20017': (0, 620) ,
'20018': (0, 539) ,
'20019': (0, 458) ,
'20020': (0, 296) ,
'20021': (324, 944) ,
'20022': (0, 215) ,
'20023': (0, 134) ,
'20024': (0, 53) ,
'20025': (81, 944) ,
'20026': (162, 944) ,
'20027': (243, 944) ,
'20028': (405, 944) ,
'20029': (243, 863) ,
'20030': (162, 134) ,
'20031': (324, 863) ,
'20032': (324, 782) ,
'20033': (405, 782) ,
'20034': (486, 782) ,
'20035': (567, 782) ,
'20036': (648, 782) ,
'20037': (729, 782) ,
'20038': (891, 782) ,
'20039': (243, 215) ,
'20040': (243, 701) ,
'20041': (243, 620) ,
'20042': (243, 539) ,
'20043': (243, 458) ,
'20044': (243, 377) ,
'20045': (243, 296) ,
'20046': (243, 782) ,
'20047': (810, 782) ,
'20048': (162, 53) ,
'20049': (891, 863) ,
'20050': (405, 863) ,
'20051': (486, 863) ,
'20052': (567, 863) ,
'20053': (648, 863) ,
'20054': (729, 863) ,
'20055': (810, 863) ,
'20056': (162, 782) ,
'20057': (162, 215) ,
'20058': (162, 701) ,
'20059': (162, 620) ,
'20060': (162, 539) ,
'20061': (162, 458) ,
'20062': (162, 377) ,
'20063': (162, 296) ,
'20064': (243, 134) ,
'20065': (891, 134) ,
'00000': (0, 944) 
}

listma = [('10001', 'normal', '蘋果', 'ㄧㄥ', 'ㄨㄛ'),
('10001', 'great', '禁忌的果實', 'ㄧㄣ', 'ㄕ'),
('10001', 'great', '智慧之果', 'ㄓ', 'ㄨㄛ'),
('10002', 'normal', '黑猩猩', 'ㄟ', 'ㄧㄥ'),
('10002', 'great', '靈長類', 'ㄧㄥ', 'ㄟ'),
('10002', 'great', '嗚吼嗚吼', 'ㄨ', 'ㄡ'),
('10002', 'puricone', '擲岩猴仙', 'ㄓ', 'ㄧㄢ'),
('10003', 'normal', '喇叭', 'ㄚ', 'ㄚ'),
('10003', 'great', '小號', 'ㄧㄠ', 'ㄠ'),
('10003', 'great', '管樂器', 'ㄨㄢ', 'ㄧ'),
('10004', 'normal', '鳳梨', 'ㄥ', 'ㄧ'),
('10004', 'great', '菠蘿', 'ㄛ', 'ㄨㄛ'),
('10004', 'great', '旺來', 'ㄨㄤ', 'ㄞ'),
('10005', 'normal', '紅寶石', 'ㄨㄥ', 'ㄕ'),
('10005', 'normal', '寶石', 'ㄠ', 'ㄕ'),
('10005', 'great', '魔法石', 'ㄛ', 'ㄕ'),
('10005', 'puricone', '秋乃的胸針', 'ㄧㄡ', 'ㄣ'),
('10005', 'puricone', '紫藤紅輝石', 'ㄗ', 'ㄕ'),
('10006', 'normal', '啤酒', 'ㄧ', 'ㄧㄡ'),
('10006', 'normal', '酒杯', 'ㄧㄡ', 'ㄟ'),
('10006', 'great', '麥酒', 'ㄞ', 'ㄧㄡ'),
('10006', 'puricone', '永恆之盅', 'ㄥ', 'ㄨㄥ'),
('10007', 'normal', '弓箭', 'ㄨㄥ', 'ㄧㄢ'),
('10007', 'normal', '箭矢', 'ㄧㄢ', 'ㄕ'),
('10007', 'great', '遠距離武器', 'ㄩㄢ', 'ㄧ'),
('10007', 'great', '邱比特', 'ㄧㄡ', 'ㄜ'),
('10007', 'great', '打獵', 'ㄚ', 'ㄧㄝ'),
('10007', 'great', '狩獵', 'ㄡ', 'ㄧㄝ'),
('10008', 'normal', '音符', 'ㄧㄣ', 'ㄨ'),
('10008', 'normal', '旋律', 'ㄩㄢ', 'ㄩ'),
('10008', 'great', 'ㄉㄡㄖㄨㄟㄇㄧ', 'ㄡ', 'ㄧ'),
('10008', 'great', '和弦', 'ㄜ', 'ㄧㄢ'),
('10009', 'normal', '顏料', 'ㄧㄢ', 'ㄧㄠ'),
('10009', 'normal', '水彩', 'ㄨㄟ', 'ㄞ'),
('10009', 'great', '軟管', 'ㄨㄢ', 'ㄨㄢ'),
('10009', 'great', '藍色', 'ㄢ', 'ㄜ'),
('10010', 'normal', '劍', 'ㄧㄢ', 'ㄧㄢ'),
('10010', 'great', '武器', 'ㄨ', 'ㄧ'),
('10010', 'great', '短劍', 'ㄨㄢ', 'ㄧㄢ'),
('10010', 'puricone', '公主之劍', 'ㄨㄥ', 'ㄧㄢ'),
('10010', 'great', '近戰武器', 'ㄧㄣ', 'ㄧ'),
('10011', 'normal', '眼鏡', 'ㄧㄢ', 'ㄧㄥ'),
('10011', 'great', '鏡片', 'ㄧㄥ', 'ㄧㄢ'),
('10011', 'great', '書呆子', 'ㄨ', 'ㄗ'),
('10011', 'great', '扮裝道具', 'ㄢ', 'ㄩ'),
('10011', 'puricone', '花凜的眼鏡', 'ㄨㄚ', 'ㄧㄥ'),
('10012', 'normal', '放大鏡', 'ㄤ', 'ㄧㄥ'),
('10012', 'normal', '鏡片', 'ㄧㄥ', 'ㄧㄢ'),
('10012', 'great', '凸透鏡', 'ㄨ', 'ㄧㄥ'),
('10012', 'puricone', '偵探必備的物品', 'ㄣ', 'ㄧㄣ'),
('10013', 'normal', '肉', 'ㄡ', 'ㄡ'),
('10013', 'great', '料理', 'ㄧㄠ', 'ㄧ'),
('10013', 'great', '帶骨肉', 'ㄞ', 'ㄡ'),
('10013', 'puricone', '龍肉', 'ㄨㄥ', 'ㄡ'),
('10014', 'normal', '月亮', 'ㄩㄝ', 'ㄧㄤ'),
('10014', 'normal', '滿月', 'ㄢ', 'ㄩㄝ'),
('10014', 'great', '露娜', 'ㄨ', 'ㄚ'),
('10014', 'great', '中秋節', 'ㄨㄥ', 'ㄧㄝ'),
('10014', 'great', '衛星', 'ㄟ', 'ㄧㄥ'),
('10015', 'normal', '蝙蝠', 'ㄧㄢ', 'ㄨ'),
('10015', 'great', '德古拉', 'ㄜ', 'ㄚ'),
('10015', 'puricone', '伊莉亞的眷屬', 'ㄧ', 'ㄨ'),
('10016', 'normal', '鳥類', 'ㄧㄠ', 'ㄟ'),
('10016', 'great', '魔物', 'ㄛ', 'ㄨ'),
('10016', 'puricone', '席茲', 'ㄧ', 'ㄗ'),
('10016', 'great', '始祖鳥', 'ㄕ', 'ㄧㄠ'),
('10016', 'great', '猛禽', 'ㄥ', 'ㄧㄣ'),
('10017', 'normal', '鞋子', 'ㄧㄝ', 'ㄗ'),
('10017', 'normal', '短靴', 'ㄨㄢ', 'ㄩㄝ'),
('10017', 'great', '皮鞋', 'ㄧ', 'ㄧㄝ'),
('10017', 'great', '靴子', 'ㄩㄝ', 'ㄗ'),
('10017', 'great', '防具', 'ㄤ', 'ㄩ'),
('10018', 'normal', '貓咪', 'ㄠ', 'ㄧ'),
('10018', 'normal', '花貓', 'ㄨㄚ', 'ㄠ'),
('10018', 'puricone', '珠希的朋友', 'ㄨ', 'ㄧㄡ'),
('10019', 'normal', '金魚', 'ㄧㄣ', 'ㄩ'),
('10019', 'normal', '小魚', 'ㄧㄠ', 'ㄩ'),
('10019', 'normal', '魚', 'ㄩ', 'ㄩ'),
('10019', 'great', '觀賞魚', 'ㄨㄢ', 'ㄩ'),
('10020', 'normal', '老鼠', 'ㄠ', 'ㄨ'),
('10020', 'great', '吱吱', 'ㄓ', 'ㄓ'),
('10020', 'great', '齧齒生物', 'ㄧㄝ', 'ㄨ'),
('10021', 'normal', '蛋', 'ㄢ', 'ㄢ'),
('10021', 'great', '卵', 'ㄨㄢ', 'ㄨㄢ'),
('10021', 'great', '鳥巢', 'ㄧㄠ', 'ㄠ'),
('10021', 'great', '燕窩', 'ㄧㄢ', 'ㄨㄛ'),
('10022', 'normal', '船', 'ㄨㄢ', 'ㄨㄢ'),
('10022', 'great', '帆船', 'ㄢ', 'ㄨㄢ'),
('10022', 'great', '軍艦', 'ㄩㄣ', 'ㄧㄢ'),
('10022', 'great', '航海', 'ㄤ', 'ㄞ'),
('10022', 'great', '大航海時代', 'ㄚ', 'ㄞ'),
('10022', 'great', '貿易', 'ㄠ', 'ㄧ'),
('10023', 'normal', '牛奶', 'ㄧㄡ', 'ㄞ'),
('10023', 'great', 'ㄋㄟㄋㄟ', 'ㄟ', 'ㄟ'),
('10023', 'great', '酸奶', 'ㄨㄢ', 'ㄞ'),
('10023', 'puricone', '伊麗莎白', 'ㄧ', 'ㄞ'),
('10024', 'normal', '巧克力', 'ㄧㄠ', 'ㄧ'),
('10024', 'normal', '朱古力', 'ㄨ', 'ㄧ'),
('10024', 'great', '甜食', 'ㄧㄢ', 'ㄕ'),
('10024', 'puricone', '哆啦喜歡的東西', 'ㄨㄛ', 'ㄧ'),
('10025', 'normal', '橡果', 'ㄧㄤ', 'ㄨㄛ'),
('10025', 'great', '果實', 'ㄨㄛ', 'ㄕ'),
('10025', 'great', '堅果', 'ㄧㄢ', 'ㄨㄛ'),
('10025', 'puricone', '鈴的點心', 'ㄧㄥ', 'ㄧㄣ'),
('10026', 'normal', '草莓', 'ㄠ', 'ㄟ'),
('10026', 'great', '野莓', 'ㄧㄝ', 'ㄟ'),
('10026', 'great', '莓果', 'ㄟ', 'ㄨㄛ'),
('10027', 'normal', '老虎', 'ㄠ', 'ㄨ'),
('10027', 'great', '猛獸', 'ㄥ', 'ㄡ'),
('10027', 'puricone', '茉莉的憧憬', 'ㄛ', 'ㄧㄥ'),
('10027', 'puricone', '無敵英雄虎虎', 'ㄨ', 'ㄨ'),
('10028', 'normal', '兔子', 'ㄨ', 'ㄗ'),
('10028', 'normal', '玩偶', 'ㄨㄢ', 'ㄡ'),
('10028', 'great', '娃娃', 'ㄨㄚ', 'ㄨㄚ'),
('10028', 'puricone', '亞瑟', 'ㄧㄚ', 'ㄜ'),
('10029', 'normal', '炸彈', 'ㄚ', 'ㄢ'),
('10029', 'great', '危險物品', 'ㄨㄟ', 'ㄧㄣ'),
('10029', 'great', '遠距離武器', 'ㄩㄢ', 'ㄧ'),
('10029', 'puricone', '禊的惡作劇道具', 'ㄧ', 'ㄩ'),
('10030', 'normal', '西瓜', 'ㄧ', 'ㄨㄚ'),
('10030', 'great', '夏天風情', 'ㄧㄚ', 'ㄧㄥ'),
('10030', 'great', '清涼退火', 'ㄧㄥ', 'ㄨㄛ'),
('10031', 'normal', '馬', 'ㄚ', 'ㄚ'),
('10031', 'normal', '驢子', 'ㄩ', 'ㄗ'),
('10031', 'great', '純種馬', 'ㄨㄣ', 'ㄚ'),
('10031', 'puricone', '夢魘', 'ㄥ', 'ㄧㄢ'),
('10032', 'normal', '椅子', 'ㄧ', 'ㄗ'),
('10032', 'great', '家具', 'ㄧㄚ', 'ㄩ'),
('10032', 'great', '小學椅', 'ㄧㄠ', 'ㄧ'),
('10032', 'puricone', '公會小屋道具', 'ㄨㄥ', 'ㄩ'),
('10033', 'normal', '海', 'ㄞ', 'ㄞ'),
('10033', 'normal', '淺灘', 'ㄧㄢ', 'ㄢ'),
('10033', 'great', '潮汐', 'ㄠ', 'ㄧ'),
('10033', 'great', '浪花', 'ㄤ', 'ㄨㄚ'),
('10033', 'puricone', '瑪爾傑海岸', 'ㄚ', 'ㄢ'),
('10034', 'normal', '貝殼', 'ㄟ', 'ㄜ'),
('10034', 'great', '甲殼類', 'ㄧㄚ', 'ㄟ'),
('10034', 'puricone', '寄居蟹騎士', 'ㄧ', 'ㄕ'),
('10035', 'normal', '笛', 'ㄧ', 'ㄧ'),
('10035', 'normal', '直笛', 'ㄓ', 'ㄧ'),
('10035', 'great', '管樂器', 'ㄨㄢ', 'ㄧ'),
('10035', 'great', '豎笛', 'ㄨ', 'ㄧ'),
('10036', 'normal', '書本', 'ㄨ', 'ㄣ'),
('10036', 'normal', '筆記', 'ㄧ', 'ㄧ'),
('10036', 'great', '小說', 'ㄧㄠ', 'ㄨㄛ'),
('10036', 'puricone', '凱留的魔導書', 'ㄞ', 'ㄨ'),
('10037', 'normal', '魚', 'ㄩ', 'ㄩ'),
('10037', 'normal', '小魚', 'ㄧㄠ', 'ㄩ'),
('10037', 'great', '鮪魚', 'ㄟ', 'ㄩ'),
('10037', 'great', '海洋生物', 'ㄞ', 'ㄨ'),
('10038', 'normal', '樹', 'ㄨ', 'ㄨ'),
('10038', 'great', '杉木', 'ㄢ', 'ㄨ'),
('10038', 'great', '聖誕節', 'ㄥ', 'ㄧㄝ'),
('10038', 'great', '耶誕樹', 'ㄧㄝ', 'ㄨ'),
('10038', 'great', '平安夜', 'ㄧㄥ', 'ㄧㄝ'),
('10038', 'puricone', '忘却的頌歌', 'ㄨㄤ', 'ㄜ'),
('10039', 'normal', '棒棒糖', 'ㄤ', 'ㄤ'),
('10039', 'great', '甜食', 'ㄧㄢ', 'ㄕ'),
('10039', 'puricone', '克蘿依的點心', 'ㄜ', 'ㄧㄣ'),
('10040', 'normal', '玩具槌', 'ㄨㄢ', 'ㄨㄟ'),
('10040', 'great', '鐵鎚', 'ㄧㄝ', 'ㄨㄟ'),
('10040', 'great', '小槌', 'ㄧㄠ', 'ㄨㄟ'),
('10040', 'puricone', '祈梨的武器', 'ㄧ', 'ㄧ'),
('10041', 'normal', '星星', 'ㄧㄥ', 'ㄧㄥ'),
('10041', 'great', '海星', 'ㄞ', 'ㄧㄥ'),
('10041', 'great', '亮晶晶', 'ㄧㄤ', 'ㄧㄥ'),
('10041', 'great', '流星', 'ㄧㄡ', 'ㄧㄥ'),
('10041', 'puricone', '蘭德索爾的形狀', 'ㄢ', 'ㄨㄤ'),
('10042', 'normal', '帽子', 'ㄠ', 'ㄗ'),
('10042', 'great', '禮帽', 'ㄧ', 'ㄠ'),
('10042', 'great', '紳士', 'ㄣ', 'ㄕ'),
('10043', 'normal', '杯子', 'ㄟ', 'ㄗ'),
('10043', 'great', '馬克杯', 'ㄚ', 'ㄟ'),
('10043', 'great', '可可', 'ㄜ', 'ㄜ'),
('10043', 'great', '摩卡', 'ㄛ', 'ㄚ'),
('10044', 'normal', '狗', 'ㄡ', 'ㄡ'),
('10044', 'normal', '犬', 'ㄩㄢ', 'ㄩㄢ'),
('10044', 'great', '狼', 'ㄤ', 'ㄤ'),
('10044', 'great', '月月', 'ㄩㄝ', 'ㄩㄝ'),
('10044', 'great', '哈士奇', 'ㄚ', 'ㄧ'),
('10045', 'normal', '旗子', 'ㄧ', 'ㄗ'),
('10045', 'great', '戰旗', 'ㄢ', 'ㄧ'),
('10045', 'great', '信號旗', 'ㄧㄣ', 'ㄧ'),
('10046', 'normal', '蛋糕', 'ㄢ', 'ㄠ'),
('10046', 'great', '點心', 'ㄧㄢ', 'ㄧㄣ'),
('10046', 'great', '生日快樂', 'ㄥ', 'ㄜ'),
('10046', 'puricone', '羈絆點數', 'ㄧ', 'ㄨ'),
('10046', 'puricone', '綜合莓果蛋糕', 'ㄨㄥ', 'ㄠ'),
('10047', 'normal', '麥克風', 'ㄞ', 'ㄥ'),
('10047', 'great', '唱歌', 'ㄤ', 'ㄜ'),
('10047', 'great', '演唱會', 'ㄧㄢ', 'ㄨㄟ'),
('10047', 'great', '偶像的必備物品', 'ㄡ', 'ㄧㄣ'),
('10047', 'puricone', '閃耀麥克風', 'ㄢ', 'ㄥ'),
('10048', 'normal', '口紅', 'ㄡ', 'ㄨㄥ'),
('10048', 'normal', '唇膏', 'ㄨㄣ', 'ㄠ'),
('10048', 'great', '化妝品', 'ㄨㄚ', 'ㄧㄣ'),
('10049', 'normal', '年糕', 'ㄧㄢ', 'ㄠ'),
('10049', 'normal', '麻糬', 'ㄚ', 'ㄨ'),
('10049', 'great', '鏡餅', 'ㄧㄥ', 'ㄧㄥ'),
('10049', 'great', '碳水化合物', 'ㄢ', 'ㄨ'),
('10049', 'great', '糯米糕', 'ㄨㄛ', 'ㄠ'),
('10050', 'normal', '妖精', 'ㄧㄠ', 'ㄧㄥ'),
('10050', 'puricone', '涅比亞', 'ㄧㄝ', 'ㄧㄚ'),
('10051', 'normal', '雨傘', 'ㄩ', 'ㄢ'),
('10051', 'great', '遮陽傘', 'ㄜ', 'ㄢ'),
('10051', 'great', '陽傘', 'ㄧㄤ', 'ㄢ'),
('10051', 'puricone', '貪吃佩可夏日', 'ㄢ', 'ㄖ'),
('10052', 'normal', '骰子', 'ㄞ', 'ㄗ'),
('10052', 'great', '賭博', 'ㄨ', 'ㄛ'),
('10052', 'great', '六面體', 'ㄧㄡ', 'ㄧ'),
('10052', 'great', '大富翁', 'ㄚ', 'ㄨㄥ'),
('10052', 'great', '洗八啦', 'ㄧ', 'ㄚ'),
('10053', 'normal', '信', 'ㄧㄣ', 'ㄧㄣ'),
('10053', 'great', '郵件', 'ㄧㄡ', 'ㄧㄢ'),
('10053', 'great', '情書', 'ㄧㄥ', 'ㄨ'),
('10053', 'great', '書信', 'ㄨ', 'ㄧㄣ'),
('10053', 'great', '飛鴿傳書', 'ㄟ', 'ㄨ'),
('10054', 'normal', '葡萄', 'ㄨ', 'ㄠ'),
('10054', 'great', '巨峰', 'ㄩ', 'ㄥ'),
('10054', 'great', '紫葡萄', 'ㄗ', 'ㄠ'),
('10055', 'normal', '綿羊', 'ㄧㄢ', 'ㄧㄤ'),
('10055', 'normal', '羊咩咩', 'ㄧㄤ', 'ㄧㄝ'),
('10055', 'great', '白羊', 'ㄞ', 'ㄧㄤ'),
('10055', 'great', '瑪莉有隻小綿羊', 'ㄚ', 'ㄧㄤ'),
('10056', 'normal', '豆腐', 'ㄡ', 'ㄨ'),
('10056', 'great', '木綿豆腐', 'ㄨ', 'ㄨ'),
('10056', 'great', '涼拌豆腐', 'ㄧㄤ', 'ㄨ'),
('10056', 'great', '杏仁豆腐', 'ㄧㄥ', 'ㄨ'),
('10057', 'normal', '鴨子', 'ㄧㄚ', 'ㄗ'),
('10057', 'great', '鳥類', 'ㄧㄠ', 'ㄟ'),
('10057', 'great', '水鳥', 'ㄨㄟ', 'ㄧㄠ'),
('10058', 'normal', '蜻蜓', 'ㄧㄥ', 'ㄧㄥ'),
('10058', 'great', '晏蜓', 'ㄧㄢ', 'ㄧㄥ'),
('10058', 'great', '昆蟲', 'ㄨㄣ', 'ㄨㄥ'),
('10058', 'great', '飛龍', 'ㄟ', 'ㄨㄥ'),
('10059', 'normal', '葉子', 'ㄧㄝ', 'ㄗ'),
('10059', 'normal', '樹葉', 'ㄨ', 'ㄧㄝ'),
('10059', 'great', '綠葉', 'ㄩ', 'ㄧㄝ'),
('10059', 'puricone', '碧的朋友', 'ㄧ', 'ㄧㄡ'),
('10060', 'normal', '戒指', 'ㄧㄝ', 'ㄓ'),
('10060', 'normal', '鑽戒', 'ㄨㄢ', 'ㄧㄝ'),
('10060', 'great', '指環', 'ㄓ', 'ㄨㄢ'),
('10060', 'great', '珠寶', 'ㄨ', 'ㄠ'),
('10061', 'normal', '繩子', 'ㄥ', 'ㄗ'),
('10061', 'normal', '麻繩', 'ㄚ', 'ㄥ'),
('10061', 'great', '草繩', 'ㄠ', 'ㄥ'),
('10061', 'puricone', '空花的秘密道具', 'ㄨㄥ', 'ㄩ'),
('10061', 'puricone', '絕頂', 'ㄩㄝ', 'ㄧㄠ'),
('10062', 'normal', '盾牌', 'ㄨㄣ', 'ㄞ'),
('10062', 'great', '護具', 'ㄨ', 'ㄩ'),
('10062', 'great', '防具', 'ㄤ', 'ㄩ'),
('10062', 'great', '裝備', 'ㄨㄤ', 'ㄟ'),
('10062', 'puricone', '地獄之盾', 'ㄧ', 'ㄨㄣ'),
('10063', 'normal', '錢幣', 'ㄧㄢ', 'ㄧ'),
('10063', 'normal', '金錢', 'ㄧㄣ', 'ㄧㄢ'),
('10063', 'great', '寶藏', 'ㄠ', 'ㄤ'),
('10063', 'great', '財物', 'ㄞ', 'ㄨ'),
('10063', 'puricone', '盧幣', 'ㄨ', 'ㄧ'),
('10063', 'puricone', '公會小屋購買家具', 'ㄨㄥ', 'ㄩ'),
('10064', 'normal', '布丁', 'ㄨ', 'ㄧㄥ'),
('10064', 'great', '豪華法式布丁', 'ㄠ', 'ㄧㄥ'),
('10064', 'great', '甜點', 'ㄧㄢ', 'ㄧㄢ'),
('10064', 'puricone', '宮子的點心', 'ㄨㄥ', 'ㄧㄣ'),
('10065', 'normal', '項鍊', 'ㄧㄤ', 'ㄧㄢ'),
('10065', 'great', '墜飾', 'ㄨㄟ', 'ㄕ'),
('10065', 'great', '飾品', 'ㄕ', 'ㄧㄣ'),
('10065', 'great', '首飾', 'ㄡ', 'ㄕ'),
('10066', 'normal', '稻米', 'ㄠ', 'ㄧ'),
('10066', 'great', '米飯', 'ㄧ', 'ㄢ'),
('10066', 'great', '麥子', 'ㄞ', 'ㄗ'),
('10066', 'great', '穀物', 'ㄨ', 'ㄨ'),
('10067', 'normal', '醬油', 'ㄧㄤ', 'ㄧㄡ'),
('10067', 'great', '豆油', 'ㄡ', 'ㄧㄡ'),
('10067', 'great', '調味料', 'ㄧㄠ', 'ㄧㄠ'),
('10067', 'great', '柴魚醬油', 'ㄞ', 'ㄧㄡ'),
('10068', 'normal', '輸送帶', 'ㄨ', 'ㄞ'),
('10068', 'great', '工廠', 'ㄨㄥ', 'ㄤ'),
('10068', 'great', '生產線', 'ㄥ', 'ㄧㄢ'),
('10068', 'puricone', '鯛魚燒工廠', 'ㄧㄠ', 'ㄤ'),
('10069', 'normal', '吊燈', 'ㄧㄠ', 'ㄥ'),
('10069', 'great', '燭臺', 'ㄨ', 'ㄞ'),
('10069', 'great', '燈飾', 'ㄥ', 'ㄕ'),
('10070', 'normal', '鹽', 'ㄧㄢ', 'ㄧㄢ'),
('10070', 'great', '氯化納', 'ㄩ', 'ㄚ'),
('10070', 'great', '調味料', 'ㄧㄠ', 'ㄧㄠ'),
('10070', 'great', '低鈉鹽', 'ㄧ', 'ㄧㄢ'),
('10071', 'normal', '漩渦', 'ㄩㄢ', 'ㄨㄛ'),
('10071', 'great', '咕嚕咕嚕', 'ㄨ', 'ㄨ'),
('10071', 'great', '海難', 'ㄞ', 'ㄢ'),
('10072', 'normal', '釣竿', 'ㄧㄠ', 'ㄢ'),
('10072', 'great', '魚餌', 'ㄩ', 'ㄦ'),
('10072', 'puricone', '流夏的興趣', 'ㄧㄡ', 'ㄩ'),
('10073', 'normal', '鍋子', 'ㄨㄛ', 'ㄗ'),
('10073', 'great', '咖哩', 'ㄚ', 'ㄧ'),
('10073', 'great', '燉菜', 'ㄨㄣ', 'ㄞ'),
('10073', 'great', '滷汁', 'ㄨ', 'ㄓ'),
('10073', 'great', '紅酒燉牛肉', 'ㄨㄥ', 'ㄡ'),
('10074', 'normal', '蹺蹺板', 'ㄧㄠ', 'ㄢ'),
('10074', 'great', '兒童遊樂設施', 'ㄦ', 'ㄕ'),
('10074', 'great', '去公園玩', 'ㄩ', 'ㄨㄢ'),
('10074', 'great', '失衡', 'ㄕ', 'ㄥ'),
('10075', 'normal', '筆', 'ㄧ', 'ㄧ'),
('10075', 'great', '書法', 'ㄨ', 'ㄚ'),
('10075', 'great', '毛筆', 'ㄠ', 'ㄧ'),
('10075', 'great', '寫字', 'ㄧㄝ', 'ㄗ'),
('10075', 'great', '硯臺', 'ㄧㄢ', 'ㄞ'),
('10075', 'puricone', '東國文化', 'ㄨㄥ', 'ㄨㄚ'),
('10076', 'normal', '啞鈴', 'ㄧㄚ', 'ㄧㄥ'),
('10076', 'great', '肌肉', 'ㄧ', 'ㄡ'),
('10076', 'great', '鍛鍊', 'ㄨㄢ', 'ㄧㄢ'),
('10076', 'great', '重訓', 'ㄨㄥ', 'ㄩㄣ'),
('10076', 'great', '二頭肌', 'ㄦ', 'ㄧ'),
('10077', 'normal', '鬼魂', 'ㄨㄟ', 'ㄨㄣ'),
('10077', 'normal', '幽靈', 'ㄧㄡ', 'ㄧㄥ'),
('10077', 'puricone', '宮子', 'ㄨㄥ', 'ㄗ'),
('10077', 'puricone', '無敵', 'ㄨ', 'ㄧ'),
('20001', 'normal', '日和', 'ㄖ', 'ㄜ'),
('20001', 'puricone', '放不下心', 'ㄤ', 'ㄧㄣ'),
('20002', 'normal', '優衣', 'ㄡ', 'ㄧ'),
('20002', 'puricone', '全體治癒', 'ㄩㄢ', 'ㄩ'),
('20002', 'puricone', '真琴的兒時玩伴', 'ㄣ', 'ㄢ'),
('20003', 'normal', '怜', 'ㄧㄥ', 'ㄧㄥ'),
('20003', 'puricone', '騎馬', 'ㄧ', 'ㄚ'),
('20003', 'puricone', '劍術', 'ㄧㄢ', 'ㄨ'),
('20004', 'normal', '禊', 'ㄧ', 'ㄧ'),
('20004', 'puricone', '搗蛋鬼', 'ㄠ', 'ㄨㄟ'),
('20005', 'normal', '茉莉', 'ㄛ', 'ㄧ'),
('20005', 'puricone', '見習英雄', 'ㄧ', 'ㄧㄥ'),
('20006', 'normal', '茜里', 'ㄧㄢ', 'ㄧ'),
('20006', 'puricone', '依里的妹妹', 'ㄧ', 'ㄟ'),
('20006', 'puricone', '小惡魔', 'ㄧㄠ', 'ㄛ'),
('20007', 'normal', '宮子', 'ㄨㄥ', 'ㄗ'),
('20007', 'puricone', '幽靈', 'ㄧㄡ', 'ㄧㄥ'),
('20007', 'puricone', '最喜歡布丁', 'ㄨㄟ', 'ㄧㄥ'),
('20008', 'normal', '雪', 'ㄩㄝ', 'ㄩㄝ'),
('20008', 'puricone', '美麗的我', 'ㄟ', 'ㄨㄛ'),
('20008', 'puricone', '自戀', 'ㄗ', 'ㄧㄢ'),
('20009', 'normal', '杏奈', 'ㄧㄥ', 'ㄞ'),
('20009', 'puricone', '疾風之冥姬', 'ㄧ', 'ㄧ'),
('20009', 'puricone', '中二病', 'ㄨㄥ', 'ㄧㄥ'),
('20010', 'normal', '真步', 'ㄣ', 'ㄨ'),
('20010', 'puricone', '公主', 'ㄨㄥ', 'ㄨ'),
('20010', 'puricone', '咕嚕靈波', 'ㄨ', 'ㄛ'),
('20011', 'normal', '璃乃', 'ㄧ', 'ㄞ'),
('20011', 'puricone', '妹妹', 'ㄟ', 'ㄟ'),
('20011', 'puricone', '小笨蛋', 'ㄧㄠ', 'ㄢ'),
('20012', 'normal', '初音', 'ㄨ', 'ㄧㄣ'),
('20012', 'puricone', '超能力少女', 'ㄠ', 'ㄩ'),
('20012', 'puricone', '小栞的姊姊', 'ㄧㄠ', 'ㄧㄝ'),
('20013', 'normal', '七七香', 'ㄧ', 'ㄧㄤ'),
('20013', 'puricone', '魔法少女', 'ㄛ', 'ㄩ'),
('20013', 'puricone', '最可愛', 'ㄨㄟ', 'ㄞ'),
('20014', 'normal', '霞', 'ㄧㄚ', 'ㄧㄚ'),
('20014', 'puricone', '名偵探', 'ㄧㄥ', 'ㄢ'),
('20014', 'puricone', '偵探', 'ㄣ', 'ㄢ'),
('20015', 'normal', '美里', 'ㄟ', 'ㄧ'),
('20015', 'puricone', '幼稚園的老師', 'ㄧㄡ', 'ㄕ'),
('20016', 'normal', '鈴奈', 'ㄧㄥ', 'ㄞ'),
('20016', 'puricone', '超級名模', 'ㄠ', 'ㄛ'),
('20016', 'puricone', '辣妹', 'ㄚ', 'ㄟ'),
('20017', 'normal', '香織', 'ㄧㄤ', 'ㄓ'),
('20017', 'puricone', '琉球空手道', 'ㄧㄡ', 'ㄠ'),
('20017', 'puricone', '嗨―呵', 'ㄞ', 'ㄜ'),
('20018', 'normal', '伊緒', 'ㄧ', 'ㄩ'),
('20018', 'puricone', '老師', 'ㄠ', 'ㄕ'),
('20019', 'normal', '美美', 'ㄟ', 'ㄟ'),
('20019', 'puricone', '最喜歡兔子先生', 'ㄨㄟ', 'ㄥ'),
('20020', 'normal', '胡桃', 'ㄨ', 'ㄠ'),
('20020', 'puricone', '知名女演員', 'ㄓ', 'ㄩㄢ'),
('20021', 'normal', '依里', 'ㄧ', 'ㄧ'),
('20021', 'puricone', '雙胞胎姊姊', 'ㄨㄤ', 'ㄧㄝ'),
('20021', 'puricone', '害羞', 'ㄞ', 'ㄧㄡ'),
('20021', 'puricone', '天才玩家', 'ㄧㄢ', 'ㄧㄚ'),
('20022', 'normal', '綾音', 'ㄧㄥ', 'ㄧㄣ'),
('20022', 'puricone', '噗吉的夥伴', 'ㄨ', 'ㄢ'),
('20023', 'normal', '鈴莓', 'ㄧㄥ', 'ㄟ'),
('20023', 'puricone', '女僕', 'ㄩ', 'ㄨ'),
('20023', 'puricone', '冒冒失失', 'ㄠ', 'ㄕ'),
('20024', 'normal', '鈴', 'ㄧㄥ', 'ㄧㄥ'),
('20024', 'puricone', '懶散', 'ㄢ', 'ㄢ'),
('20025', 'normal', '惠理子', 'ㄨㄟ', 'ㄗ'),
('20025', 'puricone', '破壞者', 'ㄛ', 'ㄜ'),
('20026', 'normal', '咲戀', 'ㄧㄠ', 'ㄧㄢ'),
('20026', 'puricone', '媽媽', 'ㄚ', 'ㄚ'),
('20027', 'normal', '望', 'ㄨㄤ', 'ㄨㄤ'),
('20027', 'puricone', '超人氣偶像', 'ㄠ', 'ㄧㄤ'),
('20028', 'normal', '妮諾', 'ㄧ', 'ㄨㄛ'),
('20028', 'puricone', '憧憬東國', 'ㄨㄥ', 'ㄨㄛ'),
('20028', 'puricone', '冒牌忍者', 'ㄠ', 'ㄜ'),
('20029', 'normal', '忍', 'ㄣ', 'ㄣ'),
('20029', 'puricone', '占卜師', 'ㄢ', 'ㄕ'),
('20030', 'normal', '秋乃', 'ㄧㄡ', 'ㄞ'),
('20030', 'puricone', '大小姐', 'ㄚ', 'ㄧㄝ'),
('20031', 'normal', '真陽', 'ㄣ', 'ㄧㄤ'),
('20031', 'puricone', '牧場主人', 'ㄨ', 'ㄣ'),
('20031', 'puricone', '搞笑藝人之路', 'ㄠ', 'ㄨ'),
('20032', 'normal', '優花梨', 'ㄧㄡ', 'ㄧ'),
('20032', 'puricone', '女中酒豪', 'ㄩ', 'ㄠ'),
('20033', 'normal', '鏡華', 'ㄧㄥ', 'ㄨㄚ'),
('20033', 'puricone', '資優生', 'ㄗ', 'ㄥ'),
('20034', 'normal', '智', 'ㄓ', 'ㄓ'),
('20034', 'puricone', '御久間流', 'ㄩ', 'ㄧㄡ'),
('20035', 'normal', '栞', 'ㄢ', 'ㄢ'),
('20035', 'puricone', '初音的妹妹', 'ㄨ', 'ㄟ'),
('20036', 'normal', '碧', 'ㄧ', 'ㄧ'),
('20036', 'puricone', '邊緣人', 'ㄧㄢ', 'ㄣ'),
('20037', 'normal', '千歌', 'ㄧㄢ', 'ㄜ'),
('20037', 'puricone', '唱喚士', 'ㄤ', 'ㄕ'),
('20037', 'puricone', '歌姬', 'ㄜ', 'ㄧ'),
('20038', 'normal', '真琴', 'ㄣ', 'ㄧㄣ'),
('20038', 'puricone', '優衣的兒時玩伴', 'ㄧㄡ', 'ㄢ'),
('20038', 'puricone', '月月', 'ㄩㄝ', 'ㄩㄝ'),
('20039', 'normal', '伊莉亞', 'ㄧ', 'ㄧㄚ'),
('20039', 'puricone', '傳說的吸血鬼', 'ㄨㄢ', 'ㄨㄟ'),
('20039', 'puricone', '統領黑夜之人', 'ㄨㄥ', 'ㄣ'),
('20040', 'normal', '空花', 'ㄨㄥ', 'ㄨㄚ'),
('20040', 'puricone', '被虐狂', 'ㄟ', 'ㄨㄤ'),
('20041', 'normal', '珠希', 'ㄨ', 'ㄧ'),
('20041', 'puricone', '貓娘', 'ㄠ', 'ㄧㄤ'),
('20041', 'puricone', '幻影貓', 'ㄨㄢ', 'ㄠ'),
('20042', 'normal', '純', 'ㄨㄣ', 'ㄨㄣ'),
('20042', 'puricone', '團長', 'ㄨㄢ', 'ㄤ'),
('20043', 'normal', '美冬', 'ㄟ', 'ㄨㄥ'),
('20043', 'puricone', '師傅', 'ㄕ', 'ㄨ'),
('20043', 'puricone', '效率至上', 'ㄧㄠ', 'ㄤ'),
('20044', 'normal', '靜流', 'ㄧㄥ', 'ㄧㄡ'),
('20044', 'puricone', '是姐姐喔', 'ㄕ', 'ㄛ'),
('20045', 'normal', '美咲', 'ㄟ', 'ㄧㄠ'),
('20045', 'puricone', '成熟的淑女', 'ㄥ', 'ㄩ'),
('20046', 'normal', '深月', 'ㄣ', 'ㄩㄝ'),
('20046', 'puricone', '瘋狂科學家', 'ㄥ', 'ㄧㄚ'),
('20046', 'puricone', '獨眼惡魔', 'ㄨ', 'ㄛ'),
('20047', 'normal', '莉瑪', 'ㄧ', 'ㄚ'),
('20047', 'puricone', '毛茸茸', 'ㄠ', 'ㄨㄥ'),
('20048', 'normal', '莫妮卡', 'ㄛ', 'ㄚ'),
('20048', 'puricone', '小鬼頭', 'ㄧㄠ', 'ㄡ'),
('20049', 'normal', '紡希', 'ㄤ', 'ㄧ'),
('20049', 'puricone', '裁縫師', 'ㄞ', 'ㄕ'),
('20049', 'puricone', '怜大人粉絲俱樂部', 'ㄧㄥ', 'ㄨ'),
('20050', 'normal', '步未', 'ㄨ', 'ㄟ'),
('20050', 'puricone', '跟蹤狂', 'ㄣ', 'ㄨㄤ'),
('20051', 'normal', '流夏', 'ㄧㄡ', 'ㄧㄚ'),
('20051', 'puricone', '大姐頭', 'ㄚ', 'ㄡ'),
('20052', 'normal', '吉塔', 'ㄧ', 'ㄚ'),
('20052', 'puricone', '蒼空的騎空士', 'ㄤ', 'ㄕ'),
('20053', 'normal', '貪吃佩可', 'ㄢ', 'ㄜ'),
('20053', 'puricone', '皇家裝備', 'ㄨㄤ', 'ㄟ'),
('20053', 'puricone', '太讚了吧', 'ㄞ', 'ㄚ'),
('20054', 'normal', '可可蘿', 'ㄜ', 'ㄨㄛ'),
('20054', 'puricone', '嚮導', 'ㄧㄤ', 'ㄠ'),
('20054', 'puricone', '巫女', 'ㄨ', 'ㄩ'),
('20055', 'normal', '凱留', 'ㄞ', 'ㄧㄡ'),
('20055', 'puricone', '傲嬌', 'ㄠ', 'ㄧㄠ'),
('20055', 'puricone', '接頭霸王', 'ㄧㄝ', 'ㄨㄤ'),
('20056', 'normal', '矛依未', 'ㄠ', 'ㄨㄟ'),
('20056', 'puricone', '諾維姆', 'ㄨㄛ', 'ㄨ'),
('20057', 'normal', '亞里莎', 'ㄧㄚ', 'ㄚ'),
('20057', 'puricone', '精靈女', 'ㄧㄥ', 'ㄩ'),
('20057', 'puricone', '見習森林守衛', 'ㄧㄢ', 'ㄨㄟ'),
('20058', 'normal', '似似花', 'ㄙ', 'ㄨㄚ'),
('20058', 'puricone', '變貌大妃', 'ㄧㄢ', 'ㄟ'),
('20058', 'puricone', '分身', 'ㄣ', 'ㄣ'),
('20059', 'normal', '克莉絲提娜', 'ㄜ', 'ㄚ'),
('20059', 'puricone', '誓約女君', 'ㄕ', 'ㄩㄣ'),
('20059', 'puricone', '副團長', 'ㄨ', 'ㄤ'),
('20060', 'normal', '祈梨', 'ㄧ', 'ㄧ'),
('20060', 'puricone', '龍之吐息', 'ㄨㄥ', 'ㄧ'),
('20060', 'puricone', '幹部', 'ㄢ', 'ㄨ'),
('20061', 'normal', '嘉夜', 'ㄧㄚ', 'ㄧㄝ'),
('20061', 'puricone', '笨蛋打架狂', 'ㄣ', 'ㄨㄤ'),
('20062', 'normal', '帆稀', 'ㄢ', 'ㄧ'),
('20062', 'puricone', '幫派老大', 'ㄤ', 'ㄚ'),
('20063', 'normal', '克蘿依', 'ㄜ', 'ㄧ'),
('20063', 'puricone', '陰暗系', 'ㄧㄣ', 'ㄧ'),
('20063', 'puricone', '聖德蕾女的狂人', 'ㄥ', 'ㄣ'),
('20064', 'normal', '琪愛兒', 'ㄧ', 'ㄦ'),
('20064', 'puricone', '咧切嚕切嚕啵啪嗶', 'ㄧㄝ', 'ㄧ'),
('20064', 'puricone', '聖德蕾女的狂人', 'ㄥ', 'ㄣ'),
('20065', 'normal', '優妮', 'ㄧㄡ', 'ㄧ'),
('20065', 'puricone', '繭居族', 'ㄧㄢ', 'ㄨ'),
('20065', 'puricone', '聖德蕾女的狂人', 'ㄥ', 'ㄣ')]