# example of configuration file
treeName= 'Events'

#date='_Nov252018_ptll'
date='_20Oct2020'

tag = 'VBS_ZV'+date

# used by mkShape to define output directory for root files
outputDir = 'rootFile'+date

# file with TTree aliases
aliasesFile = 'aliases_DNN.py'

# file with list of variables
variablesFile = 'variables_DNN.py'
#variablesFile = 'variables_test.py'

# file with list of cuts
cutsFile = 'cuts_DNN.py'

# file with list of samples
#samplesFile = 'samples_test.py'
samplesFile = 'samples.py'


# file with list of samples
#plotFile = 'plot_sig.py'
plotFile = 'plot.py'


# luminosity to normalize to (in 1/fb)
lumi = 59.74

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = '/eos/user/a/ahakimi/www/ZV_analysis/2018_v7/PlotsVBS_ZV'+date


# used by mkDatacards to define output directory for datacards: common vbs-italia github folder 
outputDirDatacard = '/afs/cern.ch/user/a/ahakimi/ZV_analysis/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/2018_v7/Datacards'+date


# structure file for datacard
structureFile = 'structure.py'

# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'
#nuisancesFile ='nuisances_StatOnly.py'
