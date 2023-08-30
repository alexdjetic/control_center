#!/bin/bash

for file in *.py; do
    if [ ! -x "$file" ]; then
        chmod +x "$file"
        echo "Added execution permission to $file"
    fi
done


python3 main.py
