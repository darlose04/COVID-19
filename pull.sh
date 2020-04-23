#!/bin/bash

echo "Pulling data from COVID-19 Github Repository at $(date +%B%d,%T)" > /home/zach/Storage/Projects/COVID-19/pull.out

cd /home/zach/Storage/Projects/COVID-19/covidData
git pull
cd ../

echo "Data updated" >> /home/zach/Storage/Projects/COVID-19/pull.out
