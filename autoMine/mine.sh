#! /bin/bash

INTERVAL=10
DIR=$(dirname ${BASH_SOURCE[*]})

source $DIR/commands &

# wait if there's no update
pushd $DIR
while git pull origin autoMine 2>&1 | grep "Already up-to-date" > /dev/null; do
    sleep $INTERVAL
done
popd

# script updated, reload commands
pgrep cpuminer | xargs kill
sleep $INTERVAL
exec $DIR/$(basename $0)

