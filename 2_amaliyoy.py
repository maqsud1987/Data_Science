import numpy as np

# 🟢 1_masala
""" Elementlari 0 dan 9 gacha (9 ning o'zi massiv elementiga kirmaydi),
 qadami esa 1 ga teng bo'lgan (3, 3) o'lchamli massiv yaratuvchi 
 funksiyani davom ettiring.  """
 
def nd_array():
  sonlar = np.arange(0,9).reshape(3,3) # .reshape(3,3) 9ta sonni 3 qatorga bo'ladi
  return sonlar
#print(nd_array())


# 🟢 2_masala
""" Yuqorida yaratilgan massivning elementlari 6 va 7 ga teng bo'lgan
 qismini kesib olish funksiyasini davom ettiring. """
 
def sliced_array_2d():
    sonlar = np.arange(0,9).reshape(3,3)
    sliced_array = sonlar[2,:2]
    return sliced_array
#print(sliced_array_2d())


# 🟢 3_masala
"""  Indeks yordamida 3-o'lchamli massivdan elementlarni kesib olish.
Masala : 3-o'lchamli massivni quyidagi listdan yarating, hamda 12, 13, 15,
 va 16 elementlarini kesib oluvchi funksiyani davom ettiring. 
 
   [[[ 0,  1,  2],
               [ 3,  4,  5],
               [ 6,  7,  8]],

              [[ 9, 10, 11],
               [12, 13, 14],
               [15, 16, 17]],

              [[18, 19, 20],
               [21, 22, 23],
               [24, 25, 26]]] """


def sliced_array_3d():
    sonlar_2 = np.arange(0,27).reshape(3,3,3)
    sliced_array = sonlar_2[1,1:3,0:2]   
    return sliced_array
#print(sliced_array_3d())
    
# 🟢 4_masala
""" Boolean indeks yordamida 2 o'lchamli massivlardan Javohir va Elyor
 ismlariga tegishli ma'lumotlarni  kesib olish  """

def boolean_slicing():
    names = np.array(['Hasan', 'Husan', 'Javohir', 'Elyor', 'Hasan', 'Javohir', 'Elyor'])
    data = np.array ( [[5, 6, 1, 1],
                       [9, 1, 1, 1],
                       [7, 7, 4, 2],
                       [1, 5, 1, 9],
                       [9, 9, 4, 5],
                       [7, 5, 9, 6],
                       [5, 3, 7, 4]])
    mask=data[(names=='Javohir') | (names=='Elyor') ] 
    
    return mask
print(boolean_slicing())
    

    

