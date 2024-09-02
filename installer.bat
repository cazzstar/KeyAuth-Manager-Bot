@echo off
echo Installing dependencies...
echo.

pip uninstall discord -y
cls
pip uninstall py-cord -y
cls
pip install discord
cls
pip install py-cord
cls
pip uninstall discord -y

echo.
echo Dependencies installed.
pause
