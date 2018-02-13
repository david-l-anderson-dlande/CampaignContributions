#!/bin/bash

export PYTHONPATH=$PYTHONPATH:../../../src

python3 -m unittest campconttest -v
