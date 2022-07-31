# this script runs on ubuntu
#!bash
apt-get update && apt-get install -y locales
apt-get install -y make git unzip gcc
mkdir /home/dev && cd /home/dev
git clone https://github.com/wg/wrk.git
cd wrk && make
ln ./wrk /usr/local/bin
apt-get install -y python3 python3-pip
pip install fastapi[all]
apt-get install -y inetutils-ping
pip install fabric
apt-get install -y iperf3 nmap
apt-get install -y sudo curl


# nodejs
curl -fsSL https://deb.nodesource.com/setup_current.x | sudo -E bash -
apt-get install nodejs 
sudo apt-get update && sudo apt-get install yarn
apt-get install -y npm
