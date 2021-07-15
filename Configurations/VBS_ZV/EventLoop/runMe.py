from ROOT import gSystem
gSystem.Load("Analysis.so")
from ROOT import EventLoop
eventLoop = EventLoop()


# 1. name of the tree.
# tree should be called Events for Latinos
eventLoop.treeName = "Events"





# 2. add the input files. We use MC simulation of some process
eventLoop.inputFiles.push_back('/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2016_102X_nAODv7_Full2016v7/DATAl1loose2016v7/nanoLatino_DoubleEG_Run2016D-02Apr2020-v1__part0.root')
eventLoop.inputFiles.push_back('/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2016_102X_nAODv7_Full2016v7/DATAl1loose2016v7/nanoLatino_DoubleEG_Run2016D-02Apr2020-v1__part1.root')
#eventLoop.inputFiles.push_back( ....

# eventually 
# add some loop 
# on samples to 
# speed it up !!!







eventLoop.initialize()
eventLoop.execute()
