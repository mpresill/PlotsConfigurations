#!/bin/bash
folder=2018_test
date=31Mar2021_2018bintest
VAR=Zleppt
CUT=Resolved_DYcr_bVeto
DATACARD_NAME=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${folder}/Datacards_${date}/${CUT}/${VAR}/datacard



cd ${folder}

#echo "RUNNING WITH TOP CR FIT"
rm -rf Fit/${CUT}
mkdir -p Fit
mkdir Fit/${CUT}
cardName=${CUT}
cardNameWorkspace=Fit/${CUT}
outputFolder=Fit/${CUT}



text2workspace.py ${DATACARD_NAME}.txt -o ${cardNameWorkspace}.root
mkdir fitDiagnosticsCombined

combine -M FitDiagnostics ${cardNameWorkspace}.root --out fitDiagnosticsCombined

#cd Datacards_${date}
PostFitShapesFromWorkspace \
    -w ../${cardNameWorkspace}.root \
    -d ${DATACARD_NAME}.txt \
    -o ../output_histograms.root \
    --postfit --sampling \
    -f ../fitDiagnosticsCombined/fitDiagnostics.root:fit_s \
    --total-shapes
#cd .. 

#kind P = postfit, p=prefit 
mkPostFitCombinedPlot.py \
    --inputFilePostFitShapesFromWorkspace output_histograms.root \
    --outputFile postfit.root \
    --kind P \
    --cutName ${cut} \
    --variable ${VAR} \
    --structureFile structure.py \
    --plotFile plot.py \
    --lumiText '59.74/fb'

mkPlot.py --pycfg=configuration_combined.py --inputFile postfit.root --onlyPlot=cratio --logOnly --showIntegralLegend=1

cp -r plot_${CUT} /eos/home-a/ahakimi/www/ZV_analysis/${date}

cd ..
