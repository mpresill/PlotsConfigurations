# example of configuration file
treeName= 'Events'

date='_5May2022_2016'
tag = 'VBS_ZV'+date+'testFJ'

# used by mkShape to define output directory for root files
outputDir = '/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile'+date+'testFJ'

# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of variables
#variablesFile = 'variables.py'
variablesFile = 'testFJ/variables_testFJ.py'

# file with list of cuts
cutsFile = 'testFJ/cuts_testFJ.py'

# file with list of samples
samplesFile = 'testFJ/samples_testFJ.py'
#samplesFile = 'samples.py' #this is a subset of samples_EFT.py, which does not contain EFT and VBS samples global recoil option.


# file with list of samples
plotFile = 'testFJ/plot_testFJ.py'


# luminosity to normalize to (in 1/fb)
lumi = 35.87

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = '/eos/user/m/mpresill/www/VBS/2016_v7/Plots'+date


# used by mkDatacards to define output directory for datacards: common vbs-italia github folder : /afs/cern.ch/work/m/mpresill/Combine_limits/CMSSW_10_2_13/src/HiggsAnalysis/CombinedLimit/VBS/2017_v7/
outputDirDatacard = '/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards'+date
#to be backed up here: /eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards

# structure file for datacard
structureFile = 'structure.py'

# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'testFJ/nuisances_testFJ.py'

