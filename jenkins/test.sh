#!/bin/bash

source venv/bin/activate
python3 -m pytest \
    --cov=application \
    --cov-report term-missing \