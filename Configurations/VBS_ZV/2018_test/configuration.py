# example of configuration file
treeName= 'Events'

date='_29June2021_2018_bin1D'
tag = 'VBS_ZV'+date

# used by mkShape to define output directory for root files
outputDir = 'rootFile'+date

# file with TTree aliases
#aliasesFile = 'aliases_PUjet.py'
aliasesFile = 'aliases.py'

# file with list of variables
#variablesFile = 'variables_test.py'
variablesFile = 'variables.py'

# file with list of cuts
cutsFile = 'cuts.py'

# file with list of samples
#samplesFile = 'samples_dipoleRecoil.py'
#samplesFile = 'samples_PUjet.py'
samplesFile = 'samples.py'


# file with list of samples
#plotFile = 'plot_dipoleRecoil.py'
#plotFile = 'plot_PUjet.py'#this has same color palette in Alexander's, for PUjet based splitting
plotFile = 'plot.py'#this is for bin splitting


# luminosity to normalize to (in 1/fb)
lumi = 59.74

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = '/eos/user/m/mpresill/www/VBS/2018_v7/PlotsVBS_ZV'+date


# used by mkDatacards to define output directory for datacards: 
outputDirDatacard = './Datacards/'+date


# structure file for datacard
#structureFile = 'structure_PUjet.py'
structureFile = 'structure.py'

# nuisances file for mkDatacards and for mkShape
#nuisancesFile = 'nuisances_PUjet.py'
#nuisancesFile ='nuisances_StatOnly.py'
nuisancesFile ='nuisances.py'

