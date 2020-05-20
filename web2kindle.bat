@echo off

echo %date%
set YYYYMMDD=%DATE:~0,4%%DATE:~5,2%%DATE:~8,2%
echo %YYYYMMDD%
set _TIME=%TIME:~0,2%%TIME:~3,2%%TIME:~6,2%
set NAME=%YYYYMMDD%%_TIME%
echo %NAME%
rem chcp 65001

setlocal
chcp 65001
set _filename=%~n1
set _extension=%~x1

ebook-convert.exe %1 %1.mobi --filter-css ',background,color,background-color,font-family' --mobi-file-type both --pretty-print 