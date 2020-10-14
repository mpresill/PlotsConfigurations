# Configuration file to produce initial root files -- has both merged and binned ggH samples

treeName = 'Events'

tag = 'ggH_vbf_VH_2017v6_STXS_22May'

# used by mkShape to define output directory for root files
outputDir = 'rootFile_'+tag

# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of variables
variablesFile = 'variables_mkshapes.py'

# file with list of cuts
cutsFile = 'cuts.py' 

# file with list of samples
samplesFile = 'samples.py' 

# file with list of samples
plotFile = 'plot.py' 

# luminosity to normalize to (in 1/fb)
lumi = 41.53

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = 'plots_'+tag

# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards_'+tag

# structure file for datacard
structureFile = 'structure.py'

# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'

# input files
# /eos/cms/store/group/phys_higgs/cmshww/amassiro/Full2016_Apr17/Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__wwSel
