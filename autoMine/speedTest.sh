#! /bin/bash

INTERVAL=10

getLatency() {
    local latency=`ping -c $INTERVAL -s 128 speedtest.$1.nicehash.com | grep rtt | awk -F '/' {'print $5'}`
    if [ x"$1" == x"hk" ]; then
        echo "$latency+150" | bc
    elif [ x"$1" == x"jp" ]; then
	echo "$latency+100" | bc
    else
        echo $latency
    fi
}

# set default gateway
best_proxy="usa"
best_latency=`getLatency $best_proxy`

for proxy in "hk" "jp" "usa" "eu"; do
    if [ x$best_proxy == x$proxy ]; then
	latency=$best_latency
    else
	latency=`getLatency $proxy`
    fi
    echo Proxy $proxy $latency ms
    
    if [ $(echo $best_latency'>'$latency | bc) == 1 ]; then
        best_proxy=$proxy
        best_latency=$latency
    fi
done

echo Best Proxy is $best_proxy, latency $best_latency
