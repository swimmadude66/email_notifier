#!/bin/bash

mkdir /home/.emails
echo "emails directory located at /home/.emails"
cp ./*.py /home/.emails
cp ./K00shutdown-email /etc/init.d/
cp ./S20bootup-email /etc/init.d/
cp ./update-email /etc/cron.daily
cp ./restart-email /etc/cron.daily
cd /etc/rc0.d
ln -s ../init.d/K00shutdown-email
cd ../rc2.d
ln -s ../init.d/S20bootup-email

echo "Files installed in correct locations"
