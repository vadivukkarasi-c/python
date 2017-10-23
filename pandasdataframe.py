dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
import numpy as np

brics = pd.DataFrame(dict)
print(brics)

data = np.array([['','Col1','Col2','Col3','Col4','Col5'],
                ['Row1',1,2,3,4,5],
                ['Row2',3,4,5,6,7]])
                
print(pd.DataFrame(data=data[1:,1:],
                  index=data[1:,0],
                  columns=data[0,1:]))
b1 = data[:4, 0:1]
b2 = data[0,4]
print(b1)
print(b2)
s = pd.Series()
print(s)
