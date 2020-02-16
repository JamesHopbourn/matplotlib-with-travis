# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt 
import matplotlib
myfont = matplotlib.font_manager.FontProperties(fname=r"./SimHei.ttfF")  #fname指定字体文件  选简体显示中文

#plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签 

plt.rcParams['axes.unicode_minus']=False #用来正常显示负号 #有中文出现的情况，需要u'内容' 

plt.clf()  # 清空画布
plt.plot([1, 2, 3], [4, 5, 6])
plt.xlabel(u'横轴')
plt.ylabel(u'纵轴')
plt.title(u'中文标题')
plt.savefig("Chinese.png")
plt.show()

