#!/bin/bash
instala(){
	echo
	echo "Aguarde enquanto o programa é instalado..."
	apt-get update
	if [[ $? == '0' ]] ; then
		rm -rf /var/www/html/*
		rm -rf /usr/lib/cgi-bin/*
		apt-get install apache2 -y
		echo "AddDefaultCharset UTF-8" >> /etc/apache2/conf-enabled/charset.conf
		a2enmod cgid &> /dev/null
		systemctl restart apache2 
		cp -rf ./program/html/* /var/www/html
		cp -rf ./program/cgi-bin/* /usr/lib/cgi-bin
		ln -s '/usr/lib/cgi-bin' /var/www/html/cgi-bin
		chmod 777 /var/www/html/*
		chmod 777 /usr/lib/cgi-bin/*
		clear
		read -p "Programa instalado. Pressione [ENTER] sair do instalador."
		exit 0
	else
		read -p "Verifique sua conectividade. Pressione [ENTER] para sair do instalador."
		exit 0
	fi
}
clear
echo Este executável instalará os programas:
echo - apache2;
echo - MoniTech.
echo E excluirá todo o conteúdo, caso haja algum, das pastas:
echo - /var/www/html;
echo - /usr/lib/cgi-bin.
echo
read -p "Deseja continuar com a instalação?(Sim ou Não) " OPTION
case $OPTION in
	[Ss][Ii][Mm]|[Ss]|[Yy][Ee][Ss]|[Yy]) instala ;;
	[Nn][Ãã][Oo]|[Nn][Aa][Oo]|[Nn]|[Nn][Oo]) clear ; exit 0 ;;
	*) read -p "Opção inválida. Pressione [ENTER] para sair..."
esac
