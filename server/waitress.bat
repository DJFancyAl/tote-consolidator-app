@echo off

rem Set the path to your Python interpreter.
set PYTHONPATH=C:\Users\ablue\Documents\Marker Systems\tote_consolidator\server\venv\Scripts

rem Activate the venv.
call .\venv\Scripts\activate

rem Run your Python script.
py waitress_server.py
