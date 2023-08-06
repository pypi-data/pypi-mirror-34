#!/bin/bash

if [ ! -d $HOME/azure ]; then
    sudo mkdir $HOME/azure
    sudo chown $USER $HOME/azure
fi

if [ ! -d $HOME/azure/waagent ]; then
    sudo mkdir $HOME/azure/waagent
    sudo chown $USER $HOME/azure/waagent
fi

install_log="$HOME/azure/waagent/install.log"

echo "Installing waagent" > $install_log
cd waagent
echo "going to install rpm" >> $install_log
sudo cp init/waagent.service /usr/lib/systemd/system
filename=$(ls ../*.rpm)
sudo yum -y localinstall $filename
echo "Starting waagent daemon" >> $install_log
sudo systemctl enable /usr/lib/systemd/system/waagent.service
sudo service waagent start
systemctl status waagent >> $install_log
echo "Waagent daemon running" >> $install_log