#!/bin/bash

read VAR

echo "content-type: text/html"
echo

urldecode(){
	echo -e $(sed 's/%/\\x/g')
}

EQUIP=$(echo $VAR | cut -d"&" -f1 | cut -d"=" -f2 | tr + ' ' | urldecode)
LOCAL=$(echo $VAR | cut -d"&" -f2 | cut -d"=" -f2 | tr + ' ' | urldecode)
IP=$(echo $VAR | cut -d"&" -f3 | cut -d"=" -f2)
CIP=$(echo $VAR | cut -d"&" -f4 | cut -d"=" -f2)
EIP=$(grep ";$IP$" equips.csv | cut -d";" -f3 )

echo "<script lang=javascript>"
if [[ $EQUIP != "" ]] ; then
	if [[ $LOCAL != "" ]] ; then
		if [[ $IP != "" ]] ; then
			if [[ $CIP != "" ]] ; then
				if [[ $IP == $CIP ]] ; then
					if [[ $IP != $EIP ]] ; then
						echo "$EQUIP;$LOCAL;$IP" >> equips.csv
						echo "$(date);$IP;ADICIONADO" >> equip.log
						echo "alert('Equipamento adicionado.')"
						echo "location.href='../index.html'"
					else
						echo "alert('Endereço de IP já adicionado a outro equipamento.')"
						echo "location.href='../index.html'"
					fi
				else
					echo "alert('Campos não coincidem-se.')"
					echo "location.href='../index.html'"
				fi
			else
				echo "alert('Campos vazios.')"
				echo "location.href='../index.html'"
			fi
			else
			echo "alert('Campos vazios.')"
			echo "location.href='../index.html'"
		fi
	else
		echo "alert('Campos vazios.')"
		echo "location.href='../index.html'"
	fi
else
	echo "alert('Campos vazios.')"
	echo "location.href='../index.html'"
fi
echo "</script>":
