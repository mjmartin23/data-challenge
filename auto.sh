#!/bin/bash

for file in *.csv; do
    echo "$file"
    cat $file | wc -l
done
