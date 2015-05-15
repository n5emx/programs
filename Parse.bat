@echo off
echo Repositories Available
cd\version-control
dir /b /ad
pause
REM call c:\python34\pythonw.exe

c:\python34\python.exe c:\scripts\parsecfg.py
