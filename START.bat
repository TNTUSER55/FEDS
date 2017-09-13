@echo off

if exist yes.txt (
	cd py
	goto :sub_run
) else (
	echo PLEASE RUN SUTUP.bat
)


:sub_run
cls
python client.py
pause