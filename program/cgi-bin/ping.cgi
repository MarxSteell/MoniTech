#!/bin/bash
IFS=$'\n'

rm -rf rsimple.log
touch rsimple.log
chmod 777 rsimple.log
for name in $(cat equips.csv | cut -d";" -f1) ; do
	for location in $(grep "^$name;" equips.csv | cut -d";" -f2) ; do	
		for ip in $(grep "^$name;" equips.csv | cut -d";" -f3) ; do
			ping -W 1 -c 1 -i 1 $ip &> /dev/null
			if [[ $? == "0" ]] ; then
				echo "$(date);$name;$location;$ip;UP" >> rdetail.log
				echo "$name;$location;$ip;UP" >> rsimple.log
			else
				echo "$(date);$name;$location;$ip;DOWN" >> rdetail.log
				echo "$name;$location;$ip;DOWN" >> rsimple.log
			fi
		done
	done
done
