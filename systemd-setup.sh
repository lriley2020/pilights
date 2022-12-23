#!/bin/bash
if [ "$EUID" -ne 0 ];then
    echo "Please run this script as root"
    exit 1
fi
echo "This script will move and enable the example 'pilights.service' file"
echo "Some of the hardcoded paths present in this file will need to be changed before the service is enabled"
read -p "Do you wish to continue? (y/n)> " REPLY
if [ "$REPLY" != "y" ]; then
   exit
fi
echo "Copying config file..."
cp ./pilights.service /etc/systemd/system/
echo "Reloading systemd daemon..."
systemctl daemon-reload
echo "Enabling service..."
systemctl enable pilights --now
