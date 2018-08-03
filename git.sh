#!/bin/bash
echo "git operation"
if [ $1 = 'push' ]
then
    read -p '输入commit参数>>>:' commitarg
    git add -A
    git commit -m  ${commitarg}
    git push origin master
elif test $1 == pull
then
    echo 'pull.....'
    git pull origin master 
fi
