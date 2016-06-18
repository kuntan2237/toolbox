#!/usr/bin/env bash

sudo launchctl stop com.crashplan.engine
sudo launchctl unload /Library/LaunchDaemons/com.crashplan.engine.plist
