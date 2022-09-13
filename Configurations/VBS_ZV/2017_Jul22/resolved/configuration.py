# example of configuration file
treeName= 'Events'

date='_13Sep2022_2017' 

#categ = 'boosted'
categ = 'resolved'

#tag = 'VBS_ZV'+date #+'_EFT'             #after adding
tag = 'VBS_ZV'+date+'_'+categ


# used by mkShape to define output directory for root files
outputDir = '/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile'+date

# file with TTree aliases
aliasesFile = '../aliases.py'

# file with list of variables
#variablesFile = 'variables.py'
variablesFile = '../variables_reduced.py'

# file with list of cuts
cutsFile = 'cuts_'+categ+'.py'#when launching
#cutsFile = 'cuts.py'#after adding

# file with list of samples
samplesFile = 'samples_'+categ+'.py' #when launching
#samplesFile = 'samples.py' #after adding


# file with list of samples
plotFile = '../plot.py' #this is the updated version for postfit plotting without hacks



# luminosity to normalize to (in 1/fb)
lumi = 41.53

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = '/eos/user/m/mpresill/www/VBS/2017_v7/Plots'+date


# used by mkDatacards to define output directory for datacards: common vbs-italia github folder : /afs/cern.ch/work/m/mpresill/Combine_limits/CMSSW_10_2_13/src/HiggsAnalysis/CombinedLimit/VBS/2017_v7/
outputDirDatacard = '/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards'+date
#outputDirDatacard = '/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/DatacardsEFT'+date
#outputDirDatacard = '/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/VBScomb_Datacards'+date    

# structure file for datacard
structureFile = '../structure.py'

# nuisances file for mkDatacards and for mkShape
nuisancesFile = '../nuisances.py'

