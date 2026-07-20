@echo off
echo 清理项目文件...

rmdir /s /q cache 2>nul
rmdir /s /q saves 2>nul

del /s /q *.rpyc 2>nul
del /s /q *.rpymc 2>nul

echo 清理完毕！
pause
