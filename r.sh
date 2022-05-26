#!/bin/bash

python3 preprocessor.py $1 tmp.r

./r.out tmp.r