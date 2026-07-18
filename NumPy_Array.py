import numpy as np

# massiv ko'rinishidagi ma'lumotlarni yaratish

data1=[3.5,5,6,2]  #list
arr1=np.array(data1)  #array1    🟢 1 o'lchamli massiv

data2 = (2,3,8,-10)  # tuple      🟢 1 o'lchamli massiv
arr2 = np.array(data2)

data3 = [[-2,6,50.5],[6,8,-1]] #list ichidagi list  🟢 2 o'lchamli massiv
arr3 =np.array(data3)

data4 =[[[1, 2], [3, 4]], # 1-jadval
    [[5, 6], [7, 8]]    # 2-jadval
]  # 🟢 3 o'lchamli massiv
arr4 = np.array(data4)


# shape va size metodlari
# shape metodi massivning qator va ustunlar sonini ko'rsatsa, 
#  size esa massivlardagi elementlar sonini nomoyon etadi

arr3.shape # qator va ustunlar sonini ko'rsatadi (q, u)
(2, 4)

arr3.size # array3 ning elementlar soni 
8

# N-o'lchamli massivlar yaratishning boshqa usullari
# zeros va ones funksiyalari yordamida massivlar yaratish

arr4 = np.zeros((2, 4)) # barcha elemtlari 0 ga teng bo'lgan (2, 4)
arr4 
#array([[0., 0., 0., 0.],
#      [0., 0., 0., 0.]])


# random funksiyasi yordamida yaratish (rand, randint, randn)


