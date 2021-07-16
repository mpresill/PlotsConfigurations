from ROOT import gSystem
gSystem.Load("Analysis.so")
from ROOT import EventLoop
eventLoop = EventLoop()
import os

# 1. name of the tree.
# tree should be called Events for Latinos
eventLoop.treeName = "Events"



data_dir= '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2016_102X_nAODv7_Full2016v7/DATAl1loose2016v7/'

files= [file for file  in os.listdir(data_dir) if 'Run2016D' in file]
# 2. add the input files. We use MC simulation of some process
for file in files:
    eventLoop.inputFiles.push_back(data_dir + file)

#eventLoop.inputFiles.push_back( ....

# eventually 
# add some loop 
# on samples to 
# speed it up !!!







eventLoop.initialize()
eventLoop.execute()
