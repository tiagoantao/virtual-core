#!/bin/bash
git submodule update --init --recursive
PYTHONPATH=. python3 -m wizard
