==========
make-clean
==========

If one'd like to make sphinx repository with github-pages sumodule, one shoud
exclude rm ``_build/html/.git``.

``make-clean`` package provide to keep ``.git`` file with it.

Switch ``make.bat`` file clean to below::

  if "%1" == "clean" (
  	.\path\to\make-clean.exe _build --excludes _build\html\.git _build\html\.gitignore
  	goto end
  )
