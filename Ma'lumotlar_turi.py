import numpy as np

# Massivlar yaratishda ma'lumot turlarini aniq kiritish, ma'lumot turlarini aniqlash, 
# bir turdagi ma'lumot turidan ikkinchi turdagi ma'lumot turiga o'girish

# 🟢 dtype — massiv ichidagi barcha elementlarning qanday tur ekanini ko'rsatadi.

# 🟩 dtype=np.float64 — massivni yaratishda majburiy ravishda qanday tur bilan saqlash kerakligini ko'rsatadi.

arr1 = np.array([1,2,3],dtype=np.float64) # float645 ma'lumotlar turiga ega massiv

arr2 = np.array([1,2,3],dtype = np.int32) # integer ma'lumotlar turiga ega massiv



# 🔵 astype — bu haqiqiy metod (qavs bilan chaqiriladi), va u mavjud massivning turini boshqa turga o'zgartirib, yangi massiv qaytaradi.

arr = np.array([1,2,3,4]) # type=np.float64  berilmasa,majburiy int64 ni beradi 
#print(arr.dtype)  #  int64


arr3 = np.array([3.4,2.06,3.12,5])
data = arr3.astype( dtype = np.int64)
print(data)