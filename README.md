This is an unified package that installs and imports frequently used data science packages like numpy, pandas, scikit-learn, etc.

# Installation
dslibs is currently availiable on PyPI only:
```
pip install dslibs-baosws
```

# Usage
Just `from dslibs import *`. Now you have your extensively used libraries imported with compact aliases very quickly:
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
>>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}) # notice that we can use 'pd' now without needing 'import pandas as pd' as usual
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
