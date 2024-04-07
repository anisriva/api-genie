#!/bin/bash

rm -rf venv

python3.9 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

