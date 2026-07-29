import numpy as np

"""  🔷 Bitta faylni saqlash  """

arr = np.arange(10)

#print(np.save('data', arr))  # np.save - faylni saqlash,'data' - fayl nomi 

#print(np.load('data.npy'))   # np.load - faylni o'qish

"""  🔷 Bir necha  faylni saqlash  """ 

arr1 = np.arange(7)

arr2 = np.arange(7,11 )

np.savez('arrays', a=arr1,b=arr2)  # np.savez - bir necha fayl saqlash,'arrays' - fayl nomi
arrays = np.load('arrays.npz')  # .npz yozish shart
print(arrays['a'])  # 'arrays' - fayl ichidagi "a" ni o'qish  
print(arrays['b'])  # 'arrays' - fayl ichidagi "b" ni o'qish 

np.savez_compressed('array_comp.npz', a=arr, b=arr1) ,# fayllarni siqish

