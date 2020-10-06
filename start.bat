@echo off

echo Projekt z przedmiotu jezyki skryptowe
echo.
:info
echo Dostepne polecenia:
echo start	- uruchamia plik exe oraz generuje raport
echo info	- pokazuje dostepne komendy
echo backup	- generuje backup plikow projektu
echo quit	- zakoncz dzialanie programu

:wybor
echo.
set /p wybor=">> "
if %wybor%==start goto start
if %wybor%==info goto info
if %wybor%==backup goto backup
if %wybor%==quit goto quit
echo Niepoprawne polecenie
goto wybor

:start
echo.
del /q daneWyjsciowe\*
for /r %%v in (daneWejsciowe\*.txt) do call aplikaca_exe\Debug\aplikaca_exe.exe "%%v"
del /q index.html
for /r %%v in (daneWyjsciowe\*.txt) do call python.exe python_raport\python_raport\python_raport.py "%%v"
call index.html
goto wybor

:backup
if not exist backup (mkdir backup)
xcopy /q /y %cd%\index.html %cd%\backup
goto wybor

:quit
pause
echo on
