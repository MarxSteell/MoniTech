#!/bin/bash

read VAR

echo "content-type: text/html"
echo

urldecode(){
	echo -e $(sed 's/%/\\x/g')
}

TYPE=$(echo $VAR | cut -d"&" -f1 | cut -d"=" -f2)
IP=$(echo $VAR | cut -d"&" -f2 | cut -d"=" -f2)
INF=$(echo $VAR | cut -d"&" -f3 | cut -d"=" -f2 | urldecode | tr + ' ')
CINF=$(echo $VAR | cut -d"&" -f4 | cut -d"=" -f2 | urldecode | tr + ' ')
CIP=$(grep ";$IP$" equips.csv | cut -d";" -f3)
EINF=$(grep ";$INF$" equips.csv | cut -d";" -f3)
F1=$(grep ";$IP$" equips.csv | cut -d";" -f1)
F2=$(grep ";$IP$" equips.csv | cut -d";" -f2)
F3=$(grep ";$IP$" equips.csv | cut -d";" -f3)

echo "<script lang=javascript>"
if [[ $IP == $CIP ]] ; then
	if [[ $INF != "" ]] ; then
		if [[ $INF == $CINF ]] ; then
			if [[ $TYPE == "name" ]] ; then
				grep -v ";$IP$" equips.csv > equips.new
				grep ";$IP$" equips.csv | sed -e "s/^$F1;/$INF;/g" >> equips.new
				mv equips.new equips.csv
				chmod 777 equips.csv
				echo "$(date);$IP;ALTERADO" >> equip.log
				echo "alert('Equipamento alterado.');"
				echo "location.href='../index.html'"
			elif [[ $TYPE == "local" ]] ; then
				grep -v ";$IP$" equips.csv > equips.new
				grep ";$IP$" equips.csv | sed -e "s/;$F2;/;$INF;/g" >> equips.new
				mv equips.new equips.csv
				chmod 777 equips.csv
				echo "$(date);$IP;ALTERADO" >> equip.log
				echo "alert('Equipamento alterado.');"
				echo "location.href='../index.html'"
			elif [[ $TYPE == "ip" ]] ; then
				if [[ $INF != $EINF ]] ; then
					grep -v ";$IP$" equips.csv > equips.new
					grep ";$IP$" equips.csv | sed -e "s/;$F3$/;$INF/g" >> equips.new
					mv equips.new equips.csv
					chmod 777 equips.csv
					echo "$(date);$IP;ALTERADO" >> equip.log
					echo "alert('Equipamento alterado.');"
					echo "location.href='../index.html'"
				else
					echo "alert('Endereço de IP já adicionado em outro equipamento.');"
					echo "location.href='../index.html'"
				fi
			else
				echo "alert('Campos vazios');"
				echo "location.href='../index.html'"
			fi
		else
			echo "alert('Campos não coincidem-se');"
			echo "location.href='../index.html'"
		fi
	else
		echo "alert('Campos vazios');"
		echo "location.href='../index.html'"
	fi
else
	echo "alert('Campos não coincidem-se');"
	echo "location.href='../index.html'"
fi
echo "</script>"
