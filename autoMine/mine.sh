#! /bin/bash

pushd $(dirname ${BASH_SOURCE[*]})
while true; do
    source ./manual
    pgrep cpuminer | xargs kill
    pushd ..; git pull origin master; popd
done
popd

