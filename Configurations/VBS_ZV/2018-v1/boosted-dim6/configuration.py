# example of configuration file
treeName= 'Events'

date='_6Dec2023_2018-dim6'

categ = 'boosted'
#operator = 'T9'

#categ = 'resolved'

#tag = 'VBS_ZV'+date              #after adding
tag = 'VBS_ZV'+date+'_'+categ


# used by mkShape to define output directory for root files
outputDir = '/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile'+date

# file with TTree aliases
aliasesFile = '../aliases.py'

# file with list of variables
variablesFile = '../boosted/variables.py'
#variablesFile = '../variables_njet.py'

# file with list of cuts
cutsFile = 'cuts_'+categ+'.py'#when launching
#cutsFile = 'cuts_'+categ+'_closure.py'#when launching
#cutsFile = 'cuts.py'#after adding

# file with list of samples
samplesFile = 'samples_'+categ+'-dim6.py' #when launching
#samplesFile = 'samples.py' #after adding


# file with list of samples
plotFile = '../plot_v2_EFT.py'
#plotFile = '../plot.py'


# luminosity to normalize to (in 1/fb)
lumi = 59.74

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = '/eos/user/m/mpresill/www/VBS/2018_v7/PlotsVBS_ZV'+date


# used by mkDatacards to define output directory for datacards: common vbs-italia github folder : /afs/cern.ch/work/m/mpresill/Combine_limits/CMSSW_10_2_13/src/HiggsAnalysis/CombinedLimit/VBS/2017_v7/
outputDirDatacard = '/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards'+date
#outputDirDatacard = '/eos/user/m/mpresill/CMS/VBS/VBS_ZV/DatacardsEFT/Datacards'+date+'_c'+operator
#outputDirDatacard = '/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/VBScomb_Datacards'+date


# structure file for datacard
structureFile = '../structure-dim6.py'

# nuisances file for mkDatacards and for mkShape
nuisancesFile = '../nuisances-dim6.py'
#nuisancesFile = '../2016_v7_Jan22/nuisances_StatOnly.py'

