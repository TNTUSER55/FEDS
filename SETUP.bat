@echo off
cd ..
set place="%CD%"
cls
echo Setting up!
set new=C:\Users\%USERNAME%\Desktop\"Chat Server"
mkdir %new%
xcopy %place% %new% /s /e /v /q
echo.>yes.txt
cls