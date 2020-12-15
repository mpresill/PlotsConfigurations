#! /bin/bash
cd 2018_SR_new
mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files --doNotCleanup --nThreads=10 #to hadd files
cd ..

#force hadd:
#hadd -j 5 -f plots_VBS_ZV_20June2020.root plots_VBS_ZV_20June2020_ALL_*
