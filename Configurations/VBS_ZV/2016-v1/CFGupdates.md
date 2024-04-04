# List of changes wrt older configs
## LIST OF UPDATES WRT TO CONFIG 2016_Jul22:
- updated pdf for 2016 bkg to rms for bkgs and correlated to 17 and 18 for signals.
- updated PS parametrization, extrapolated from fiducial region 2018
- updated QCD scale for VBS QCD VV, extrapolated from fiducial region 2018 as Log-Normal
- dy rate parameters initialized to post-fit values

## LIST OF UPDATES WRT TO CONFIG 2016_Dec22:

- This is the release started on 22 may 2023 - latest to date.
- Modification to samples.py (both topologies):
    - removed `(Sum$(abs(GenPart_pdgId)==6)==0)` from ZZ_ewk signal (not needed here)
    - included both the tZq_ll bkg and the tZq obtained from `(Sum$(abs(GenPart_pdgId)==6)!=0)`(i.e. by reverting this cut)
    - changes on DY samples:
        - removed `DY_LO_pTllrw` and `DY_NLO_pTllrw`
        - removed  `DYJetsToLL_M-50_HT-70to100` and put the cut btw inclusive and HT-binned to `LHE_HT == 100`
        - removed all `DYJetsToLL_M-5to50_HT*`
        - split 'VZ' samples in 'VZ' and 'ZZlep', but we'll only use the ZZlep ones in the structure file - following ARC comments
        - removed 'WWG' from VVV samples as supposed to overlap with 'ggWW'

## LIST OF UPDATES WRT TO CONFIG 2016-v0:
- minor backgrounds are gathered in the datacards
- PS weights for DY, Vg, VgS, top are computed with the old method 
- some patches in the name conventions for Fakes
- JES are not log normal anymore (and they are included for all processes)
- b-tagging nuisances are shape


__________________________________________________
# list of commands to make it work (SM EWK):
1. run mkShape, get to end, and hadd
2. backup the file produced
```sh
cp /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/plots_VBS_ZV_6Dec2023_2016_boosted.root /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/plots_VBS_ZV_6Dec2023_2016_boosted_copy.root

cp /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/plots_VBS_ZV_6Dec2023_2016_resolved.root /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/plots_VBS_ZV_6Dec2023_2016_resolved_copy.root
```
Corrected samples will be stored at this path (if does not exists, mkdir): `/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections`


3. apply the patch for QCDscale VBS VV QCD background (extracted from 2018):
```sh
python ../../scripts/Utilities_nuisances/apply_nuisances_effect.py -i /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/plots_VBS_ZV_6Dec2023_2016_resolved.root -o \
/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_resolved_QCDvar.root --nuisance-effect \
../../2018-v1/resolved/QCDscale-plots_VBS_ZV_6Dec2023_2018_resolved.root -s VBS_VV_QCD -n QCDscale_VBS_VV_QCD

python ../../scripts/Utilities_nuisances/apply_nuisances_effect.py -i /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/plots_VBS_ZV_6Dec2023_2016_boosted.root -o \
/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_boosted_QCDvar.root --nuisance-effect \
../../2018-v1/boosted/QCDscale-plots_VBS_ZV_6Dec2023_2018_boosted.root -s VBS_VV_QCD -n QCDscale_VBS_VV_QCD
```
and the uncomment the corresponding nuisance from `nuisances_datacard.py` so can be included in the datacard

4. patch for PS weights: 
(N.b. ho dovuto togliere i fondi migliori per l'estrapolazione perché "other" non è ancora definito mentre scrivo nel 2018)
```sh
cd 2016-v1/resolved
python ../../scripts/Utilities_nuisances/apply_nuisances_effect.py -i /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/plots_VBS_ZV_6Dec2023_2016_resolved.root -o /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_resolved_PSvar.root --nuisance-effect ../../2018-v1/resolved/PS-plots_VBS_ZV_6Dec2023_2018_resolved.root -sf ../../2018-v1/resolved/samples_PS_extraction_2016.txt -n PS_FSR PS_ISR
cd ../boosted
python ../../scripts/Utilities_nuisances/apply_nuisances_effect.py -i /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/plots_VBS_ZV_6Dec2023_2016_boosted.root -o /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_boosted_PSvar.root --nuisance-effect ../../2018-v1/boosted/PS-plots_VBS_ZV_6Dec2023_2018_boosted.root -sf ../../2018-v1/boosted/samples_PS_extraction_2016.txt -n PS_FSR PS_ISR
```
and uncomment the corresponding nuisance from `nuisances.py` so can be included in the datacard
5. patch for QCD scale DY process
```sh
sh QCDnorm_datacards.sh _6Dec2023_2016 resolved 2016-v1
sh QCDnorm_datacards.sh _6Dec2023_2016 boosted 2016-v1
```

6. hadd files with the corrected ones

a.  WITH QCD scale DY corrections
```sh
hadd /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_resolved_wPS_wQCD_QCDscaleDY_corr.root \
/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_resolved_QCDvar.root \
/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_resolved_PSvar.root \
/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_resolved.root 

hadd /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_boosted_wPS_wQCD_QCDscaleDY_corr.root \
/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_boosted_QCDvar.root \
/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_boosted_PSvar.root \
/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_boosted.root 
```
b.  WITHOUT QCD scale DY corrections
```sh
hadd /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_resolved_wPS_wQCD.root \
/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_resolved_QCDvar.root \
/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_resolved_PSvar.root \
/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/plots_VBS_ZV_6Dec2023_2016_resolved.root 

hadd /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_boosted_wPS_wQCD.root \
/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_boosted_QCDvar.root \
/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_boosted_PSvar.root \
/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/plots_VBS_ZV_6Dec2023_2016_boosted.root 
```



7. make datacards (N.B.: use `nuisances_datacards.py` as input since I realized that when there are two nuisances entries with same name, the combineCards.py keeps only one of the two, i.e. in the case of `nuisances.py` would suppress all nuisances for backgrougs in JES, etc etc):
```sh
###without QCD corrections
cd 2016-v1/resolved
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_resolved_wPS_wQCD.root --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_6Dec2023_2016/  --skipMissingNuisance --nuisancesFile=../nuisances_datacards.py
cd ../boosted
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_boosted_wPS_wQCD.root --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_6Dec2023_2016/  --skipMissingNuisance --nuisancesFile=../nuisances_datacards.py
###with QCD corrections
cd ../resolved
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_resolved_wPS_wQCD_QCDscaleDY_corr.root --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_6Dec2023_2016_QCDscaleDY_corr/  --skipMissingNuisance --nuisancesFile=../nuisances_datacards.py
cd ../boosted
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_boosted_wPS_wQCD_QCDscaleDY_corr.root --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_6Dec2023_2016_QCDscaleDY_corr/  --skipMissingNuisance --nuisancesFile=../nuisances_datacards.py
###with QCD corrections and DY ln (for this need to update nuisances.py before)
cd ../resolved
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_resolved_wPS_wQCD_QCDscaleDY_corr.root --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_6Dec2023_2016_QCDscaleDY_corr_ln/  --skipMissingNuisance --nuisancesFile=../nuisances_datacards.py
cd ../boosted
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_boosted_wPS_wQCD_QCDscaleDY_corr.root --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_6Dec2023_2016_QCDscaleDY_corr_ln/  --skipMissingNuisance --nuisancesFile=../nuisances_datacards.py
```


To avoid unpleasant statistical fluctuations for nuisances of minor backgrouds in top cr (since those crs are very very pure), I am removing all nuisances from minor backgrouds in datacards for top cr. To try this out, please run again `mkDatacards.py` as follows (for the case of QCD corr+ln DY for instance)
```sh
cd ../resolved
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_resolved_wPS_wQCD_QCDscaleDY_corr.root --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_6Dec2023_2016_QCDscaleDY_corr_ln_topcr/ --skipMissingNuisance --nuisancesFile=../nuisances_datacards_topcr.py --cutsFile=cuts_resolved_topcr.py 
cd ../boosted
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_boosted_wPS_wQCD_QCDscaleDY_corr.root --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_6Dec2023_2016_QCDscaleDY_corr_ln_topcr/ --skipMissingNuisance --nuisancesFile=../nuisances_datacards_topcr.py --cutsFile=cuts_boosted_topcr.py 
```


8. do the statistical analysis (check combine2016 or combineRun2 folder)


__________________________________________________
# list of commands to make it work (EFT):
1. complete the list above for the SM EWK measurement and be sure to have the correct `variables.py` for both EWk and EFT processing
2. hadd EFT outputs, and the manually hadd EFT and EWK outputs:
```sh
hadd /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016-dim8/plots_VBS_ZV_6Dec2023_2016-dim8_boosted_wBkg.root /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016-dim8/plots_VBS_ZV_6Dec2023_2016-dim8_boosted.root /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_boosted_wPS_wQCD_QCDscaleDY_corr.root
```
In the example I merged the boosted dim-8 signals root file with the QCDscaleDY corrected smaples.
3. prepare datacards (picking up the desired EFT signals in the `structure-dim8.py` and in the `samples-datacards-dim8.py`) and using the `nuisances_datacards-dim8.py`:
```sh
cd 2016-v1/boosted-dim8
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016-dim8/plots_VBS_ZV_6Dec2023_2016-dim8_boosted_wBkg.root --skipMissingNuisance --nuisancesFile=../nuisances_datacards-dim8.py --samplesFile=../samples-datacards-dim8.py
```
You need to prepare one set of datacards per EFT operator, modifying samples, structure and configuration every time.
4. use the `EFT/datacards_categories_2016_EFT.sh` macro to combine categories (here for the single-here example)
5. launch the `EFT/eft.sh` script as follows:
```sh
sh eft.sh /eos/user/m/mpresill/CMS/VBS/VBS_ZV/DatacardsEFT/YearsCombination_8June2022/combined_boosted_bVeto.txt cT1 boosted_bVeto 
```

__________________________________________________
# list of commands to make it work (SM EWK+QCD):
The signal is now called "VBS_ZV_EWK_QCD" and includes the old "sm_dipole", i.e. ZV VBS EWK process (with top veto), and ZV QCD processes obtained from old VBS VV QCD samples (removing top contribution at gen level as well). For this joint contribution care must be taken when dealing with QCD scale uncertainty for 2016, since originally the QCD scale for VBS VV QCD was bugged so better to extract it from 2018 as we do for the sm ewk measurement.

1. hadd newly produced signals (`sh hadd``)

2. hadd the newly produced signals with the backgrounds produced for the EWK measurements (there is no problem if EWk and QCD signals are included in the hadd-ed root file, since they  will not overalp and we'll decide what to include in the datacardsa at a later stage):
```sh
###### boosted category
hadd -f /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_boosted_wBkg.root \
    /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_boosted.root \
    /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_boosted.root
###### resolved category 
hadd -f /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_resolved_wBkg.root /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_resolved.root /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_resolved.root 
```
we took the bkgs with correction on DY already applied, but with no PS corrections on top (that we apply in the next step).


3. patch for PS weights: 
(N.b. ho dovuto togliere i fondi migliori per l'estrapolazione perché "other" non è ancora definito mentre scrivo nel 2018)
```sh
cd 2016-v1/resolved_ewk_qcd
python ../../scripts/Utilities_nuisances/apply_nuisances_effect.py -i /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_resolved_wBkg.root -o /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_resolved_wBkg_PSvar.root --nuisance-effect /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2018_ewk_qcd/corrections/PS-plots_VBS_ZV_16Mar2024_2018_ewk_qcd_resolved.root -sf ../../2018-v1/resolved_ewk_qcd/samples_PS_extraction.txt -n PS_FSR PS_ISR
cd ../boosted_ewk_qcd
python ../../scripts/Utilities_nuisances/apply_nuisances_effect.py -i /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_boosted_wBkg.root -o /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_boosted_wBkg_PSvar.root --nuisance-effect /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2018_ewk_qcd/corrections/PS-plots_VBS_ZV_16Mar2024_2018_ewk_qcd_boosted.root -sf ../../2018-v1/boosted_ewk_qcd/samples_PS_extraction.txt -n PS_FSR PS_ISR
```
and uncomment the corresponding nuisance from `nuisances.py` so can be included in the datacard.

4. apply the patch for QCDscale VBS VV QCD background (extracted from 2018):
```sh
python ../../scripts/Utilities_nuisances/apply_nuisances_effect.py -i /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_resolved_wBkg.root -o /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_resolved_wBkg_QCDscale_ZV_EWK_QCDvar.root --nuisance-effect /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2018_ewk_qcd/corrections/QCDscale_ZV_EWK_QCD-plots_VBS_ZV_16Mar2024_2018_ewk_qcd_resolved.root -s VBS_ZV_EWK_QCD -n QCDscale_VBS_ZV_EWK_QCD

python ../../scripts/Utilities_nuisances/apply_nuisances_effect.py -i /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_resolved_wBkg.root -o /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_resolved_wBkg_QCDscale_VBS_WV_QCD_QCDvar.root --nuisance-effect /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2018_ewk_qcd/corrections/QCDscale_WV_QCD-plots_VBS_ZV_16Mar2024_2018_ewk_qcd_resolved.root -s VBS_WV_QCD -n QCDscale_VBS_WV_QCD

python ../../scripts/Utilities_nuisances/apply_nuisances_effect.py -i /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_resolved_wBkg.root -o /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_resolved_wBkg_QCDscale_tZq_QCD_QCDvar.root --nuisance-effect /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2018_ewk_qcd/corrections/QCDscale_tZq_QCD-plots_VBS_ZV_16Mar2024_2018_ewk_qcd_resolved.root -s tZq_QCD -n QCDscale_tZq_QCD
```
```sh
python ../../scripts/Utilities_nuisances/apply_nuisances_effect.py -i /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_boosted_wBkg.root -o /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_boosted_wBkg_QCDscale_ZV_EWK_QCDvar.root --nuisance-effect /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2018_ewk_qcd/corrections/QCDscale_ZV_EWK_QCD-plots_VBS_ZV_16Mar2024_2018_ewk_qcd_boosted.root -s VBS_ZV_EWK_QCD -n QCDscale_VBS_ZV_EWK_QCD

python ../../scripts/Utilities_nuisances/apply_nuisances_effect.py -i /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_boosted_wBkg.root -o /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_boosted_wBkg_QCDscale_VBS_WV_QCD_QCDvar.root --nuisance-effect /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2018_ewk_qcd/corrections/QCDscale_WV_QCD-plots_VBS_ZV_16Mar2024_2018_ewk_qcd_boosted.root -s VBS_WV_QCD -n QCDscale_VBS_WV_QCD

python ../../scripts/Utilities_nuisances/apply_nuisances_effect.py -i /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_boosted_wBkg.root -o /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_boosted_wBkg_QCDscale_tZq_QCD_QCDvar.root --nuisance-effect /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2018_ewk_qcd/corrections/QCDscale_tZq_QCD-plots_VBS_ZV_16Mar2024_2018_ewk_qcd_boosted.root -s tZq_QCD -n QCDscale_tZq_QCD
```

5. hadd files with the corrected ones
WITH QCD scale DY corrections
```sh
hadd /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_resolved_wBkg_wPS_wQCDscales_QCDscaleDY_corr.root \
/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_resolved_wBkg.root \
/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_resolved_wBkg_PSvar.root \
/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_resolved_wBkg_QCDscale_ZV_EWK_QCDvar.root \
/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_resolved_wBkg_QCDscale_VBS_WV_QCD_QCDvar.root \
/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_resolved_wBkg_QCDscale_tZq_QCD_QCDvar.root

hadd /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_boosted_wBkg_wPS_wQCDscales_QCDscaleDY_corr.root \
/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_boosted_wBkg.root \
/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_boosted_wBkg_PSvar.root \
/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_boosted_wBkg_QCDscale_ZV_EWK_QCDvar.root \
/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_boosted_wBkg_QCDscale_VBS_WV_QCD_QCDvar.root \
/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_boosted_wBkg_QCDscale_tZq_QCD_QCDvar.root

```




6. make datacards(N.B.: use `nuisances_datacards.py` as input since I realized that when there are two nuisances entries with same name, the combineCards.py keeps only one of the two, i.e. in the case of `nuisances.py` would suppress all nuisances for backgrougs in JES, etc etc):
```sh
###with QCD corrections and DY ln (for this need to update nuisances.py before)
cd ../resolved_ewk_qcd
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_resolved_wBkg_wPS_wQCDscales_QCDscaleDY_corr.root  --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_16Mar2024_2016_ewk_qcd_QCDscaleDY_corr_ln/ --skipMissingNuisance --nuisancesFile=../nuisances_datacards_ewk_qcd.py 
cd ../boosted_ewk_qcd
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_boosted_wBkg_wPS_wQCDscales_QCDscaleDY_corr.root  --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_16Mar2024_2016_ewk_qcd_QCDscaleDY_corr_ln/ --skipMissingNuisance --nuisancesFile=../nuisances_datacards_ewk_qcd.py
```
To avoid unpleasant statistical fluctuations for nuisances of minor backgrouds in top cr (since those crs are very very pure), I am removing all nuisances from minor backgrouds in datacards for top cr. To try this out, please run again `mkDatacards.py` as follows (for the case of QCD corr+ln DY for instance)
```sh
cd ../resolved_ewk_qcd
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_resolved_wBkg_wPS_wQCDscales_QCDscaleDY_corr.root  --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_16Mar2024_2016_ewk_qcd_QCDscaleDY_corr_ln_topcr/ --skipMissingNuisance --nuisancesFile=../nuisances_datacards_topcr.py --cutsFile=cuts_resolved_topcr.py 
cd ../boosted_ewk_qcd
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2016_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2016_ewk_qcd_boosted_wBkg_wPS_wQCDscales_QCDscaleDY_corr.root  --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_16Mar2024_2016_ewk_qcd_QCDscaleDY_corr_ln_topcr/ --skipMissingNuisance --nuisancesFile=../nuisances_datacards_topcr.py --cutsFile=cuts_boosted_topcr.py
``````
