#! /bin/bash

INTERVAL=10
LATENCY_THRESHOLD=100
DIR=$(dirname ${BASH_SOURCE[*]})

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

getProxy() {
    local bestProxy=$1
    local bestLatency=`getLatency $1`

    for proxy in "hk" "jp" "usa" "eu"; do
        if [ x$bestProxy == x$proxy ]; then continue; fi

	local latency=`getLatency $proxy`
        if [ $(echo $bestLatency'>'$latency'+'$LATENCY_THRESHOLD | bc) == 1 ]; then
            bestProxy=$proxy
            bestLatency=$latency
	    fi
    done

    echo $bestProxy
}

if [ x$1 == x ]; then
    currProxy="hk"
else
    currProxy=$1
fi

source $DIR/commands $currProxy &

# wait if there's no update
pushd $DIR
while git pull origin autoMine 2>&1 | grep "Already up-to-date" > /dev/null; do
    # Check fastest proxy
    bestProxy=`getProxy $currProxy`
    if [ x$bestProxy != x$currProxy ]; then
	echo =====PROXY CHANGED!=====
	break;
    fi
done
popd

# script updated, reload commands
pgrep cpuminer | xargs kill
sleep $INTERVAL
exec $DIR/$(basename $0) $bestProxy

