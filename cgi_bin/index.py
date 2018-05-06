# -*- coding: UTF-8 -*-
# filename:test.py


import os

print("Content-type: text/html")
print()
print("<br/>")
radius=0
c_length=0
if REQUEST_METHOD" == "POST" ]];then
    read vars
    echo "$vars" | awk -F "=" '{print $2}' > temp
    dos2unix temp
    radius=`cat temp`
    c_length=$(echo "scale=2;2*3.14*$radius" | bc)

    echo "<br/>"
    echo "<table border="5" cellpadding="10">"
    echo "Userid Info:"
    echo "<tr>"
    echo "<td>半径</td><td>周长</td>"
    echo "</tr>"
    echo "<tr>"
    echo "<td>"$radius"</td><td>"$c_length"</td>"
    echo "</tr>"
    echo "</table>" 
"""
#!/bin/bash

mysql_bin=/home/work/mysql/bin/mysql

echo "Content-Type:text/html; Charset=gbk"
echo ""

echo "<br/>"
radius=0
c_length=0
if [[ "$REQUEST_METHOD" == "POST" ]];then
    read vars
    echo "$vars" | awk -F "=" '{print $2}' > temp
    dos2unix temp
    radius=`cat temp`
    c_length=$(echo "scale=2;2*3.14*$radius" | bc)

    echo "<br/>"
    echo "<table border="5" cellpadding="10">"
    echo "Userid Info:"
    echo "<tr>"
    echo "<td>半径</td><td>周长</td>"
    echo "</tr>"
    echo "<tr>"
    echo "<td>"$radius"</td><td>"$c_length"</td>"
    echo "</tr>"
    echo "</table>"
fi
"""