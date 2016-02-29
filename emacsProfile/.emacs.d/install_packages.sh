#!/bin/bash

getPkg() {
    if [ -d $1 ]; then
	pushd $1 > /dev/null ;
	echo -n $1...; git pull;
	popd > /dev/null
    else
	git clone $2
    fi
}

pushd ~/.emacs.d/ > /dev/null

# Add packages here
getPkg "ztree" "https://github.com/fourier/ztree.git"
getPkg "xcscope.el" "https://github.com/dkogan/xcscope.el.git"

popd > /dev/null
