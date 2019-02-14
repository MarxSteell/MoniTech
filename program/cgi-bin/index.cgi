#!/bin/bash
read VAR

echo "content-type: text/html"
echo

IFS=$'\n'
IP=$REMOTE_ADDR
REDIRECT=$(echo $VAR | cut -d"=" -f2 | sed "s/%2F/\//g")
MENUA=/var/www/html/pages/admin.html
MENUC=/var/www/html/pages/common.html
LOGIN=/var/www/html/pages/login.html
TYPE=$(grep ";$IP;" users.csv | cut -d";" -f4)
STATE=$(grep ";$IP;" users.csv | cut -d";" -f6)

grep ";$IP;" users.csv> /dev/null

if [[ $? == "0" ]] ; then
	if [[ $STATE == "logged" ]] ; then
		if [[ $TYPE == "admin" ]] ; then
			if [[ $REDIRECT == "/usr/lib/cgi-bin/vequip.cgi" ]] ; then
				cat head.log
				echo "<body>"
				echo "<div id=\"table-menu\">"
				echo "<table id=\"response\">"
				echo "<tr>"
				echo "<th>Nome:</th>"
				echo "<th>Localização:</th>"
				echo "<th>Endereço de IP:</th>"
				echo "</tr>"
				for x in $(tail -n15 equips.csv | tac) ; do
					echo "<tr>"
					for y in $(echo $x) ; do
						NAME=$(echo $y | cut -d";" -f1)
						LOCAL=$(echo $y | cut -d";" -f2)
						IP=$(echo $y | cut -d";" -f3)
						echo "<td>$NAME</td>"
						echo "<td>$LOCAL</td>"
						echo "<td>$IP</td>"
					done
					echo "</tr>"
				done
				echo "</table>"
				echo "</div>"
				echo "<div id=\"sidebar\">"
				echo "<div class=\"toggle-btn\" onclick=\"toggleSidebar()\">"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "</div>"
				cat "$MENUA"
				echo "</div>"
				echo "</body>"
				echo "</html>"
			elif [[ $REDIRECT == "/usr/lib/cgi-bin/vuser.cgi" ]] ; then
				cat head.log
				echo "<body>"
				echo "<div id=\"table-menu\">"
				echo "<table>"
				echo "<tr>"
				echo "<th>Nome de usuário:</th>"
				echo "<th>Endereço de e-mail:</th>"
				echo "<th>Tipo de usuário:</th>"
				echo "</tr>"
				for x in $(tail -n10 users.csv | tac) ; do
					echo "<tr>"
					for y in $(echo $x) ; do
						NAME=$(echo $y | cut -d";" -f1)
						EMAIL=$(echo $y | cut -d";" -f3)
						TYPE=$(echo $y | cut -d";" -f4)
						echo "<td>$NAME</td>"
						echo "<td>$EMAIL</td>"
						echo "<td>$TYPE</td>"
					done
					echo "</tr>"
				done
				echo "</table>"
				echo "</div>"
				echo "<div id=\"sidebar\">"
				echo "<div class=\"toggle-btn\" onclick=\"toggleSidebar()\">"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "</div>"
				cat "$MENUA"
				echo "</div>"
				echo "</body>"
				echo "</html>"
			elif [[ $REDIRECT == "/usr/lib/cgi-bin/log/equip.cgi" ]] ; then 
				cat head.log
				echo "<body>"
				echo "<div id=\"table-menu\">"
				echo "<table>"
				echo "<tr>"
				echo "<th>IP:</th>"
				echo "<th>Ação:</th>"
				echo "<th>Data e hora:</th>"
				echo "</tr>"
					
				for x in $(tail -n15 equip.log | tac) ; do
					echo "<tr>"
					for y in $(echo $x) ; do
						NAME=$(echo $y | cut -d";" -f2)
						ACT=$(echo $y | cut -d";" -f3)
						DATE=$(echo $y | cut -d";" -f1)
						echo "<td>$NAME</td>"
						echo "<td>$ACT</td>"
						echo "<td>$DATE</td>"
					done
					echo "</tr>"
				done
				echo "</table>"
				echo "</div>"
				echo "<div id=\"sidebar\">"
				echo "<div class=\"toggle-btn\" onclick=\"toggleSidebar()\">"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "</div>"
				cat "$MENUA"
				echo "</div>"
				echo "</body>"
				echo "</html>"
			elif [[ $REDIRECT == "/usr/lib/cgi-bin/log/user.cgi" ]] ; then 
				cat head.log
				echo "<body>"
				echo "<div id=\"table-menu\">"
				echo "<table>"
				echo "<tr>"
				echo "<th>Nome de usuário:</th>"
				echo "<th>Ação:</th>"
				echo "<th>Data e hora:</th>"
				echo "</tr>"
				for x in $(tail -n15 user.log | tac) ; do
					echo "<tr>"
					for y in $(echo $x) ; do
						NAME=$(echo $y | cut -d";" -f2)
						ACT=$(echo $y | cut -d";" -f3)
						DATE=$(echo $y | cut -d";" -f1)
						echo "<td>$NAME</td>"
						echo "<td>$ACT</td>"
						echo "<td>$DATE</td>"
					done
					echo "</tr>"
				done
				echo "</table>"
				echo "</div>"
				echo "<div id=\"sidebar\">"
				echo "<div class=\"toggle-btn\" onclick=\"toggleSidebar()\">"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "</div>"
				cat "$MENUA"
				echo "</div>"
				echo "</body>"
				echo "</html>"
			elif [[ $REDIRECT == "/usr/lib/cgi-bin/log/login.cgi" ]] ; then 
				cat head.log
				echo "<body>"
				echo "<div id=\"table-menu\">"
				echo "<table>"
				echo "<tr>"
				echo "<th>Nome de usuário:</th>"
				echo "<th>Ação:</th>"
				echo "<th>Data e hora:</th>"
				echo "</tr>"
				for x in $(tail -n15 login.log | tac) ; do
					echo "<tr>"
					for y in $(echo $x) ; do
						NAME=$(echo $y | cut -d";" -f2)
						ACT=$(echo $y | cut -d";" -f3)
						DATE=$(echo $y | cut -d";" -f1)
						echo "<td>$NAME</td>"
						echo "<td>$ACT</td>"
						echo "<td>$DATE</td>"
					done
					echo "</tr>"
				done
				echo "</table>"
				echo "</div>"
				echo "<div id=\"sidebar\">"
				echo "<div class=\"toggle-btn\" onclick=\"toggleSidebar()\">"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "</div>"
				cat "$MENUA"
				echo "</div>"
				echo "</body>"
				echo "</html>"
			elif [[ $REDIRECT == "/var/www/html/pages/aequip.html" ]] ; then
				cat head.log
				echo "<body>"
				echo "<div id=\"sidebar\">"
				echo "<div class=\"toggle-btn\" onclick=\"toggleSidebar()\">"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "</div>"
				cat "$MENUA"
				echo "</div>"
				cat $REDIRECT
				echo "</div>"
			elif [[ $REDIRECT == "/var/www/html/pages/requip.html" ]] ; then
				cat head.log
				echo "<body>"
				echo "<div id=\"sidebar\">"
				echo "<div class=\"toggle-btn\" onclick=\"toggleSidebar()\">"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "</div>"
				cat "$MENUA"
				echo "</div>"
				cat $REDIRECT
			elif [[ $REDIRECT == "/var/www/html/pages/cequip.html" ]] ; then
				cat head.log
				echo "<body>"
				echo "<div id=\"sidebar\">"
				echo "<div class=\"toggle-btn\" onclick=\"toggleSidebar()\">"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "</div>"
				cat "$MENUA"
				echo "</div>"
				cat $REDIRECT
			elif [[ $REDIRECT == "/var/www/html/pages/auser.html" ]] ; then
				cat head.log
				echo "<body>"
				echo "<div id=\"sidebar\">"
				echo "<div class=\"toggle-btn\" onclick=\"toggleSidebar()\">"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "</div>"
				cat "$MENUA"
				echo "</div>"
				cat $REDIRECT
			elif [[ $REDIRECT == "/var/www/html/pages/ruser.html" ]] ; then
				cat head.log
				echo "<body>"
				echo "<div id=\"sidebar\">"
				echo "<div class=\"toggle-btn\" onclick=\"toggleSidebar()\">"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "</div>"
				cat "$MENUA"
				echo "</div>"
				cat $REDIRECT
			elif [[ $REDIRECT == "/var/www/html/pages/cuser.html" ]] ; then
				cat head.log
				echo "<body>"
				echo "<div id=\"sidebar\">"
				echo "<div class=\"toggle-btn\" onclick=\"toggleSidebar()\">"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "</div>"
				cat "$MENUA"
				echo "</div>"
				cat $REDIRECT
			elif [[ $REDIRECT == "/var/www/html/pages/doc.html" ]] ; then
				cat head.log
				echo "<body>"
				echo "<div id=\"sidebar\">"
				echo "<div class=\"toggle-btn\" onclick=\"toggleSidebar()\">"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "</div>"
				cat "$MENUA"
				echo "</div>"
				cat $REDIRECT
			elif [[ $REDIRECT == "/var/www/html/pages/sup.html" ]] ; then
				cat head.log
				echo "<body>"
				echo "<div id=\"sidebar\">"
				echo "<div class=\"toggle-btn\" onclick=\"toggleSidebar()\">"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "</div>"
				cat "$MENUA"
				echo "</div>"
				cat $REDIRECT
			elif [[ $REDIRECT == "Chamado" ]] ; then
				cat head.log
				echo "<body>"
				echo "<div id=\"sidebar\">"
				echo "<div class=\"toggle-btn\" onclick=\"toggleSidebar()\">"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "</div>"
				cat "$MENUA"
				echo "</div>"
				cat "/var/www/html/pages/called.html"
			elif [[ $REDIRECT == "Atualizar" ]] ; then
				echo "<script>"
				echo "location.href='../index.html'"
				echo "</script>"
			elif [[ $REDIRECT == "Detalhes" ]] ; then
				cat head.log
				echo "<body>"
				echo "<div id=\"table-menu\">"
				echo "<table>"
				echo "<tr>"
				echo "<th>Data e hora:</th>"
				echo "<th>Nome:</th>"
				echo "<th>Localização:</th>"
				echo "<th>Endereço de IP:</th>"
				echo "<th>Status:</th>"
				echo "</tr>"
				for x in $(tail -n15 rdetail.log | tac) ; do
					echo "<tr>"
					for y in $(echo $x) ; do
						DATE=$(echo $y | cut -d";" -f1)
						NAME=$(echo $y | cut -d";" -f2)
						LOCAL=$(echo $y | cut -d";" -f3)
						IP=$(echo $y | cut -d";" -f4)
						STATUS=$(echo $y | cut -d";" -f5)
						echo "<td>$DATE</td>"
						echo "<td>$NAME</td>"
						echo "<td>$LOCAL</td>"
						echo "<td>$IP</td>"
						echo "<td>$STATUS</td>"
					done
					echo "</tr>"
				done
				echo "</table>"
				echo "</div>"
				echo "<div id=\"sidebar\">"
				echo "<div class=\"toggle-btn\" onclick=\"toggleSidebar()\">"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "</div>"
				cat "$MENUA"
				echo "</div>"
				echo "</body>"
				echo "</html>"
			else
				cat head.log
				echo "<body>"
				echo "<div id=\"table-menu\">"
				echo "<form method='POST'>"
 				echo "<input type='submit' name='var' value='Iniciar' formaction='serv.cgi'>"
				echo "<input type='submit' name='var' value='Encerrar' formaction='serv.cgi'>"
				echo "<input type='submit' name='var' value='Reiniciar' formaction='serv.cgi'>"
				echo "<input type='submit' name='var' value='Status' formaction='serv.cgi'>"
				echo "<input type='submit' name='var' value='Atualizar' formaction='index.cgi'>"
				echo "<input type='submit' name='var' value='Detalhes' formaction='index.cgi'>"
				echo "<table>"
				echo "<tr>"
				echo "<th>Nome:</th>"
				echo "<th>Localização:</th>"
				echo "<th>Endereço de IP:</th>"
				echo "<th>Status:</th>"
				echo "</tr>"
				for x in $(tail -n15 rsimple.log | tac) ; do
					echo "<tr>"
					for y in $(echo $x) ; do
						NAME=$(echo $y | cut -d";" -f1)
						LOCAL=$(echo $y | cut -d";" -f2)
						IP=$(echo $y | cut -d";" -f3)
						STATUS=$(echo $y | cut -d";" -f4)
						echo "<td>$NAME</td>"
						echo "<td>$LOCAL</td>"
						echo "<td>$IP</td>"
						echo "<td>$STATUS</td>"
					done
					echo "</tr>"
				done
				echo "</table>"
				echo "</form>"
				echo "</div>"
				echo "<div id=\"sidebar\">"
				echo "<div class=\"toggle-btn\" onclick=\"toggleSidebar()\">"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "<span class=\"span\"></span>"
				echo "</div>"
				cat "$MENUA"
				echo "</div>"
				echo "</body>"
				echo "</html>"
			fi
			elif [[ $TYPE == "common" ]] ; then
				if [[ $REDIRECT == "/usr/lib/cgi-bin/vequip.cgi" ]] ; then
					cat head.log
					echo "<body>"
					echo "<div id=\"table-menu\">"
					echo "<table>"
					echo "<tr>"
					echo "<th>Nome:</th>"
					echo "<th>Localização:</th>"
					echo "<th>Endereço de IP:</th>"
					echo "</tr>"
					for x in $(tail -n10 equips.csv | tac) ; do
						echo "<tr>"
						for y in $(echo $x) ; do
							NAME=$(echo $y | cut -d";" -f1)
							LOCAL=$(echo $y | cut -d";" -f2)
							IP=$(echo $y | cut -d";" -f3)
							echo "<td>$NAME</td>"
							echo "<td>$LOCAL</td>"
							echo "<td>$IP</td>"
						done
					echo "</tr>"
					done
					echo "</table>"
					echo "</div>"
					echo "<div id=\"sidebar\">"
					echo "<div class=\"toggle-btn\" onclick=\"toggleSidebar()\">"
					echo "<span></span>"
					echo "<span></span>"
					echo "<span></span>"
					echo "</div>"
					cat "$MENUC"
					echo "</div>"
					echo "</body>"
					echo "</html>"
				elif [[ $REDIRECT == "Detalhes" ]] ; then
					cat head.log
					echo "<body>"
					echo "<div id=\"table-menu\">"
					echo "<table>"
					echo "<tr>"
					echo "<th>Data e hora:</th>"
					echo "<th>Nome:</th>"
					echo "<th>Localização:</th>"
					echo "<th>Endereço de IP:</th>"
					echo "<th>Status:</th>"
					echo "</tr>"
					for x in $(tail -n10 rdetail.log | tac) ; do
						echo "<tr>"
						for y in $(echo $x) ; do
							DATE=$(echo $y | cut -d";" -f1)
							NAME=$(echo $y | cut -d";" -f2)
							LOCAL=$(echo $y | cut -d";" -f3)
							IP=$(echo $y | cut -d";" -f4)
							STATUS=$(echo $y | cut -d";" -f5)
							echo "<td>$DATE</td>"
							echo "<td>$NAME</td>"
							echo "<td>$LOCAL</td>"
							echo "<td>$IP</td>"
							echo "<td>$STATUS</td>"
						done
						echo "</tr>"
					done
					echo "</table>"
					echo "</div>"
					echo "<div id=\"sidebar\">"
					echo "<div class=\"toggle-btn\" onclick=\"toggleSidebar()\">"
					echo "<span></span>"
					echo "<span></span>"
					echo "<span></span>"
					echo "</div>"
					cat "$MENUC"
					echo "</div>"
					echo "</body>"
					echo "</html>"
				elif [[ $REDIRECT == "Atualizar" ]] ; then
					echo "<script>"
					echo "location.href='../index.html'"
					echo "</script>"
				elif [[ $REDIRECT == "/var/www/html/pages/aequip.html" ]] ; then
					cat head.log
					echo "<body>"
					echo "<div id=\"sidebar\">"
					echo "<div class=\"toggle-btn\" onclick=\"toggleSidebar()\">"
					echo "<span class=\"span\"></span>"
					echo "<span class=\"span\"></span>"
					echo "<span class=\"span\"></span>"
					echo "</div>"
					cat "$MENUC"
					echo "</div>"
					cat $REDIRECT
				elif [[ $REDIRECT == "/var/www/html/pages/requip.html" ]] ; then
					cat head.log
					echo "<body>"
					echo "<div id=\"sidebar\">"
					echo "<div class=\"toggle-btn\" onclick=\"toggleSidebar()\">"
					echo "<span class=\"span\"></span>"
					echo "<span class=\"span\"></span>"
					echo "<span class=\"span\"></span>"
					echo "</div>"
					cat "$MENUC"
					echo "</div>"
					cat $REDIRECT
				elif [[ $REDIRECT == "/var/www/html/pages/cequip.html" ]] ; then
					cat head.log
					echo "<body>"
					echo "<div id=\"sidebar\">"
					echo "<div class=\"toggle-btn\" onclick=\"toggleSidebar()\">"
					echo "<span class=\"span\"></span>"
					echo "<span class=\"span\"></span>"
					echo "<span class=\"span\"></span>"
					echo "</div>"
					cat "$MENUC"
					echo "</div>"
					cat $REDIRECT
				elif [[ $REDIRECT == "/var/www/html/pages/doc.html" ]] ; then
					cat head.log
					echo "<body>"
					echo "<div id=\"sidebar\">"
					echo "<div class=\"toggle-btn\" onclick=\"toggleSidebar()\">"
					echo "<span class=\"span\"></span>"
					echo "<span class=\"span\"></span>"
					echo "<span class=\"span\"></span>"
					echo "</div>"
					cat "$MENUC"
					echo "</div>"
					cat $REDIRECT
				else
					cat head.log
					echo "<body>"
					echo "<div id=\"table-menu\">"
					echo "<form method='POST'>"
					echo "<input type='submit' name='var' value='Iniciar' formaction='serv.cgi'>"
					echo "<input type='submit' name='var' value='Encerrar' formaction='serv.cgi'>"
					echo "<input type='submit' name='var' value='Reiniciar' formaction='serv.cgi'>"
					echo "<input type='submit' name='var' value='Status' formaction='serv.cgi'>"
					echo "<input type='submit' name='var' value='Atualizar' formaction='index.cgi'>"
					echo "<input type='submit' name='var' value='Detalhes' formaction='index.cgi'>"
					echo "<table>"
					echo "<tr>"
					echo "<th>Nome:</th>"
					echo "<th>Localização:</th>"
					echo "<th>Endereço de IP:</th>"
					echo "<th>Status:</th>"
					echo "</tr>"
					for x in $(tail -n10 rsimple.log | tac) ; do
						echo "<tr>"
						for y in $(echo $x) ; do
							NAME=$(echo $y | cut -d";" -f1)
							LOCAL=$(echo $y | cut -d";" -f2)
							IP=$(echo $y | cut -d";" -f3)
							STATUS=$(echo $y | cut -d";" -f4)
							echo "<td>$NAME</td>"
							echo "<td>$LOCAL</td>"
							echo "<td>$IP</td>"
							echo "<td>$STATUS</td>"
						done
						echo "</tr>"
					done	
					echo "</table>"
					echo "</form>"
					echo "</div>"
					echo "<div id=\"sidebar\">"
					echo "<div class=\"toggle-btn\" onclick=\"toggleSidebar()\">"
					echo "<span></span>"
					echo "<span></span>"
					echo "<span></span>"
					echo "</div>"
					cat "$MENUC"
					echo "</div>"
					echo "</body>"
					echo "</html>"
				fi
			else
				cat $LOGIN
			fi
		else
			cat $LOGIN
		fi
	else
		cat $LOGIN
	fi
