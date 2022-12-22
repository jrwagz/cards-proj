#!/usr/bin/env bash

python3 -m venv venv
source venv/bin/activate
pip3 install --upgrade pip
pip3 install pytest

if [[ -e "requirements.txt" ]]; then
    pip3 install -r requirements.txt
fi
