#!/usr/bin/env bash

grep set-title ~/.bashrc > /dev/null
if [ $? = 0 ]; then
    echo "set-title() already exist."
elif [ $? = 1 ]; then
    echo 'set-title(){' >> ~/.bashrc
    echo '    ORIG=$PS1' >> ~/.bashrc
    echo '    TITLE="\e]2;$@\a"' >> ~/.bashrc
    echo '    PS1=${ORIG}${TITLE}' >> ~/.bashrc
    echo '}' >> ~/.bashrc
    echo "set-title() patched into ~/.bashrc."
elif [ $? = 2 ]; then
    echo "~/.bashrc does not exist!"
else
    echo "Unknow error"
fi
