#! /bin/bash
#
# Miner command syntax
# <miner> -a <alog> -o stratum+tcp://<alog>.<proxy>.nicehash.com:<port> -u <wallet>.<worker> -p <password> -t <thread_number>

# wrapper settings
INTERVAL=10
DIR=$(dirname ${BASH_SOURCE[*]})
CPU="cpuminer"
GPU="ccminer"

# miner parameters
ALOG="quark"; PORT="3345"
#ALOG="x11"; PORT="3336"
PROXY="hk"
#WALLET="1GYFNyra9yTcX74ibEx2Vwjio81yBKBT5m" #blockchain
WALLET="1FVFQL9LdUEoXFJnibmaZp7qHpUQRqYNN6" #okcoin
WORKER="default"
PASSWORD="x"
THREADS="0"

echo_time() {
    date +"%D %r: $*"
}

# start mining
for miner in $CPU $GPU; do
    echo_time start $miner...

    # name the worker
    #WORKER=`ifconfig | grep "127.0.0" | awk -F'[ .]' '{print $13}' | xargs printf %03d`${miner:0:3}
    WORKER=`ifconfig | grep "10.42.0" | awk -F'[ .]' '{print $13}' | xargs printf %03d`${miner:0:3}

    # get thread number for CPU
    if [ x$miner == x"cpuminer" ]; then
	THREADS=$[`nproc`-2]
    else
	THREADS="0"
	lsmod | grep nvidia > /dev/null || continue
    fi

    # start mining
    cmd="$miner -a $ALOG -o stratum+tcp://$ALOG.$PROXY.nicehash.com:$PORT -u $WALLET.$WORKER -p $PASSWORD -t $THREADS"
    echo_time $cmd; $cmd >$miner.log &
done

# wait until branch update
pushd $DIR/..
while git pull origin autoMine 2>&1 | grep "Already up-to-date" > /dev/null; do
    echo_time No repo change, continue running
    sleep $[$INTERVAL*10]
done
popd

# script updated, reload commands
echo_time Script Changed, stop commands...
pgrep $CPU && pgrep $CPU | xargs kill
pgrep $GPU && pgrep $GPU | xargs kill
sleep $INTERVAL

# reload self
exec $DIR/$(basename $0)
