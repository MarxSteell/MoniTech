#!/bin/bash

read VAR

echo "content-type: text/html"
echo

IP=$(echo $VAR | cut -d"&" -f1 | cut -d"=" -f2)
CIP=$(echo $VAR | cut -d"&" -f2 | cut -d"=" -f2)

echo "<!DOCTYPE html>"
echo "<head>"
echo "</head>"
echo "<body>"
echo "<script lang='javascript'>"
if [[ $IP != '' ]] ; then
	if [[ $CIP != '' ]] ; then
		if [[ $IP == $CIP ]] ; then
			grep -v ";$IP$" equips.csv > equips.new
			mv equips.new equips.csv
			chmod 777 equips.csv
			echo "$(date);$IP;REMOVIDO" >> equip.log
			echo "alert ('Equipamento removido.');"
			echo "location.href='../index.html'"
		else
			echo "alert ('Campos não coincidem-se.');"
			echo "location.href='../index.html'"
		fi
	else
		echo "alert ('Campos vazios.');"
		echo "location.href='../index.html'"
	fi
else
	echo "alert ('Campos vazios.');"
	echo "location.href='../index.html'"
fi
echo "</script>"
echo "</body>"
echo "</html>"
