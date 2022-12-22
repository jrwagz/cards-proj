#!/usr/bin/env bash

python3.10 -m venv .venv
source .venv/bin/activate
pip3 install --upgrade pip

if [[ -e "requirements.txt" ]]; then
    pip3 install -r requirements.txt
fi

if [[ -e "requirements-dev.txt" ]]; then
    pip3 install -r requirements-dev.txt
fi

pip3 install -e .