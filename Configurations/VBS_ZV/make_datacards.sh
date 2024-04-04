#! /bin/bash
DATE=_6Dec2023_2018
CATEGORY=boosted
eosPATH=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms


#### the official script: https://github.com/latinos/LatinoAnalysis/blob/master/ShapeAnalysis/scripts/mkDatacards.py , which can be directly used invoking mkDatacard.py, contains a patch to logNormal datacard nuisances.
### the script mkDatacards2.py contains a patch I did to correctly include nuisances groups (for ratePatameters, I guess)
### the script mkDatacards3.py is identical to the official version, but with a patch that allows to rename nuisances while making the datacards -- incomplete 



#10Dic2020_2017_nobtag #change date 
#mkShapesMulti.py --pycfg=configuration.py --batchSplit=Samples,Files

#mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=longlunch  #espresso #longlunch #--dry-run

##mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files --doNotCleanup --nThreads=10 #to hadd files

#mkPlot.py --pycfg=configuration.py --inputFile=rootFile_${DATE}/plots_VBS_ZV_${DATE}.root --minLogC=0.01 --minLogCratio=0.01 --maxLogC=10000000 --maxLogCratio=10000000  --showIntegralLegend=1

#rm -rf /eos/user/m/mpresill/CMS/VBS/VBS_ZV/plots/PlotsVBS_ZV_${DATE}
#mkdir /eos/user/m/mpresill/CMS/VBS/VBS_ZV/plots/PlotsVBS_ZV_${DATE}
#cp -r PlotsVBS_ZV_${DATE}/*.png /eos/user/m/mpresill/CMS/VBS/VBS_ZV/plots/PlotsVBS_ZV_${DATE}/. 

#to resubmit jobs:
#for i in *jid; do sed -i "s/longlunch/microcentury/g" ${i/jid/jds}; condor_submit ${i/jid/jds}; done

cd 2018-v1/${CATEGORY}
#to make datacard:
mkDatacards.py --pycfg=configuration.py --inputFile=${eosPATH}/rootFile${DATE}/plots_VBS_ZV${DATE}_${CATEGORY}.root
#mkDatacards.py --pycfg=configuration.py --inputFile=plots_VBS_ZV${DATE}_${CATEGORY}.root --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards${DATE}_QCDscaleDY_corr/ 
#mkDatacards.py --pycfg=configuration.py --inputFile=plots_VBS_ZV${DATE}_${CATEGORY}_wPS_wQCD.root --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards${DATE}_QCDscaleDY_ln/ --skipMissingNuisance
#../../scripts/mkDatacards2.py --pycfg=configuration.py --inputFile=plots_VBS_ZV${DATE}_wJes_${CATEGORY}_QCDscale_corr_noPSdy.root --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards${DATE}_wJes_QCDscale_corr_noPSdy/

    ###### when using 20.16 
#../../scripts/mkDatacards2.py --pycfg=configuration.py --inputFile=plots_VBS_ZV${DATE}_${CATEGORY}_wPS_wQCD.root --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards${DATE}_wPS/ --skipMissingNuisance #the last option is needed for the DY binned variable on which we could not extrapolate the variations

    ###### when using 20.17
#../../scripts/mkDatacards2.py --pycfg=configuration.py --inputFile=plots_VBS_ZV${DATE}_${CATEGORY}_wPS.root --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards${DATE}_wPS/ --skipMissingNuisance #the last option is needed for the DY binned variable on which we could not extrapolate the variations

    ###### when using 20.18
#../../scripts/mkDatacards2.py --pycfg=configuration.py --inputFile=plots_VBS_ZV${DATE}_${CATEGORY}.root --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards${DATE}_wPS/ --skipMissingNuisance #the last option is needed for the DY binned variable on which we could not extrapolate the variations


#../mkDatacards_QUICK.py --pycfg=configuration.py --inputFile=${eosPATH}/rootFile_${DATE}/plots_VBS_ZV_${DATE}.root #plots_VBS_ZV_${DATE}.root
##PLEASE BACK THEM UP HERE: /eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacard
cd ..
