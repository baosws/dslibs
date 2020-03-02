import importlib

imports = {
    'numpy': 'np',
    'pandas': 'pd',
    'sklearn': 'skl',
    'sklearn.preprocessing': 'spp',
    'sklearn.model_selection': 'sms',
    'sklearn.pipeline': 'spl',
    'sklearn.metrics': 'smt',
    'sklearn.feature_selection': 'sfs',
    'matplotlib.pyplot': 'plt',
    'statsmodels.api': 'sma',
    'scipy': 'sp',
    'seaborn': 'sns',
}

title = 'Following modules was installed and imported by dslibs:'
print('-' * len(title), title, sep = '\n')
for package, alias in imports.items():
    print(f'"{package}" as "{alias}"')
    alias = alias if alias else package
    globals()[alias] = importlib.import_module(package)
print('-' * len(title))

__all__ = list(imports.values())
