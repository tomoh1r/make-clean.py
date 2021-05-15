# make-clean

Make clean your files. [![Test result badge.](https://github.com/tomoh1r/make-clean.py/workflows/test/badge.svg)](https://github.com/tomoh1r/make-clean.py/actions?query=workflow%3Atest)

---

If one'd like to make sphinx repository with github-pages sumodule, one shoud
exclude rm `_build/html/.git`.

`make-clean` package provide to keep `.git` file with it.

Switch `make.bat` file clean to below

```bat
if "%1" == "clean" (
    .\path\to\make-clean.exe _build -i _build\html\.git _build\html\.gitignore
    goto end
)
```

## Usage

This package has a `make-clean` command.

```bat
> .\venv\Scripts\make-clean.exe -h
usage: make-clean-script.py [-h] [--clean-ignore CLEAN_IGNORE]
                            [-i [IGNORE [IGNORE ...]]]
                            TARGET_DIR [TARGET_DIR ...]

clean target dir without ignores

positional arguments:
  TARGET_DIR            dir to remove recursively

optional arguments:
  -h, --help            show this help message and exit
  --clean-ignore CLEAN_IGNORE
                        dir/file file to ignore from remove
  -i [IGNORE [IGNORE ...]], --ignores [IGNORE [IGNORE ...]]
                        dir/file to ignore from remove
```
