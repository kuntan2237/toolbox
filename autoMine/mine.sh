#! /bin/bash

pushd $(dirname ${BASH_SOURCE[*]})
while true; do
    source ./manual &
    sleep $[60 * 60 * 8] # 8 hrs
    pgrep cpuminer | xargs kill
    pushd ..; git pull origin master; popd
done
popd

