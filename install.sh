#!/usr/bin/env bash

if [[ "$EUID" -ne 0 ]]; then
    echo "Please run as root (use sudo)"
    exit 1
fi

file='./dorkgen.py'
name="$(basename "${file%.py}")"

mkdir /usr/local/share/dorkgen/

cp -r $file /bin/$name
cp -r ./index.html /usr/local/share/dorkgen/index.html
echo "Done."
