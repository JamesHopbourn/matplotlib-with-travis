![](https://travis-ci.com/JamesHopbourn/matplotlib-with-travis.svg?branch=develop) ![](https://img.shields.io/github/last-commit/JamesHopbourn/matplotlib-with-travis/develop?style=flat-square) ![](https://img.shields.io/github/commit-activity/m/JamesHopbourn/matplotlib-with-travis?logo=green)

[matplotlib with Travis-CI](https://jameshopbourn.github.io/2020/02/16/travis%20with%20matplotlib)

![](https://raw.githubusercontent.com/JamesHopbourn/matplotlib-with-travis/master/Demo.png)

![](https://raw.githubusercontent.com/JamesHopbourn/matplotlib-with-travis/resource/Chinese.png)

### matplotlib tample
```
# -*- coding: UTF-8 -*-
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False


plt.show()
plt.savefig("Filename.png")
```