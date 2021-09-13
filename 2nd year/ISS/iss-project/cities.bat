@ECHO OFF

FOR /F "tokens=3,4 delims=," %%a IN (cities.txt) DO (
    ECHO %%a,%%b >> orase_judete.txt
)