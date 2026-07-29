import numpy as np


""" 🔷   `unique` va `in1d` `setdiff1d` va boshqa usullari haqida """


names = np.array(['Sarvar', 'Abdurahmon', 'Hasan',  'Temur', 'Sarvar', 'Temur'])
ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])


""""  ▷   ------  `unique`  usuli ------  """

#print(np.unique(names)) # names dagi takrorlanmas elementlarni qaytaradi (takrorlansa ham faqat bittasini qabul qiladi)

#print(set(names)) # names dagi unique(takrorlanmas) elementlarni qaytaradi

### `isin` usuli haqida


""""  ▷   ------  `data`  usuli------  """


arr1 = np.array([6, 0, 0, 3, 2, 5, 6])
arr2 = np.array([0, 2, 3])

#print(np.isin(arr1, arr2)) # arr2 dagi elementlarni arr1 da mavjudligini tekshirish


""""  ▷   ------  `setdiff1d` usuli ------  """

#data
names1 = np.array(['Jasur', 'Abdurahmon', 'Hasan',  'Muhammad', 'Sarvar', 'Temur'])
names2 = np.array(['Sarvar', 'Abdurahmon', 'Hasan',  'Temur', 'Sarvar', 'Temur'])

print(np.setdiff1d(names1, names2)) # names1 massivining names2 massividagi takrorlanmas qismini qaytaradi
