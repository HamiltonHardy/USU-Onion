## USU-Onion
## Dev for an unofficial USU Free Software and Linux Onion Site



## Intall on Debian/Ubuntu

## Install dependencies
sudo apt install tor nginx git -y

## Edit the following config file with nano or your preferred text editor:
sudo nano /etc/tor/torrc
## You're going to want to uncomment the following lines of the config file:
#HiddenServiceDir /var/lib/tor/hidden_service/
#HiddenServicePort 80 127.0.0.1:80

## Restart Tor
sudo service tor stop
sudo service tor start

## Edit the following config file with nano or your preferred text editor:
sudo nano /etc/nginx/nginx.conf
## You're going to want to uncomment the following line of the config file:
# server_tokens off;
## Add the following line just below the previous one:
# port_in_redirect off;
## Just below, you're going to want to uncomment the following line of the config file:
# server_name_in_redirect off;

## Clone the repository
cd /var/www
git clone https://github.com/KuzonFyre/USU-Onion.git

## Start nginx
sudo service nginx start



## To view the .onion url
sudo cat /var/lib/tor/hidden_service/hostname

## Other useful resources:
## Vanity onion address generator: https://github.com/cathugger/mkp224o
## i put a DARK WEB website on a Raspberry Pi!! - Network Chuck: https://yewtu.be/watch?v=bllS9tkCkaM
