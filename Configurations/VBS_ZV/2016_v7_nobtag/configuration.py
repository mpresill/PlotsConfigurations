# example of configuration file
treeName= 'Events'

#date='_Nov252018_ptll'
date='_13Dec2020_2016_nobtag'

tag = 'VBS_ZV'+date

# used by mkShape to define output directory for root files
outputDir = 'rootFile'+date
#change path to: /eos/user/m/mpresill/www/VBS/2016_v7


# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of variables
variablesFile = 'variables.py'
#variablesFile = 'variables_test.py'

# file with list of cuts
cutsFile = 'cuts.py'

# file with list of samples
#samplesFile = 'samples_test.py'
samplesFile = 'samples.py'


# file with list of samples
#plotFile = 'plot_sig.py'
plotFile = 'plot.py'


# luminosity to normalize to (in 1/fb)
lumi = 35.867

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = '/eos/user/m/mpresill/www/VBS/2016_v7/PlotsVBS_ZV'+date


# used by mkDatacards to define output directory for datacards: common vbs-italia github folder : /afs/cern.ch/work/m/mpresill/Combine_limits/CMSSW_10_2_13/src/HiggsAnalysis/CombinedLimit/VBS/2017_v7/
outputDirDatacard = '/afs/cern.ch/work/m/mpresill/Combine_limits/CMSSW_10_2_13/src/HiggsAnalysis/CombinedLimit/VBS/'+date


# structure file for datacard
structureFile = 'structure.py'

# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'
#nuisancesFile ='nuisances_StatOnly.py'
