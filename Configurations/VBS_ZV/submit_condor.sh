#! /bin/bash
#DATE=3May2020 #change date 
#mkShapesMulti.py --pycfg=configuration.py --batchSplit=Samples,Files
cd 2018-v1/resolved_ewk_qcd

#mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=workday #--dry-run 
/afs/cern.ch/work/m/mpresill/Latino/CMSSW_10_6_4/src/LatinoAnalysis/ShapeAnalysis/scripts/mkShapesMultiv2.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=longlunch #--dry-run 

#mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=microcentury #--dry-run 

# N.B. the version of mkShapesMulti.py that we are using can write output files in any EOS folder, the default one is called mkShapesMulti_original.py
#mkShapesMulti_alexandre.py is in principle able to write on eos the output files too: /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms

#espresso #longlunch #--dry-run
#mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --samplesFile=VBS_VV_QCD --batchQueue=microcentury

cd ../..
##mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files --doNotCleanup --nThreads=10 #to hadd files

#mkPlot.py --pycfg=configuration.py --inputFile=rootFile_${DATE}/plots_VBS_ZV_${DATE}.root --minLogC=0.01 --minLogCratio=0.01 --maxLogC=10000000 --maxLogCratio=10000000  --showIntegralLegend=1

#rm -rf /eos/user/m/mpresill/CMS/VBS/VBS_ZV/plots/PlotsVBS_ZV_${DATE}
#mkdir /eos/user/m/mpresill/CMS/VBS/VBS_ZV/plots/PlotsVBS_ZV_${DATE}
#cp -r PlotsVBS_ZV_${DATE}/*.png /eos/user/m/mpresill/CMS/VBS/VBS_ZV/plots/PlotsVBS_ZV_${DATE}/. 

#to resubmit jobs:
#for i in *jid; do sed -i "s/longlunch/microcentury/g" ${i/jid/jds}; condor_submit ${i/jid/jds}; done

#to make datacard:
#mkDatacards.py --pycfg configuration.py --inputFile rootFile_${DATE}/plots_VBS_ZV_${DATE}.root
