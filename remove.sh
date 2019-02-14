#!/bin/bash
remove(){
	echo
	echo "Aguarde enquanto os programas são removidos..."
	rm -rf /var/www/html/*
	rm -rf /usr/lib/cgi-bin/*
	apt-get remove apache2 --purge -y
	apt-get purge apache2 -y
	apt-get autoremove -y
	clear
	read -p "Programa desinstalado. Pressione [ENTER] para sair."
	exit 0
}
clear
echo Este desinstalador removerá os seguintes programas:
echo - apache2
echo - MoniTech
echo E excluirá todo o conteúdo das pastas:
echo - /var/www/html
echo - /usr/lib/cgi-bin
echo
read -p "Deseja continuar com desinstalação?(Sim ou Não) " OPTION
case $OPTION in
	[Ss][Ii][Mm]|[Ss]|[Yy][Ee][Ss]|[Yy]) remove ;;
	[Nn][Ãã][Oo]|[Nn][Aa][Oo]|[Nn][Oo]|[Nn]) clear ; exit 0 ;;
	*) read -p "Opção inválida. Pressione [ENTER] para sair." ;;
esac
