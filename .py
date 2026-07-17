# Data Science va Sun'iy Intellekt Praktikum

## Ma'lumotlar tahlili. (NumPy kutubxonasi)

### NumPy kutubxonasini chaqirib olish

import numpy as np

### Python list bilan NumPy kutubxonasidagi massivlar (arraylar) hisoblashlari orasidagi farqni ko'ramiz.

my_list = list(range(100000)) # python list 0~99999 -->Normal

my_array = np.array(range(100000)) # numpy array(massiv) 0~99999 --> Vektorlashgan

%time for _ in range(10): [x*2 for x in my_list] # Normal

%time for _ in range(10): my_array*2 # Vektorlashgan

105/3.14