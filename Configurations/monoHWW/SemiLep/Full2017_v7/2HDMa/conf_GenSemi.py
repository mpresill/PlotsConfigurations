# Load signal sample dict

# Configuration file to produce initial root files

treeName = 'Events'

tag = 'GenSemi_2017v7'

# used by mkShape to define output directory for root files
outputDir = 'GenSemi_root'

# file with TTree aliases
aliasesFile = 'aliases_GenSemi.py'

# file with list of variables
variablesFile = 'variables_GenSemi.py'

# file with list of cuts
cutsFile = 'cuts_GenSemi.py'

# file with list of samples
samplesFile = 'samples.py'

# file with list of samples
plotFile = 'plot.py'

# luminosity to normalize to (in 1/fb)
lumi = 41.5

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = 'GenSemi_plots'

# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'GenSemi_datacards'

# structure file for datacard
structureFile = 'structure.py'

# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'
