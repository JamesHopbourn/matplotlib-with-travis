# -*- coding: UTF-8 -*-
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt 
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签 
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号 #有中文出现的情况，需要u'内容' 

plt.clf()  # 清空画布
plt.plot([1, 2, 3, 9], [8, 5, 7, 4])
plt.xlabel(u'横轴 Row')
plt.ylabel(u'纵轴 Column')
plt.title(u'中文标题')
plt.show()
plt.savefig("Chinese.png")
