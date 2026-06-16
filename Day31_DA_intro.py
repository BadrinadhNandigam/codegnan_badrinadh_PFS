'''

Data Analysis

> This is the process of inspection, cleaninng, transforming, and modeling data to discover
useful insights

Types of DA
-------------------

1. Descriptive Analysis
----------------------------------
> Summarizing the data

2, Diagnostic Analysis
----------------------------------
> Understanding causes

3. Predictive Analysis
----------------------------------
> Forcasting future outcomes

4. Prescriptive Analysis
-----------------------------------

>Suggesting actions based on data


Why DA
----------------

> To improve Decision making
> Detects Trends & Patterns


Numpy
---------
> This python library for numerical computing. it improves support for multi dimensional
arrays, and linear algebra operations, making it essential for data analysis


using numpy in DA
-----------------------

> improved performance
> simplifies complex operations
> Easy data manipulation

'''
'''
import numpy as np
aa = np.array([1,2,3,4])
print(aa)
'''

'''
import numpy as np
aa = np.array([[4,5,6,7],
              [1,2,3,4],
               [56,75,23,11]])
print(aa)
'''

'''
import numpy as np
aa = np.array([[1,2,3],[332,432,533]])
print(aa)
print(aa.shape)
reshape  = aa.reshape(3,2)
print(reshape)

,'''

'''
import numpy as np
aa = np.array([10,20,30,40])
print(f"orginal array {aa}")
print(f"updated array {aa + 5}")

'''

'''
import numpy as np
aa1 =  np.array([[1,2],[3,4]])
aa2 = np.array([[5,6],[7,8]])
print(np.dot(aa1,aa2))

'''
'''
Pandas
--------------
pandas is a powerfull data manipulation and analysis library

it provides data structure like series and dataframe for efficient data handling



import pandas as pd
aa = pd.series([2999, 15999, 4999, 1999], index =['earbuds', 'smartphone', 'laptop','watch','shirt'])
print(aa)

methods series
-----------------

mean()
sum()
max()
min()
apply()
map()


dataframe
-----------------

'''
import pandas as pd

data = {
    'product' : ['earbuds','smartphone', 'laptop', 'watch', 'footware'],
    'brand' : ['Noise', 'Vivo', 'Hp', 'bOLT','nike'],
    'Price' : [1555,33433,32234,9999,44555],
    'stock' : [50,15,23,40,70]
    }
dip = pd.DataFrame(data)
print(dip)

