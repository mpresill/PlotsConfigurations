# LIST OF UPDATES WRT TO CONFIG 2016_Jul22:


>updated pdf for 2016 bkg to rms for bkgs and correlated to 17 and 18 for signals.
>updated PS parametrization, extrapolated from fiducial region 2018
>updated QCD scale for VBS QCD VV, extrapolated from fiducial region 2018 as Log-Normal
>dy rate parameters initialized to post-fit values

# LIST OF UPDATES WRT TO CONFIG 2016_Dec22:

> This is the release started on 22 may 2023 - latest to date.
> Modification to samples.py (both topologies):
    > removed `(Sum$(abs(GenPart_pdgId)==6)==0)` from ZZ_ewk signal (not needed here)
    > included both the tZq_ll bkg and the tZq obtained from `(Sum$(abs(GenPart_pdgId)==6)!=0)`(i.e. by reverting this cut)
    >changes on DY samples:
        > removed `DY_LO_pTllrw` and `DY_NLO_pTllrw`
        > removed  `DYJetsToLL_M-50_HT-70to100` and put the cut btw inclusive and HT-binned to `LHE_HT == 100`
        >removed all `DYJetsToLL_M-5to50_HT*`
        > split 'VZ' samples in 'VZ' and 'ZZlep', but we'll only use the ZZlep ones in the structure file - following ARC comments
        > removed 'WWG' from VVV samples as supposed to overlap with 'ggWW'



# LIST OF UPDATES WRT TO CONFIG 2016-v0:
> minor backgrounds are gathered in the datacards
> PS weights for DY, Vg, VgS are computed with the old method 
> some patches in the name conventions for Fakes
> JES/JER are not log normal anymore (and they are included for all processes)
> b-tagging nuisances are shape


__________________________________________________
# list of commands to make it work:
> run mkShape, get to end, and hadd
>backup the file produced
```sh
cp /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/plots_VBS_ZV_6Dec2023_2016_boosted.root /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/plots_VBS_ZV_6Dec2023_2016_boosted_copy.root

cp /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/plots_VBS_ZV_6Dec2023_2016_resolved.root /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/plots_VBS_ZV_6Dec2023_2016_resolved_copy.root
```

> apply the patch for QCDscale VBS VV QCD background (extracted from 2018):
```sh
python ../../scripts/Utilities_nuisances/apply_nuisances_effect.py -i /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/plots_VBS_ZV_6Dec2023_2016_resolved.root -o \
plots_VBS_ZV_6Dec2023_2016_resolved_QCDvar.root --nuisance-effect \
../../2018-v0/resolved/QCDscale-plots_VBS_ZV_21Aug2023_2018_resolved.root -s VBS_VV_QCD -n QCDscale_VBS_VV_QCD

python ../../scripts/Utilities_nuisances/apply_nuisances_effect.py -i /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/plots_VBS_ZV_6Dec2023_2016_boosted.root -o \
plots_VBS_ZV_6Dec2023_2016_boosted_QCDvar.root --nuisance-effect \
../../2018-v0/boosted/QCDscale-plots_VBS_ZV_21Aug2023_2018_boosted.root -s VBS_VV_QCD -n QCDscale_VBS_VV_QCD
```
> and the uncomment the corresponding nuisance from `nuisances.py` so can be included in the datacard

> patch for PS weights: 
>(N.b. ho dovuto togliere i fondi migliori per l'estrapolazione perché "other" non è ancora definito mentre scrivo nel 2018)
```sh
python ../../scripts/Utilities_nuisances/apply_nuisances_effect.py -i /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/plots_VBS_ZV_6Dec2023_2016_resolved.root -o plots_VBS_ZV_6Dec2023_2016_resolved_PSvar.root --nuisance-effect ../../2018-v0/resolved/PS-plots_VBS_ZV_21Aug2023_2018_resolved.root -sf ../../2018-v0/resolved/samples_PS_extraction_2016.txt -n PS_FSR PS_ISR

python ../../scripts/Utilities_nuisances/apply_nuisances_effect.py -i /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/plots_VBS_ZV_6Dec2023_2016_boosted.root -o plots_VBS_ZV_6Dec2023_2016_boosted_PSvar.root --nuisance-effect ../../2018-v0/boosted/PS-plots_VBS_ZV_21Aug2023_2018_boosted.root -sf ../../2018-v0/boosted/samples_PS_extraction_2016.txt -n PS_FSR PS_ISR
```
> and the uncomment the corresponding nuisance from `nuisances.py` so can be included in the datacard
> patch for QCD scale DY process
```sh
sh QCDnorm_datacards.sh _6Dec2023_2016 resolved 2016-v1
sh QCDnorm_datacards.sh _6Dec2023_2016 boosted 2016-v1
```

> hadd files with the corrected ones
```sh
hadd plots_VBS_ZV_6Dec2023_2016_resolved_wPS_wQCD.root \
plots_VBS_ZV_6Dec2023_2016_resolved_QCDvar.root \
plots_VBS_ZV_6Dec2023_2016_resolved_PSvar.root \
plots_VBS_ZV_6Dec2023_2016_resolved.root 

hadd plots_VBS_ZV_6Dec2023_2016_boosted_wPS_wQCD.root \
plots_VBS_ZV_6Dec2023_2016_boosted_QCDvar.root \
plots_VBS_ZV_6Dec2023_2016_boosted_PSvar.root \
plots_VBS_ZV_6Dec2023_2016_boosted.root 
```

> make datacards:
```sh
mkDatacards.py --pycfg=configuration.py --inputFile=plots_VBS_ZV_6Dec2023_2016_resolved_wPS_wQCD.root --skipMissingNuisance
mkDatacards.py --pycfg=configuration.py --inputFile=plots_VBS_ZV_6Dec2023_2016_boosted_wPS_wQCD.root --skipMissingNuisance
```

> do the statistical analysis (check combine2016 or combineRun2 folder)