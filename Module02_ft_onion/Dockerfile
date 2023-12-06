FROM    debian:buster

# tor install tutorial : https://support.torproject.org/apt/

RUN	apt update -y \
        && apt upgrade -y \		
	&& apt install apt-transport-https gpg wget nginx openssh-server -y

RUN     touch /etc/apt/sources.list.d/tor.list && chmod 755 /etc/apt/sources.list.d/tor.list \
        && echo "deb [signed-by=/usr/share/keyrings/tor-archive-keyring.gpg] https://deb.torproject.org/torproject.org buster main" >> /etc/apt/sources.list.d/tor.list \
        && echo "deb-src [signed-by=/usr/share/keyrings/tor-archive-keyring.gpg] https://deb.torproject.org/torproject.org buster main" >> /etc/apt/sources.list.d/tor.list

RUN    	wget -qO- https://deb.torproject.org/torproject.org/A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89.asc | gpg --dearmor | tee /usr/share/keyrings/tor-archive-keyring.gpg >/dev/null

RUN     apt update -y \
        && apt install tor deb.torproject.org-keyring -y

RUN     chmod 777 /var/www/html

RUN     useradd -m tczarnia && echo "tczarnia:pass" | chpasswd
# in order to activate root in the docket to see the onion hostname
RUN     echo "root:pass" | chpasswd

COPY    ./conf/nginx.conf /etc/nginx/nginx.conf
COPY    ./html/index.html /var/www/html/index.html
COPY    ./conf/torrc /etc/tor/torrc
COPY	./launch.sh launch.sh
COPY    ./conf/sshd_config /etc/ssh/sshd_config

RUN 	chmod 700 launch.sh
RUN     chmod -R 755 /var/lib/tor

EXPOSE  80
EXPOSE  4242

ENTRYPOINT [ "/bin/sh", "./launch.sh" ]

