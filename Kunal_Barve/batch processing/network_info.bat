
@echo off
cls

echo Local IP addresses:
ipconfig | findstr /R "IPv4 Address"

echo Available ports:
netstat -an | findstr /R /C:"^  TCP" /C:"^  UDP" /C:"LISTENING"
