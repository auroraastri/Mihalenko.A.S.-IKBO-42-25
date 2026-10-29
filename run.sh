#!/usr/bin/env bash
set -e
python3 -m unittest discover -s tests
python3 -m src.emulator "$@"