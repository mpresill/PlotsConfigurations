#!/bin/bash
folder=2018_dec21
date=27Jan2022_2018
FITVAR=DNNoutput_pruned_bReq
CUT=Resolved_DYcr_bTag
PLOTVAR=VBS_jet_pt1
DATACARD_NAME=Datacards_${date}/${CUT}/${PLOTVAR}/datacard

rm -rf Workspace/${CUT}
mkdir -p Workspace
mkdir Workspace/${CUT}
cardName=${CUT}
for PLOTVAR in VBS_jet_pt1 VBS_jet_pt2 V_jet_pt1 V_jet_pt2 Zleppt DYfit_Z_bin_Boosted detajj_mjjmax mjj_max VBS_jet_qgl1_morphed VBS_jet_qgl2_morphed V_jet_qgl1_morphed V_jet_qgl2_morphed DNNoutput_full_bVeto DNNoutput_pruned_bVeto  
do
	echo "plotting ${PLOTVAR}"
	DATACARD_NAME=Datacards_${date}/${CUT}/${PLOTVAR}/datacard
	cardNameWorkspace=Workspace/${CUT}/${PLOTVAR}
	outputFolder=Workspace/${CUT}

	text2workspace.py ${DATACARD_NAME}.txt -o ${cardNameWorkspace}.root

	PostFitShapesFromWorkspace \
    	-w ${cardNameWorkspace}.root \
    	-d ${DATACARD_NAME}.txt \
    	-o output_${PLOTVAR}.root \
    	--postfit --sampling \
    	-f fit/${FITVAR}/fitDiagnostics.root:fit_s \
    	--total-shapes


	mkPostFitCombinedPlot.py \
    	--inputFilePostFitShapesFromWorkspace output_${PLOTVAR}.root \
    	--outputFile postfit.root \
    	--kind P \
    	--cutName ${CUT} \
    	--variable ${PLOTVAR} \
    	--structureFile structure.py \
    	--plotFile plot_res.py \
    	--lumiText '59.74/fb' \
   
    

	mkPlot.py --pycfg=configuration_combined.py --inputFile postfit.root --onlyPlot=cratio --logOnly --showIntegralLegend=1 --minLogCratio=0.01 --maxLogCratio=10000

done
rm -r postfit_${CUT}_${FITVAR}fit
mv plot_combined postfit_${CUT}_${FITVAR}fit

python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py --all --abs --format html fit/${FITVAR}/fitDiagnostics.root > postfit_${CUT}_${FITVAR}fit/fit.html

cp -r postfit_${CUT}_${FITVAR}fit /eos/home-a/ahakimi/www/ZV_analysis/Plots_${date}


