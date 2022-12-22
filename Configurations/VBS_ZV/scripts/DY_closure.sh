#!/bin/sh -x 

output_dir=$1 #preferred dir: /eos/user/m/mpresill/CMS/VBS/VBS_ZV/dy_closure_test/
name=$2

mkdir $output_dir;

########################
# Closure test
# run it like: sh ../../scripts/DY_closure.sh /eos/user/m/mpresill/CMS/VBS/VBS_ZV/dy_closure_test 14Dec2022_2017 configuration.py

# 2017 resolved b-veto internal
python ../../scripts/bins_norm_reweights_withsyst.py -i /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_$name/plots_VBS_ZV_${name}_resolved.root \
            -o $output_dir/2017/bins_norm_resolved_bveto_int.csv --vars DYfit_2D_bin_Resolved \
            -s DY_Resolved_2d_01  DY_Resolved_2d_02 DY_Resolved_2d_03 DY_Resolved_2d_04 DY_Resolved_2d_05 DY_Resolved_2d_06 DY_Resolved_2d_07 DY_Resolved_2d_08 DY_Resolved_2d_09 DY_Resolved_2d_10 DY_Resolved_2d_11 DY_Resolved_2d_12 \
            --other-samples tZq VBS_VV_QCD WJets WW ggWW VVV Fake sm_dipole top Vg VgS VBF-V VZ --cut Resolved_DYcr_bVeto_int  -c $3 

## 2017 resolved b-veto internal
python ../../scripts/bins_norm_reweights_withsyst.py -i /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_$name/plots_VBS_ZV_${name}_resolved.root \
            -o $output_dir/2017/bins_norm_resolved_bveto_ext.csv --vars DYfit_2D_bin_Resolved \
            -s DY_Resolved_2d_01  DY_Resolved_2d_02 DY_Resolved_2d_03 DY_Resolved_2d_04 DY_Resolved_2d_05 DY_Resolved_2d_06 DY_Resolved_2d_07 DY_Resolved_2d_08 DY_Resolved_2d_09 DY_Resolved_2d_10 DY_Resolved_2d_11 DY_Resolved_2d_12 \
            --other-samples tZq VBS_VV_QCD WJets WW ggWW VVV Fake sm_dipole top Vg VgS VBF-V VZ --cut Resolved_DYcr_bVeto_ext  -c $3 

# 2017 resolved b-tag internal
python ../../scripts/bins_norm_reweights_withsyst.py -i /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_$name/plots_VBS_ZV_${name}_resolved.root \
            -o $output_dir/2017/bins_norm_resolved_btag_int.csv --vars DYfit_2D_bin_Resolved \
            -s DY_Resolved_2d_01  DY_Resolved_2d_02 DY_Resolved_2d_03 DY_Resolved_2d_04 DY_Resolved_2d_05 DY_Resolved_2d_06 DY_Resolved_2d_07 DY_Resolved_2d_08 DY_Resolved_2d_09 DY_Resolved_2d_10 DY_Resolved_2d_11 DY_Resolved_2d_12 \
            --other-samples tZq VBS_VV_QCD WJets WW ggWW VVV Fake sm_dipole top Vg VgS VBF-V VZ --cut Resolved_DYcr_bTag_int  -c $3 

# 2017 resolved b-tag internal
python ../../scripts/bins_norm_reweights_withsyst.py -i /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_$name/plots_VBS_ZV_${name}_resolved.root \
            -o $output_dir/2017/bins_norm_resolved_btag_ext.csv --vars DYfit_2D_bin_Resolved \
            -s DY_Resolved_2d_01  DY_Resolved_2d_02 DY_Resolved_2d_03 DY_Resolved_2d_04 DY_Resolved_2d_05 DY_Resolved_2d_06 DY_Resolved_2d_07 DY_Resolved_2d_08 DY_Resolved_2d_09 DY_Resolved_2d_10 DY_Resolved_2d_11 DY_Resolved_2d_12 \
            --other-samples tZq VBS_VV_QCD WJets WW ggWW VVV Fake sm_dipole top Vg VgS VBF-V VZ --cut Resolved_DYcr_bTag_ext  -c $3 


# 2017 boosted b-veto internal
python ../../scripts/bins_norm_reweights_withsyst.py -i /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_$name/plots_VBS_ZV_${name}_boosted.root \
            -o $output_dir/2017/bins_norm_boosted_bveto_int.csv --vars DYfit_Z_bin_Boosted \
            -s DY_Boosted_Z_1 DY_Boosted_Z_2 DY_Boosted_Z_3 DY_Boosted_Z_4 DY_Boosted_Z_5 \
            --other-samples tZq VBS_VV_QCD WJets WW ggWW VVV Fake sm_dipole top Vg VgS VBF-V VZ --cut Boosted_DYcr_bVeto_int  -c $3 

## 2017 boosted b-veto internal
python ../../scripts/bins_norm_reweights_withsyst.py -i /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_$name/plots_VBS_ZV_${name}_boosted.root \
            -o $output_dir/2017/bins_norm_boosted_bveto_ext.csv --vars DYfit_Z_bin_Boosted \
            -s DY_Boosted_Z_1 DY_Boosted_Z_2 DY_Boosted_Z_3 DY_Boosted_Z_4 DY_Boosted_Z_5  \
            --other-samples tZq VBS_VV_QCD WJets WW ggWW VVV Fake sm_dipole top Vg VgS VBF-V VZ --cut Boosted_DYcr_bVeto_ext  -c $3 

# 2017 boosted b-tag internal
python ../../scripts/bins_norm_reweights_withsyst.py -i /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_$name/plots_VBS_ZV_${name}_boosted.root \
            -o $output_dir/2017/bins_norm_boosted_btag_int.csv --vars DYfit_Z_bin_Boosted \
            -s DY_Boosted_Z_1  DY_Boosted_Z_2 DY_Boosted_Z_3 DY_Boosted_Z_4 DY_Boosted_Z_5 \
            --other-samples tZq VBS_VV_QCD WJets WW ggWW VVV Fake sm_dipole top Vg VgS VBF-V VZ --cut Boosted_DYcr_bTag_int  -c $3 

# 2017 boosted b-tag internal
python ../../scripts/bins_norm_reweights_withsyst.py -i /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_$name/plots_VBS_ZV_${name}_boosted.root \
            -o $output_dir/2017/bins_norm_boosted_btag_ext.csv --vars DYfit_Z_bin_Boosted \
            -s DY_Boosted_Z_1  DY_Boosted_Z_2 DY_Boosted_Z_3 DY_Boosted_Z_4 DY_Boosted_Z_5 \
            --other-samples tZq VBS_VV_QCD WJets WW ggWW VVV Fake sm_dipole top Vg VgS VBF-V VZ --cut Boosted_DYcr_bTag_ext  -c $3 
