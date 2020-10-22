#!/bin/bash
cd 2018_v7
mkShapesMulti.py  --pycfg=configuration.py --batchSplit=Samples,Files --doThreads=False
cd ..
