echo off

REM set /p file=Enter file name:
set file=%1
set backend=%2
cd %backend%
echo File is %file%
echo "Processing .3ds..."
node %backend%\decompile.js %file%
echo "Plottting..."
python %backend%\draw.py
echo "Calculating area..."
python %backend%\area.py
pause