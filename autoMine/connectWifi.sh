#!/usr/bin/bash

INTERVAL=5
echo_time() {
    date +"%D %r: $*"
}

while true; do
    # Check network status
    if ping www.baidu.com -c 4 | grep "4 received" > /dev/null; then
	echo_time "WIFI Connected."
	sleep $[$INTERVAL * 10]
	continue
    else
	nmcli radio wifi off
	echo_time Connection down, disconnecting wifi... $?
	sleep $INTERVAL
    fi
    
    # Check WIFI status
    while [ `nmcli radio wifi` == "disabled" ]; do
	nmcli radio wifi on
	echo_time Reconnecting WIFI... $?
	sleep $INTERVAL
    done
    # Search AP
    while ! nmcli device wifi list | grep i-Shanghai > /dev/null; do
	nmcli device wifi rescan
	echo_time Scanning AP list... $?
	sleep $INTERVAL
    done
    # Connect to AP
    while ! nmcli device status | grep i-Shanghai > /dev/null; do
	nmcli device wifi connect i-Shanghai
	echo_time Reconnecting AP... $?
	sleep $INTERVAL
    done
    # Login
    $(dirname ${BASH_SOURCE[*]})/loginISH.py $1 $2
    echo_time Login ... $?
    sleep $INTERVAL
done
