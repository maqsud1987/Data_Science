import numpy as np

# N-o'lchamli massiv (array)larga ishlov berish
""" Indeks va kesib olish asoslari"""

arr = np.arange(10,100,10 )
sliced_arr = arr[3:5]
sliced_arr[:]=0
#print(arr)

""" copy - usuli """

arr1 = np.arange(10,100,10 )
sliced_arr1 =arr1[3:5].copy()

sliced_arr1[:]=0

# print(arr1)
# print(sliced_arr1)

""" 2 o'lchamli (2d array) massivlarda indeks va kesib olish """

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr2d)
# print(arr2d[2,2])

""" 2-o'lchamli massivlarning bir nechta elementlarini kesib olish """

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
sl_arr2d=arr2d[2,1:]
#print(sl_arr2d)

""" 3-o'lchamli (3d array) massivlarda indeks va kesib olish asoslari """

arr3d = np.array([[[ 0,  1,  2],
                   [ 3,  4,  5],
                   [ 6,  7,  8]],

                  [[ 9, 10, 11],
                   [12, 13, 14],
                   [15, 16, 17]],

                  [[18, 19, 20],
                   [21, 22, 23],
                   [24, 25, 26]]])

print(arr3d[2][2,0])









