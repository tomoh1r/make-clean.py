# UnitTest

I use [pytest](http://doc.pytest.org/en/latest/).

Setup.

```bat
> python3.X.exe -m venv --clear venv
> .\venv\Scripts\python.exe -m pip install -U setuptools pip
> .\venv\Scripts\python.exe -m pip install -e .[dev]
```

Test it.

```bat
> .\venv\Scripts\python.exe -m pytest
```
