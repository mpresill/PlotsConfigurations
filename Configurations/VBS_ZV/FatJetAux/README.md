# Uage of Fat Jet systematics in ReReco 

1. update the ShapeFactoryMulti.py to include auxiliary systematics according to this example:

and place it its correct ShapeAnalysis path:
>/afs/cern.ch/work/m/mpresill/Latino/CMSSW_10_6_4/src/LatinoAnalysis/ShapeAnalysis/python/ShapeFactoryMulti.py 


2. update mapping of fat jet nominal values branches to let them apply the magics of MultiDraw to produce up and down variations

and place it its correct NanoGardner path:
>/afs/cern.ch/work/m/mpresill/Latino/CMSSW_10_6_4/src/LatinoAnalysis/NanoGardener/python/data/BranchMapping_cfg.py 


3. update the relevant macros for jet pairing:
https://github.com/mpresill/PlotsConfigurations/blob/matteo/Configurations/VBS_ZV/macros/jets_cat_dnn_morphed_FJ.cc
https://github.com/mpresill/PlotsConfigurations/blob/matteo/Configurations/VBS_ZV/macros/jets_cat_dnn_pruned_FJ.cc 


N.B. Do not forget to polish all the compiled files (*_cc*) in the relevant folders, 
i.e. ../patches/, ./macros/, ../Differential/ 
