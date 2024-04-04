#! /bin/bash
DATE=$1 #_21Aug2023_2016
CATEGORY=$2 #resolved
release=$3
#eosPATH=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms
eosPATH=/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms
localPATH=$(pwd)

#echo "The script you are running has:"
#echo "basename: [$(basename "$0")]"
#echo "dirname : [$(dirname "$0")]"
#echo "pwd     : [$(pwd)]"

cd ${eosPATH}/rootFile${DATE}/corrections/
echo ${eosPATH}/rootFile${DATE}/corrections/
###### backup the original root file
rm plots_VBS_ZV${DATE}_${CATEGORY}.root
cp ../plots_VBS_ZV${DATE}_${CATEGORY}.root .

##### step 1: extract json files with the up/down variation with different normalization
python ${localPATH}/scripts/Utilities_nuisances/normalize_nuisance_effect.py \
-i plots_VBS_ZV${DATE}_${CATEGORY}.root \
-o ratio_normalize${DATE}_${CATEGORY}.json \
-c ${localPATH}/${release}/nuisance_norm_conf_${CATEGORY}.py  #\

###	other options:
##-e V_jet_qgl2_morphed,mjj,Zlep_1,V_jet_eta1,V_jet_eta2,Zlep_2,DYfit_2D_bin_Resolved,pt1,nCleanJetNotFat,VBS_jet_pt2,Vjet_mass,V_jet_qgl1_morphed,V_jet_pt1,V_jet_pt2,detajj_mjjmax,detajj_mjjmax,mll-peak
##-c ../nuisance_norm_conf${DATE}_${CATEGORY}.py
##--dry

cd $localPATH
