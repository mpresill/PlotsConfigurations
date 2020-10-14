# Configuration file to produce initial root files -- has both merged and binned ggH samples

treeName = 'Events'

tag = 'ggH2017v6_STXS_XSest'

# used by mkShape to define output directory for root files
outputDir = 'rootFile_'+tag

# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of variables
variablesFile = 'variables_XSest.py'

# file with list of cuts
cutsFile = 'cuts_XSest.py' 

# file with list of samples
samplesFile = 'samples_XSest.py' 

# file with list of samples
#plotFile = 'plot.py' 

# luminosity to normalize to (in 1/fb)
lumi = 41.53

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
#outputDirPlots = 'plots_'+tag

# used by mkDatacards to define output directory for datacards
#outputDirDatacard = 'datacards_'+tag

# structure file for datacard
#structureFile = 'structure.py'

# nuisances file for mkDatacards and for mkShape
#nuisancesFile = 'nuisances.py'
