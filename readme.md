# PCR自动接龙小助手

用python opencv写的(半)自动接龙脚本,在Mumu上测试成功

## 环境

+   支持adb的安卓设备/模拟器以及adb
+   opencv-python 3.4.2 及 opencv-contrib-python 3.4.2
+   pypinyin
+   ImageHash

## 使用方法

配置好环境后打开模拟器并运行小游戏,运行脚本后输入第一个词即可.

+   dict.json记录一些无法识别的图片的hash
+   history.json记录已经点击过的词, 可以使用[PCR_TW_JIELONG](https://github.com/pasiiww/PCR_TW_JIELONG)标注后用util.py转换
+   整个程序运行在1440*810分辨率下,否则请自己修改相关的截图坐标.
+   由于SIFT识别率不算太高,整个程序基本运行正常,但用来刷全图鉴还是不太行
+   内置一个选词判定算法,但效果不是很好
+   对于rush的支持暂未完全实现(也不会实现了)

## 一些问题

说到底这只是一时兴起写的demo,不完善的地方还有很多

+   对于右边的识别最好的方法是手工标注图片右下角的音韵标签
+   图片太少导致SIFT提供的特征太少,因此匹配效果不佳

## 感谢

+   pasiiww的[PCR_TW_JIELONG](https://github.com/pasiiww/PCR_TW_JIELONG)

