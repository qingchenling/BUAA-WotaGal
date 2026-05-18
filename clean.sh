#!/bin/bash

echo "清理项目文件..."

rm -rf cache
rm -rf saves

find . -name "*.rpyc" -type f -delete
find . -name "*.rpymc" -type f -delete

echo "清理完毕！"
