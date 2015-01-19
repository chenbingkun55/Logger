#!/bin/sh

m5 ./log.m5.py | m4 > ./log.py
m5 ./lib/bigquery.m5.py | m4 > ./lib/bigquery.py
m5 ./lib/xmlconfig.m5.py | m4 > ./lib/xmlconfig.py
