![](https://travis-ci.com/JamesHopbourn/matplotlib-with-travis.svg?branch=develop) ![](https://img.shields.io/github/last-commit/JamesHopbourn/matplotlib-with-travis/develop?style=flat-square) ![](https://img.shields.io/github/commit-activity/m/JamesHopbourn/matplotlib-with-travis?logo=green)

![](https://raw.githubusercontent.com/JamesHopbourn/matplotlib-with-travis/master/Demo.png)

matplotlib tample
```
# -*- coding: UTF-8 -*-
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['WenQuanYi Zen Hei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号 #有中文出现的情况，需要u'内容'

plt.show()
plt.savefig("Chinese.png")
```
