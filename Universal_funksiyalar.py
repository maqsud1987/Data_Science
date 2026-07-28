import numpy as np

# Universal funksiyalar
""" 🔷---1-qism--- Unary - funksiyalar (BITTA ARGUMENT QABUL QILUVCHI FUNKSIYA !!!)
sqrt, square, exp, log, modf, sign, isnan funksiyalarini ko'rib chiqamiz """


"""  ▶ sqrt - massivning xar bir elementini kvadrat ildizni qaytaradi """

arr = np.arange(10) # 0 ~ 10 gacha bo'lgan elementlardan iborat massivni qaytaradi
# Natija: arr = array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 


#print(np.sqrt(arr)) # arr nomli massivning barcha elementlaridan kv ildizni qaytaradi
# Natija: array([0.        , 1.        , 1.41421356, 1.73205081, 2.        ,
#      2.23606798, 2.44948974, 2.64575131, 2.82842712, 3.        ])



"""  ▶  square -  massivning xar bir elementini kvadratga oshiradi """

#print(np.square(arr)) # arr nomli massivning barcha elementlarini kvadratga oshiradi"""
# array([ 0,  1,  4,  9, 16, 25, 36, 49, 64, 81])



"""  ▶  exp -  massivning xar bir elementini eksponentini qaytaradi(e ding darajasi)  """

#print(np.exp(arr)) # arr nomli massivning barcha elementlarini eksponentini qaytaradi
# Natija: array([1.00000000e+00, 2.71828183e+00, 7.38905610e+00, 2.00855369e+01,
#        5.45981500e+01, 1.48413159e+02, 4.03428793e+02, 1.09663316e+03,
#        2.98095799e+03, 8.10308393e+03])



"""  ▶  log -  massivning xar bir logorifmini hisoblaydi """


#print(np.log(arr[1:]))# arr nomli massivning 0-elementdan tashqari barcha elementlarini logarifmini hisoblaydi (loge)
# array([0.        , 0.69314718, 1.09861229, 1.38629436, 1.60943791,
#        1.79175947, 1.94591015, 2.07944154, 2.19722458])


"""  ▶  modf bu funksiya haqiqiy sonlarni butun va qoldiq qismlarini ajratib beruvchi funksiya """

arr1 = np.random.randn(6) # 6 ta elementdan iborat taxminiy qiymatlarga ega massiv

qoldiq, butun = np.modf(arr1) # arr1 ning elementlarini qoldiq va butun qismlarini ikkita massivga ajratadi

# print(arr1)
# print(qoldiq)
# print(butun)
# Natija: [ 1.37224881  0.36898177 -0.12557477  1.12301239  0.26202445  1.05226027]
# Natija: [ 0.37224881  0.36898177 -0.12557477  0.12301239  0.26202445  0.05226027]
# Natija: [ 1.  0. -0.  1.  0.  1.]


"""  ▶  sign funkisyasi massiv elementlarini qiymati manfiy bo'lsa -1 va aksincha musbat bo'lsa 1 ni qaytaradi """

# print(arr1)
# print(np.sign(arr1)) # arr1 massivining elementlari ishoralarini "-1" va "1" ko'rinishida qaytaradi
# array([-1., -1.,  1., -1.,  1., -1.])



"""  ▶  isnan massivning elementlarida NaN ma'lumoti bo'lsa True qaytaradi va aksincha esa False qaytaradi """

print(np.isnan(arr1))
# [ ]
# arr1
# array([-1.55984491, -1.00792088,  0.54385383, -1.67291197,  0.1819676 ,
#        -0.63434352])

# [ ]
# array([False, False, False, False, False, False])

# [ ]
# arr1[0]=np.nan # 0- elementimizni nan ga almashtirish

# [ ]
# array([        nan, -1.00792088,  0.54385383, -1.67291197,  0.1819676 ,
#        -0.63434352])

# [ ]
# array([ True, False, False, False, False, False])




""" 🔷 ---2-qism--- Binary funksiyalar (BITTA ARGUMENT QABUL QILUVCHI FUNKSIYA !!!)
add, multiply, maximum funksiyalarini ko'rib chiqamiz  """

"""  ▶  add ikkita massivning mos elementlarini qo'shadi """


# 2 ta massivni yaratib olamiz
arr2 = np.random.randn(6)
arr3 = np.random.randn(6)


arr2
array([-1.37877748, -2.53283183, -0.23133261, -0.98076854,  0.31526706,
        2.45709817])


arr3
array([ 1.26554277, -0.09554287,  0.60491629,  0.71631161,  0.38196717,
        1.59739969])

[ ]
np.add(arr2, arr3) # arr2 va arr3 ning elementlarini mos ravishda qo'shib beradi
array([-0.1132347 , -2.62837469,  0.37358368, -0.26445693,  0.69723423,
        4.05449787])

[ ]
arr2 + arr3 # arr2 va arr3 ning elementlarini mos ravishda qo'shib beradi
array([-0.1132347 , -2.62837469,  0.37358368, -0.26445693,  0.69723423,
        4.05449787])

"""  ▶  multiply ikkita massivning mos elementlarini ko'paytiradi """

[ ]
arr2
array([-1.37877748, -2.53283183, -0.23133261, -0.98076854,  0.31526706,
        2.45709817])

[ ]
arr3
array([ 1.26554277, -0.09554287,  0.60491629,  0.71631161,  0.38196717,
        1.59739969])

[ ]
np.multiply(arr2, arr3) # arr2 va arr3 ning mos elementlarini ko'paytiradi
array([-1.74490187,  0.24199402, -0.13993687, -0.7025359 ,  0.12042167,
        3.92496787])


maximum ikkita massivning elementlarini taqqoslab ulardan kattasining qiymatini qaytaradi

[ ]
array([ 1.26554277, -0.09554287,  0.60491629,  0.71631161,  0.38196717,
        2.45709817])


