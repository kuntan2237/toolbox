#!/usr/bin/env bash

if [ ! -e ~/.ssh/id_rsa ]; then
    echo "Generate SSH key file."
    ssh-keygen -t rsa -f ~/.ssh/id_rsa -P ""
else
    echo "SSH key file already exist."
fi

read -p "Input remote user@hostname: " user_host

echo "Create .ssh directory at remote server..."
ssh $user_host mkdir -p .ssh
echo "Copy public key to remote server..."
cat ~/.ssh/id_rsa.pub | ssh $user_host 'cat >> .ssh/authorized_keys; chmod 700 .ssh/authorized_keys'

echo "You can login $user_host now!"
echo 'If you get error "Agent admitted failure to sign using the key.", run "ssh-add at local side".'
