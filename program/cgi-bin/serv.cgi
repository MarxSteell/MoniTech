#!/bin/bash

read VAR

echo "content-type: text/html"
echo

VAR=$(echo $VAR | cut -d"=" -f2)

iniciar(){
	./pingd.cgi &> /dev/null
}
encerrar(){
	killall pingd.cgi
}

echo "<html>"
echo "<head>"
echo "</head>"
echo "<body>"
echo "<script lang='javascript'>"
case $VAR in
	Iniciar)
		iniciar &> /dev/null
		echo "alert('Monitoramento iniciado.');"
		echo "location.href='../index.html'"
		;;
	Encerrar)
		encerrar
		echo "alert('Monitoramento encerrado.');"
		echo "location.href='../index.html'"
		;;
	Reiniciar)
		encerrar
		iniciar
		;;
	Status)
		ps -ef | grep "./pingd.cgi$" &> /dev/null
		if [[ $? == "0" ]] ; then
			echo "alert ('Monitoramento está em funcionamento.');"
			echo "location.href='../index.html'"
		else
			echo "alert ('Monitoramento está desligado.');"
			echo "location.href='../index.html'"
		fi
		;;
esac
echo "</script>"
echo "</body>"
echo "</html>"
