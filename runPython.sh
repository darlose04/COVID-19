#!/bin/bash
echo "Running Python data scripts at $(date +%B%d,%T)" > /home/zach/Storage/Projects/COVID-19/runPython.out

python3 /home/zach/Storage/Projects/COVID-19/dataParse/deaths_us.py

echo "Scripts done running " >> /home/zach/Storage/Projects/COVID-19/runPython.out
