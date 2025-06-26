#!/usr/bin/env bash

metric-cli --env prod list
metric-cli --env prod diff ./metrics_sales.yml
metric-cli --env prod deploy ./metrics_sales.yml