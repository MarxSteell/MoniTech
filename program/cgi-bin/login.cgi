#!/bin/bash
export LC_COLLATE=C
read VAR

echo "content-type: text/html"
echo

IP=$REMOTE_ADDR
USER=$(echo "$VAR" | cut -d"&" -f1 | cut -d"=" -f2)
PASS=$(echo "$VAR" | cut -d"&" -f2 | cut -d"=" -f2 | sha256sum | cut -d" " -f1)
CUSER=$(grep "^$USER;" users.csv | cut -d";" -f1)
CPASS=$(grep "^$USER;" users.csv | cut -d";" -f2)

echo "<script lang=javascript>"
if [[ $USER == $CUSER ]] ; then
	if [[ $PASS == $CPASS ]] ; then
		grep -v "^$USER;" users.csv > users.new
		grep "^$USER;" users.csv | sed "s/nlogged/logged/g" >> users.new
		mv users.new users.csv
		chmod 777 users.csv
		grep -v "^$USER;" users.csv > users.new
		grep "^$USER;" users.csv | sed "s/IP/$IP/g" >> users.new
		mv users.new users.csv
		chmod 777 users.csv
		echo "$(date);$USER;ON" >> login.log
		echo "location.href='../index.html';"
	else
		echo "alert('Usuário/senha incorreto, por favor tente novamente.');"
		echo "location.href='../index.html'"
	fi
else
	echo "alert('Usuário/senha incorreto, por favor tente novamente.');"
	echo "location.href='../index.html'"
fi
echo "</script>"
