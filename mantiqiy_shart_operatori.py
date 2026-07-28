import numpy as np


""" 🔷   Mantiqiy shart operatorlarni massiv operator sifatida qo'llash """

"""  ▶  Shart operatori sifatida `where` dan foydalanish """

### Tassavur qiling bizda ikkita ma'lumotlar (massivlar) mavjud bular:
###   `xarr` va `yarr`. Agarda shart `True`ni qanoatlantirsa `xarr` 
###  elementini qabul qilgan aksincha esa `yarr` elementini qabul qilgan yangi
###  massiv hosil qilinsin.

#1 Massivlar
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5]) # xarr
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5]) # yarr

# Shart
cond = np.array([True, False, True, True, False]) # condition(cond) - holat

# where
result = np.where(cond, xarr, yarr) # cond==True : xarr elementi, cond==False : yarr elementi
result


#2
#arr = np.random.randn(4, 4)  # (4, 4) taxminiy massiv


# where
#results = np.where(arr<0, -2, 2) # arr ning manfiy elementlarini -2 ga musbat elementlarin esa 2 ga almashitirish
#results


#3
arr1 = np.random.randn(3,3)
rezult1 = np.where(arr1<0,0, 1)