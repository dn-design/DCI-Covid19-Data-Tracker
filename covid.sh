#!/bin/bash
cd ~/datax/covid19
curl -O https://covid.ourworldindata.org/data/ecdc/full_data.csv
python3 covid.py
