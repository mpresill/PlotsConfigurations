#! /bin/bash
cd 2016_v7_2
mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files  --nThreads=15 --doNotCleanup  #to hadd files
cd ..

#force hadd:
#hadd -j 5 -f plots_VBS_ZV_19Sept2021.root plots_VBS_ZV_19Sept2021_ALL_*
