import numpy as np

""" Bolean Indekslash """

# Ismlar
names = np.array(['Hasan', 'Husan', 'Mirzabek', 'Elyor', 'Hasan', 'Javohir', 'Elyor'])

data = np.random.randn(7,4)

data[names=='Hasan'] # Hasanga tegishli barcha elementlarni ajratib olish

data[names=="Hasan",1:] # Hasanga tegishli oxirgi 3 ta ustinni ajratib olish

mask = (names =='Hasan') | (names=='Husan') # | pythondagi or "yoki" 


""" data dagi manfiy qiymatlarni 0 ga tenglashtiramiz """

data[data<0] = 0
print(data)


""" Qo'shimcha ishlash,mustahkamlash """

#1 Har kuni sotilgan mahsulot turi
mahsulotlar = np.array(['Non', 'Sut', 'Guruch', 'Non', 'Yog\'', 'Sut', 'Non'])

# Har bir kun uchun 4 xil vaqtda sotilgan miqdor (random sonlar)

savdo = np.random.randn(7,4)

savdo[mahsulotlar =='Non']



#2 do'kondagi mahsulotlarning narxi va sotilgan miqdori (so'mda).

tovarlar = np.array(['Non', 'Sut', 'Non', 'Guruch', 'Sut'])

# Har bir qatorda: [narxi (so'm), sotilgan miqdori (dona)]
sotuv = np.array([
    [3000,  50],    # 0-kun: Non — narxi 3000 so'm, 50 dona sotilgan
    [12000, 20],    # 1-kun: Sut — narxi 12000 so'm, 20 dona sotilgan
    [3000,  45],    # 2-kun: Non — narxi 3000 so'm, 45 dona sotilgan
    [15000, 10],    # 3-kun: Guruch — narxi 15000 so'm, 10 dona sotilgan
    [12000, 25]     # 4-kun: Sut — narxi 12000 so'm, 25 dona sotilgan
])

sotuv[tovarlar == 'Non'] 



