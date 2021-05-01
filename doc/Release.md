# Release

Setup.

```bat
> python3.X.exe -m venv --clear venv
> .\venv\Scripts\python.exe -m pip install -U setuptools pip
> .\venv\Scripts\python.exe -m pip install -e .[release]
```

Build it.

```bat
> .\venv\Scripts\python.exe setup.py sdist
```

Release it.

```bat
> .\venv\Scripts\python.exe -m twine upload -r testpypi dist/*
> .\venv\Scripts\python.exe -m twine upload dist/*
```
