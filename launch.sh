#!/bin/bash

source .venv/bin/activate
python3 -m unittest code.tests
if [ $? -ne 0 ]; then
    echo "Tests failed. Exiting."
    exit 1
else
    echo "All tests passed."
fi
python3 code/main.py
