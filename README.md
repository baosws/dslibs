Find yourself doing these over and over again everytime you start a new project or notebook?
```
pip3 install pandas scikit-learn matplotlib numpy statmodels scipy seaborn ...
```
and
```
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy
...
```

**dslibs** eases your pain with an *unified module* that automatically installs and imports frequently used data science modules like numpy, pandas, scikit-learn, etc. in just a sec.

# Installation
```
pip install dslibs-baosws
```

# Usage
Just `from dslibs import *`:
```
>>> from dslibs import *
-------------------------------------------------------
Following modules was installed and imported by dslibs:
"numpy" as "np"
"pandas" as "pd"
"sklearn" as "skl"
"sklearn.preprocessing" as "spp"
"sklearn.model_selection" as "sms"
"sklearn.pipeline" as "spl"
"sklearn.metrics" as "smt"
"sklearn.feature_selection" as "sfs"
"matplotlib.pyplot" as "plt"
"statsmodels.api" as "sma"
"scipy" as "sp"
-------------------------------------------------------
>>>  # now we can use 'pd' without 'import pandas as pd' as usual
>>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
>>> df
A  B
0  1  4
1  2  5
2  3  6
```

# Currently supported imports
| module                    | alias |
|---------------------------|-------|
| numpy                     | np    |
| pandas                    | pd    |
| sklearn                   | skl   |
| sklearn.preprocessing     | spp   |
| sklearn.model_selection   | sms   |
| sklearn.pipeline          | spl   |
| sklearn.metrics           | smt   |
| sklearn.feature_selection | sfs   |
| matplotlib.pyplot         | plt   |
| statsmodels.api           | sma   |
| scipy                     | sp    |
| seaborn                   | sns   |
