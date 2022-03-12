@ECHO OFF
cd ..\env\Scripts
call "activate.bat"
cd ..\..\scrubhubapi
python manage.py runserver