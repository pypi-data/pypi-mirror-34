rem SET TOTALPHASEPATH=Y:\project\tools\TotalPhase
rem SET TOTALPHASEPATH=D:\TotalPhase
    SET TOTALPHASEPATH=%CD%\..\..\tools\TotalPhase

rem SET MYPYPATH=%HOMEDRIVE%%HOMEPATH%\Dropbox\script\python
rem SET MYPYPATH=E:\Dropbox\script\python
rem SET MYPY=%MYPYPATH%\cynpy

    SET PYTHONPATH=%TOTALPHASEPATH%\aardvark-api-windows-i686-v5.13\python
rem SET PYTHONPATH=%CD%;%MYPYPATH%;%TOTALPHASEPATH%\aardvark-api-windows-x86_64-v5.13\python

    dir/w %PYTHONPATH%

rem @PATH=%CD%;%PATH%
