#!/bin/bash

echo "content-type: text/html"
echo

IP=$REMOTE_ADDR
USER=$(grep ";$IP;" users.csv | cut -d";" -f1)

grep -v ";$IP;" users.csv > users.new
grep ";$IP;" users.csv | sed -e "s/logged/nlogged/g" >> users.new
mv users.new users.csv
chmod 777 users.csv
grep -v ";$IP;" users.csv > users.new
grep ";$IP;" users.csv | sed -e "s/$IP/IP/g" >> users.new
mv users.new users.csv
chmod 777 users.csv

echo "<script lang=javascript>"
if [[ $? == '0' ]] ; then
	echo "$(date);$USER;OFF" >> login.log
	echo "alert ('Deslogando...');"
	echo "location.href='../index.html'"
fi
echo "</script>"
